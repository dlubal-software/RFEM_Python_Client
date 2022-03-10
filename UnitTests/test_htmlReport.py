import sys
import os
from os import path, getcwd
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Reports.html import ExportResultTablesToHtml
from RFEM.initModel import Model
from shutil import rmtree

if Model.clientModel is None:
    Model()

def test_html_report():
    Model.clientModel.service.delete_all()
    Model.clientModel.service.run_script('..\\scripts\\internal\\Demos\\Demo-003 Castellated Beam.js')
    Model.clientModel.service.calculate_all(False)

    dirname = path.join(getcwd(), path.dirname(__file__))
    rmtree(path.join(dirname, 'testResults'))
    ExportResultTablesToHtml(path.join(dirname, 'testResults'))
    os.system(f"start {path.join(dirname, 'testResults', 'index.html')}")
