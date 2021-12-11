import sys
from pathlib import Path

# Add the pygrader directory to the python search path
sys.path.append(str(Path(__file__).resolve().parent / "pygrader_repo"))

import pygrader


def my_callback(student_code_path, lab_name, **kw):
    lab_report_path = student_code_path / "lab_report.txt"
    if lab_report_path.is_file():
        print(open(lab_report_path).read())
    else:
        raise pygrader.CallbackFailed("Missing lab_report.txt")


grader = pygrader.Grader("example", "lab1", "learning_suite/grades.csv", "lab1_labreport", 10)
grader.set_callback_fcn(my_callback)
grader.set_submission_system_learning_suite("learning_suite/lab1_submissions.zip")
grader.run()
