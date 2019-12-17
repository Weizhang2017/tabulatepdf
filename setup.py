import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tabulatepdf",
    version="0.1",
    author="Wei Zhang",
    author_email="zhangw1.2011@gmail.com",
    description="A CLI for tabula-py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Weizhang2017/tabulatepdf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['bin/tabulatepdf'],
    install_requires=['tabula-py'],
)
