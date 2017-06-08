#!/usr/bin/env bash
set -e

py.test tests
pylint demo_python_at/
pylint tests/

echo "Good job!"
