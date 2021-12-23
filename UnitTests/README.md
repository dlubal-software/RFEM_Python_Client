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
1) Open RFEM 6 application. Check if there are no opened dialogues in RFEM and server port range under *Options-Web Services* corresponds to the one set in initModel.
2) Run whole `.\UnitTests` folder. This ensure maximum scope. Execution is independent of current working directory. Pytest has many parameters it can be runned with refer to help via `pytest -h` or documentation. Ensure that all tests are either passed or skipped.
```
> pytest --tb=no .\RFEM_Python_Client\UnitTests
```
output:
![image](https://user-images.githubusercontent.com/37547309/147245670-db248e57-95f6-4f00-9b5b-8a89033dcc2a.png)
Labels: . - passed, s - skipped, e - error, f - failed

3) To asses code coverage, run `coverage`. Pytest can be exetuted inside coverage, leaving nothing out. Coverage enables to automaticaly create formated output (html, json, or dxf). Again, for more information refer to help `coverage -h` and `coverage html -h` for details about html. In html the results can be sorted or filtered and files can be inspected separately.
```
> coverage run -m pytest --tb=no .\RFEM_Python_Client\UnitTests
...
> coverage html [target folder]
> start [target folder\index.html]
```
![image](https://user-images.githubusercontent.com/37547309/147244988-e0124457-dcb0-4d03-a10a-7d73a544d5d8.png)

![image](https://user-images.githubusercontent.com/37547309/147245207-530f75fa-33b3-4cec-9f01-8b81da8b3edd.png)

## Contribute
Contributions are always welcome! Just ensure consistency with other unit tests by startinh with `UnitTests/template.py`
