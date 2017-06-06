#!/usr/bin/env bash
set -e

py.test --cov=demo_python_at tests/

echo "Good job!"