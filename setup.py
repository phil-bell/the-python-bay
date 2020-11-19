import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-philhabell", # Replace with your own username
    version="0.0.1",
    author="Phil Bell",
    author_email="philhabell@gmail.com",
    description="A simple package for searching thepiratebay.org",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/philhabell/the-python-bay",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)