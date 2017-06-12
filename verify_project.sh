#!/usr/bin/env bash
set -e

py.test tests
pylint demo_python_at/
pylint tests/
flake8 demo_python_at/
pylint demo_python_at/
pylint tests/

echo "Good job!"
