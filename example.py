import sys
import pathlib

YGRADER_PATH = pathlib.Path(__file__).resolve().parent / "ygrader_repo"
sys.path.append(str(YGRADER_PATH))
import ygrader

def my_callback(student_code_path, lab_name, **kw):
    print("*** Grading", lab_name, "***\n")

    lab_report_path = student_code_path / "lab_report.txt"
    if lab_report_path.is_file():
        print(open(lab_report_path).read())
    else:
        raise ygrader.CallbackFailed("Missing lab_report.txt")


grader = ygrader.Grader(
    lab_name="lab1",
    grades_csv_path="learning_suite/grades.csv",
)
grader.add_item_to_grade("lab1_labreport", my_callback, max_points = 10)
grader.set_submission_system_learning_suite("learning_suite/lab1_submissions.zip")
grader.run()
