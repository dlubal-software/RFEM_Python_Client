import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Reports.html import ExportResultTablesToHtml
from RFEM.initModel import Model, url
from shutil import rmtree
import pytest

if Model.clientModel is None:
    Model()

@pytest.mark.skipif(url != 'http://127.0.0.1', reason="This test fails on remote PC due to incorrect file path. \
                    Althought it is easy to change, it would not be easy to update on every remote computer.\
                    It is not necessary to evaluate Client as functional. Localy this tests still gets executed.")
def test_html_report():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.run_script('..\\scripts\\internal\\Demos\\Demo-003 Castellated Beam.js')
    Model.clientModel.service.calculate_all(False)

    dirname = os.path.join(os.getcwd(), os.path.dirname(__file__))
    # Remove any previous results if they exist
    folderPath = os.path.join(dirname, 'testResults')
    if os.path.isdir(folderPath):
        rmtree(folderPath)
    ExportResultTablesToHtml(folderPath)

    assert os.path.exists(folderPath)
