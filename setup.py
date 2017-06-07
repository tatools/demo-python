from setuptools import setup

with open("README.md") as readme_file:
    description = readme_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name="demo_at",
    version="0.1.0",
    description="A demo of Python's project with automated tests.",
    long_description=description,
    url="https://github.com/tatools/demo-python",
    packages=["demo_python_at"],
    install_requires=requirements,
    license="Apache-2.0",
)
