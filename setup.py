import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utm_zone", # Replace with your own username
    version="1.0.1",
    author="Per Liedman",
    author_email="per@liedman.net",
    description="Find the UTM zone for your GeoJSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/perliedman/py-utm-zone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
