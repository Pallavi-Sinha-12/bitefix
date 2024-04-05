from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="bitefix",
    version="1.0.2",
    description="""Bitefix is an efficient library designed to streamline Python Runtime error debugging with AI-powered decorators. 
    It initializes a crew of AI agents which work together to diagnose the error, generate ideas to fix the error, 
    evaluate the ideas to choose the best and develop the code to fix the error that occurred.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Pallavi Sinha",
    packages=find_packages(include=["bitefix"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    license="MIT",
    url="https://github.com/Pallavi-Sinha-12/bitefix",
    python_requires=">=3.10",
)
