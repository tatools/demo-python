#!/usr/bin/env bash
set -e

py.test --cov=demo_python_at tests
flake8 demo_python_at/
pydocstyle --config=.pydocstyle demo_python_at
pylint demo_python_at/

echo "Good job!"
