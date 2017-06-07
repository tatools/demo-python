demo-python
===========
A demo of Python's project with automated tests.

[![Build Status](https://travis-ci.org/tatools/demo-python.svg?branch=master)](https://travis-ci.org/tatools/demo-python)

How to install?
===============
1. Create separate virtual environment with Python 3.5.x.
2. Run `pip install -r requirements.txt` to install required Python's dependencies.

How to install as Python dependency?
====================================
Run `python setup.py install`.

How to run automated tests?
===========================
Run `py.test demo_python_at` within your virtual environment.
 
How to validate my changes?
===========================
Run `./verify_project.sh` and make sure you have `Good job!` message in the end of execution otherwise please fix errors.
