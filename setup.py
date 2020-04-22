import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tzconvert",
    version="0.0.2.post1",
    author="Sourav Banerjee",
    author_email="srvasn@gmail.com",
    description="Make naive datetime objects timezone aware using city names",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/srvasn/tzconvert",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "python-dateutil>=2.8.1",
        "requests>=2.23.0",
        "lxml>=4.5.0"
    ],
    python_requires='>=3.0',
)