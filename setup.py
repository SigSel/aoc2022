import os
import pathlib

from setuptools import setup, find_packages

# The name of the package, and a short 1-line description.
package_name = "aoc2022"
description = "Advent of Code 2022"

# Path to the README and requirements files
readme_file = pathlib.Path("README.md")
requirements_file = pathlib.Path("requirements.txt")

# Path to the root directory in which the package directories reside.
root_dir = pathlib.Path(".")

# Main maintainer name and email
maintainer = "Sigvard Johansen Seljelv"
email = ""

# Required version of Python, and classifiers
required_python_version = ">=3.8.0"
classifiers = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10"
]

# Additional non-standard requirements
extras_requirements = {
    "dev": []
}

if os.environ.get("CI") and os.environ.get("CI_COMMIT_TAG"):
    version = os.environ.get("CI_COMMIT_TAG")
    from packaging.version import Version as PEP440Version  # Only import packaging in the pipeline
    PEP440Version(version)  # Raises packaging.version.InvalidVersion if not a valid version.
else:
    version = "local"
url = os.environ.get("CI_PROJECT_URL", "")

readme = None
readme_type = "text/markdown"
if readme_file.exists():
    if readme_file.suffix == ".rst":
        readme_type = "text/x-rst"
    with open(readme_file) as file:
        readme = file.read()

requirements = []
if requirements_file.exists():
    with open(requirements_file) as f:
        requirements = [line for line in f.read().splitlines() if "#" not in line and " " not in line]

setup(
    name=package_name,
    version=version,
    packages=find_packages(where=str(root_dir)),
    package_dir={"": str(root_dir)},
    maintainer=maintainer,
    maintainer_email=email,
    url=url,
    project_urls={},
    description=description,
    long_description=readme,
    long_description_content_type=readme_type,
    license="GPL-3.0",
    install_requires=requirements,
    extras_require=extras_requirements,
    python_requires=required_python_version,
    include_package_data=True,
    package_data={"": ["README.*", "LICENSE", "requirements.txt"]},
    classifiers=classifiers
)

if version == "local":
    print("\n\n !!!!")
    print("A PACKAGE WAS BUILT WITH VERSION 'local'")