import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="valedictory",
    version="0.0.1",
    author="Benjamin E Krikler",
    author_email="bkrikler@gmail.com",
    description="Effective dictionary and nested object validation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benkrikler/valedictory",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
