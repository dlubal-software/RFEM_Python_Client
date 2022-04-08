# A guide to unit testing
![image](https://img.shields.io/badge/framework-pytest-orange) ![image](https://img.shields.io/badge/code%20coverage-coverage-orange)

## Description
Testing framework to check all RFEM Python Client objects and types. Using `pytest` pkg enables user to run all test together or separately. This is to be maintained. Testing procedure should be exetuded before every commit to ensure compatibility.

## Getting started
### Dependencies
* [pytest](https://docs.pytest.org/) or [pytest](https://pypi.org/project/pytest/) ([pdf documentation](https://buildmedia.readthedocs.org/media/pdf/pytest/latest/pytest.pdf)) Install by executing `pip install pytest`
* [coverage](https://docs.python-requests.org/en/master/) Install by executing `pip install coverage`
* RFEM 6 application

### Step by step
1) Open RFEM 6 application. Always set language to English. The best version of RFEM is current GM, unless you are testing features that are not merged. Check if there are no opened dialogues in RFEM and server port range under *Options-Web Services* corresponds to the one set in initModel.
2) Run whole `.\UnitTests` folder to exetue tests or `.\UnitTests\Examples.py` to execute all examples. This ensure maximum scope. Execution is independent of current working directory. Pytest has many parameters it can be runned with. Refer to help (via `pytest -h`) or documentation. Ensure that all tests are either passed or skipped conditionally.
```
> pytest --tb=no .\RFEM_Python_Client\UnitTests # silent mode
> pytest -s .\RFEM_Python_Client\UnitTests\test_zCalculate.py # verbose, printing out every print() in test
> pytest -s .\RFEM_Python_Client\UnitTests\Examples.py # execute all examples
```
output:
![image](https://user-images.githubusercontent.com/37547309/147245670-db248e57-95f6-4f00-9b5b-8a89033dcc2a.png)
Indication: . - passed, s - skipped, e - error, f - failed

3) To assess code coverage, run `coverage`. Pytest can be executed inside coverage process, leaving nothing out. Coverage enables to automaticaly create formated output (html, json, or dxf). Again, for more information refer to help (`coverage -h`) and html (`coverage html -h`). In html the results can be sorted out or filtered. Files can be inspected separately. Coverage results can be directed into UnitTests folder since they are ignored by github and they will not be commited to repository. Use separate folder for the results. There is a lot of files generated.
```
> coverage run -m pytest --tb=no .\RFEM_Python_Client\UnitTests
...
> coverage html [target folder]
> start [target folder\index.html]
```
![image](https://user-images.githubusercontent.com/37547309/147244988-e0124457-dcb0-4d03-a10a-7d73a544d5d8.png)

![image](https://user-images.githubusercontent.com/37547309/147245207-530f75fa-33b3-4cec-9f01-8b81da8b3edd.png)

## Contribute
Contributions are always welcome! Just be sure to start with `UnitTests/template.py`
