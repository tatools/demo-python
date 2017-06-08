#!/usr/bin/env bash
set -e

py.test tests
flake8 demo_python_at/

echo "Good job!"