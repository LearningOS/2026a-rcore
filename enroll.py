"""Send a login or students.txt to the LearningOS enrollment hub."""

import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
HUB = "LearningOS/2026a-enroll"
COURSE_ID = "2073"


def read_students(arguments, path):
    if len(arguments) > 1:
        raise ValueError("Usage: python3 enroll.py [GITHUB_LOGIN]")
    lines = arguments if arguments else path.read_text().splitlines()
    students = []
    seen = set()
    for line in lines:
        login = line.split("#", 1)[0].strip()
        if not login:
            continue
        if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", login):
            raise ValueError(f"Invalid GitHub login: {login}")
        if login.lower() not in seen:
            seen.add(login.lower())
            students.append(login)
    if not students:
        raise ValueError("Add GitHub logins to students.txt first.")
    return students


def github(path):
    output = subprocess.check_output(["gh", "api", "--hostname", "github.com", path], text=True)
    return json.loads(output)


def main():
    logins = read_students(sys.argv[1:], ROOT / "students.txt")
    member = github("user/memberships/orgs/LearningOS")
    if member["state"] != "active" or member["role"] != "admin":
        raise ValueError("Run this script as a LearningOS organization owner.")

    # Validate the whole roster before starting the first enrollment.
    students = []
    for login in logins:
        student = github("users/" + login)
        if student["type"] != "User":
            raise ValueError(login + " is not a personal GitHub account.")
        students.append(student)

    for student in students:
        inputs = {"course": COURSE_ID, "student_id": str(student["id"])}
        request = {"ref": "main", "inputs": inputs, "return_run_details": True}
        path = f"repos/{HUB}/actions/workflows/manual-enroll.yml/dispatches"
        result = subprocess.run(["gh", "api", "--hostname", "github.com", path, "--input", "-"],
                                input=json.dumps(request), text=True, stdout=subprocess.PIPE, check=True)
        run = json.loads(result.stdout)
        print(student["login"], run["html_url"], flush=True)
        subprocess.run(["gh", "run", "watch", str(run["workflow_run_id"]),
                        "--repo", "github.com/" + HUB, "--exit-status"], check=True)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as error:
        sys.exit(str(error))
