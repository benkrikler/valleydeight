import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="valleydeight",
    version="0.0.1",
    author="Ben Krikler",
    author_email="b.krikler@gmail.com",
    description="Effective dictionary and nested object validation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benkrikler/valleydeight",
    packages=setuptools.find_packages(),
    install_requires=['six'],
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ),
)
