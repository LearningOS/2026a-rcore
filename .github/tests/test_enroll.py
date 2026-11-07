"""Maintainer fallback uses the same verified enrollment implementation."""

import importlib.util
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("maintainer_enroll", ROOT / "enroll.py")
enroll = importlib.util.module_from_spec(spec)
spec.loader.exec_module(enroll)


class EnrollmentTests(unittest.TestCase):
    def test_invalid_login_is_rejected_before_provisioning(self):
        self.assertEqual(enroll.read_students(["Alayfolk64"], None), ["Alayfolk64"])
        for login in ("../bad", "student/name", "student@example.org", "student user", "-student"):
            with self.subTest(login=login), self.assertRaises(ValueError):
                enroll.read_students([login], None)

    def test_roster_skips_comments_and_duplicate_logins(self):
        with patch.object(Path, "read_text", return_value="\n# class\nAlice # lab 1\nalice\nBob\n"):
            self.assertEqual(enroll.read_students([], Path("students.txt")), ["Alice", "Bob"])

    def test_owner_submits_canonical_id_and_waits_for_exact_run(self):
        import json
        from subprocess import CompletedProcess

        user = {"type": "User", "login": "Student", "id": 42}
        dispatched = CompletedProcess([], 0, stdout='{"workflow_run_id": 123, "html_url": "run"}')
        with patch.object(sys, "argv", ["enroll.py", "student"]), patch.object(
                enroll, "github", side_effect=[{"state": "active", "role": "admin"}, user]), patch.object(
                enroll.subprocess, "run", return_value=dispatched) as run:
            enroll.main()
        dispatch, watch = run.call_args_list
        self.assertIn("repos/LearningOS/2026a-enroll/actions/workflows/manual-enroll.yml/dispatches", dispatch.args[0])
        self.assertEqual(json.loads(dispatch.kwargs["input"])["inputs"],
                         {"course": enroll.COURSE_ID, "student_id": "42"})
        self.assertIn("123", watch.args[0])
        self.assertIn("--exit-status", watch.args[0])

    def test_non_owner_and_invalid_roster_never_dispatch(self):
        owner = {"state": "active", "role": "admin"}
        for answers in ([{"state": "active", "role": "member"}],
                        [owner, {"type": "User", "id": 1}, {"type": "Organization"}]):
            with patch.object(enroll, "read_students", return_value=["student", "org"]), patch.object(
                    enroll, "github", side_effect=answers), patch.object(enroll.subprocess, "run") as run:
                with self.assertRaises(ValueError):
                    enroll.main()
                run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
