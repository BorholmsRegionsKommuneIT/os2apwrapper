from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="os2apwrapper",
    version="0.0.1",
    description="A modul for updating phase/status by process id in os2autoprocess",
    package_dir={"": "os2apwrapper"},
    packages=find_packages(where="os2apwrapper"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BorholmsRegionsKommuneIT/os2apwrapper",
    author="nk11-dat",
    author_email="nicki.kielsen@brk.dk",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests','python-dotenv', 'typing'],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)