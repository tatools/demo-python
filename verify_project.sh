#!/usr/bin/env bash
set -e

py.test --cov=demo_python_at
flake8 demo_python_at/

echo "Good job!"
