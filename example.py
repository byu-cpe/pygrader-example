import ygrader


def my_callback(student_code_path, lab_name, **kw):
    print("*** Grading", lab_name, "***\n")

    lab_report_path = student_code_path / "lab_report.txt"
    if lab_report_path.is_file():
        print(open(lab_report_path).read())
    else:
        raise ygrader.CallbackFailed("Missing lab_report.txt")


grader = ygrader.Grader(
    name="example",
    lab_name="lab1",
    grades_csv_path="learning_suite/grades.csv",
    grades_col_name="lab1_labreport",
    points=10,
)
grader.set_callback_fcn(my_callback)
grader.set_submission_system_learning_suite("learning_suite/lab1_submissions.zip")
grader.run()
