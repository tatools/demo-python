demo-python
===========
A demo of Python's project with automated tests.

How to install?
===============
1. Create separate virtual environment with Python 3.5.x.
2. Run `pip install -r requirements-dev.txt` to install required Python's dependencies.

How to run automated tests?
============================
1. Run `py.test demo_python_at` within your virtual environment.
2. Run `py.test --cov=demo_python_at tests/` within your virtual environment to run tests with coverage. 
 
How to validate my changes?
===========================
Run `./verify_project.sh` and make sure you have `Good job!` message in the end of execution otherwise please fix errors.
