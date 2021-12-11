import sys

# Add the parent directory to the Pythons search path
sys.path.append("..")

import pygrader


def my_callback(student_code_path, lab_name, **kw):
    print(student_code_path)


grader = pygrader.Grader("example", "lab1", "grades.csv", "lab1_labreport", 10)
grader.set_callback_fcn(my_callback)
grader.run()
