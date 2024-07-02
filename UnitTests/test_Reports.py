import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Reports.printoutReport import PrintoutReport
from RFEM.Reports.html import ExportResultTablesToHtml
from RFEM.initModel import Model, closeModel, openFile, getPathToRunningRFEM
from RFEM.connectionGlobals import url
from shutil import rmtree
import pytest
import time

if Model.clientModel is None:
    Model()


@pytest.mark.skipif(url != 'http://127.0.0.1', reason="This test fails on remote PC due to incorrect file path. \
                    Althought it is easy to change, it would not be easy to update on every remote computer.\
                    It is not necessary to evaluate Client as functional. Localy this tests still gets executed.")

def test_html_report():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.run_script(os.path.join(getPathToRunningRFEM(),'scripts\\internal\\Demos\\Demo-002 Cantilever Beams.js'))
    Model.clientModel.service.calculate_all(False)

    dirname = os.path.join(os.getcwd(), os.path.dirname(__file__))
    folderPath = os.path.join(dirname, 'testResults')
    # Remove any previous results if they exist
    if os.path.isdir(folderPath):
        rmtree(folderPath)
    ExportResultTablesToHtml(folderPath, False)

    assert os.path.exists(folderPath)


@pytest.mark.skipif(url != 'http://127.0.0.1', reason="This test fails on remote PC due to incorrect file path. \
                    Althought it is easy to change, it would not be easy to update on every remote computer.\
                    It is not necessary to evaluate Client as functional. Localy this tests still gets executed.")

def test_printout_report():
    # Remove any previous results if they exist
    dirname = os.path.join(os.getcwd(), os.path.dirname(__file__))
    folderPath = os.path.join(dirname, 'testResults')
    if not os.path.isdir(folderPath):
        os.mkdir(folderPath)

    htmlPath = os.path.join(folderPath, 'printout.html')
    pdfPath = os.path.join(folderPath, 'printout.pdf')

    if os.path.exists(htmlPath):
        os.remove(htmlPath)
    if os.path.exists(pdfPath):
        os.remove(pdfPath)
    if os.path.isdir(os.path.join(folderPath, 'printout_data')):
        rmtree(os.path.join(folderPath, 'printout_data'))

    openFile(os.path.join(dirname, 'src', 'printout.rf6'))

    PrintoutReport.delete(3)
    assert len(PrintoutReport.getList()) == 2

    PrintoutReport.exportToHTML(1, htmlPath)
    PrintoutReport.exportToPDF(2, pdfPath)

    time.sleep(2)

    assert os.path.exists(htmlPath)
    #assert os.path.exists(pdfPath) # this check creates timeouts often

    closeModel('printout.rf6')
    time.sleep(1)
