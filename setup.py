from setuptools import find_packages
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent
readme = (here/"README.md").read_text()

setup(
    name='RFEM',
    version='1.11.0',
    description='Python Framework for RFEM6 Web Services',
    long_description=readme,
    long_description_content_type = "text/markdown",
    url="https://github.com/Dlubal-Software/RFEM_Python_Client",
    author="Dlubal Software",
    author_email="info@dlubal.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10"
    ],
    packages=find_packages(),
    package_dir={"RFEM":"RFEM"},
    include_package_data=True,
    install_requires=["requests", "six", "suds-py3", "xmltodict", "pytest", "mock", "setuptools"],
    zip_safe = False
)
