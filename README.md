# Uncommon Python Error: ZeroDivisionError Despite Zero Checks

This repository demonstrates a subtle error that can lead to a `ZeroDivisionError` in Python, even when there are seemingly adequate checks to prevent division by zero.

The `bug.py` file contains the buggy code. The error occurs because although the function checks for `a` or `b` being zero, it does not prevent the division if both are non-zero.

The `bugSolution.py` file shows how to fix the error by adding a comprehensive check to avoid division by zero in all cases.

This example illustrates the importance of thoroughly considering edge cases when writing functions and how seemingly correct logic can sometimes overlook subtle flaws that result in unexpected errors.