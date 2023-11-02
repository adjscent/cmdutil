from setuptools import find_packages, setup

__version__ = "0.0.1"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Typing :: Typed",
]

setup(
    name="cmdutil",
    version=__version__,
    packages=find_packages(exclude=["tests*", "docs"]),
    author="adjscent",
    author_email="me@imsj.dev",
    description="command line utility written in Python that performs os functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["cmdutil = cmdutil.cli:main"]},
    install_requires=[],
    classifiers=classifiers,
    python_requires=">=3.8",
    project_urls={"Repository": "https://github.com/adjscent/cmdutil"},
)
