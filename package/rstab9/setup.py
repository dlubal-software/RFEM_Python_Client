from setuptools import find_packages
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent
readme = (here/"README.md").read_text()

setup(
    name='dlubal-rstab-9',
    version='1.0.2',
    description='Open API project for RSTAB',
    long_description=readme,
    long_description_content_type = "text/markdown",
    url="https://github.com/Dlubal-Software/RFEM_Python_Client",
    author="Dlubal Software",
    author_email="info@dlubal.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9"
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["suds", "requests", "suds_requests", "xmltodict", "setuptools==58.0.0"],
    zip_safe = False
)
