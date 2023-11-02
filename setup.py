from setuptools import setup, find_packages

__version__ = "0.0.1"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cmdutil",
    version=__version__,
    packages=find_packages(exclude=["tests*", "docs"]),
    author="adjscent",
    author_email="me@imsj.dev",
    description="command line utility written in Python that performs os functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "cmdutil = cmdutil.cli:main",
        ],
    },
    install_requires=[],
)
