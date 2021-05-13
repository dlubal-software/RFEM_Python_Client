# RfemPythonWsClient
Python client (or high-level functions) for RFEM 6 using Web Services (WS), SOAP and WSDL
## Short description
This Python project is focused on opening RFEM 6 to all our customers, enabling them to interact with RFEM on much higher level. If you are looking for tool to help you solve parametric models or optimization tasks, you are on the right place. This project and comunity will create support for all your projects. The goal is to create easily expandable Python library communicating instructions to RFEM through WS. WS anable you to access your local version of RFEM or remote via internet connection.
## Architecture
![image](https://user-images.githubusercontent.com/37547309/118119185-44a22f00-b3ee-11eb-9d60-3d74a4a96f81.png)
### Data Structure
* main.py:      setting of individual objects by one line entry
* window.py:    definition of GUI layer; called first
* initModel.py: runs after window and initializes suds.Client by connecting to `http://localhost:8081/wsdl` and active model in RFEM
* enums.py:     definition of enums
* dataTypes.py: definition of special data types
* RFEM:         folder folloving structure of RFEM 6 navigator containing individual types of objects
## Getting started
### Dependencies
* SUDS library
* RFEM 6 application
### Step by step
1) Download repo (main.py + RFEM folder) or instal pkg via command line `pip install RfemPythonWsClient`
2) Open RFEM 6 application
3) Check that there are no opened dialogues in RFEM and server port range under *Options-Web Services* 8081 or corresponds with the one set in initModel
4) Update main.py and run from this location.
### Examples
Examples can be found under Examples folder.
## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Contribute
Contributions are always welcome! Please ensure your pull request adheres to the following guidelines:

* Alphabetize your entry.
* Search previous suggestions before making a new one, as yours may be a duplicate.
* Suggested READMEs should be beautiful or stand out in some way.
* Make an individual pull request for each suggestion.
* New categories, or improvements to the existing categorization are welcome.
* Keep descriptions short and simple, but descriptive.
* Start the description with a capital and end with a full stop/period.
* Check your spelling and grammar.
* Make sure your text editor is set to remove trailing whitespace.
* Use the #readme anchor for GitHub READMEs to link them directly
