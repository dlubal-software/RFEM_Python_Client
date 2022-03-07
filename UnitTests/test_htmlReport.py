import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Reports.html import ExportResultTablesToHtml
from RFEM.initModel import Model

if Model.clientModel is None:
    Model()

def test_html_report():
    Model.clientModel.service.delete_all()
    # Model.clientModel.service.run_script('..\\scripts\\internal\\Demos\\Demo-006 Castellated Beam.js')
    Model.clientModel.service.run_script('..\\scripts\\internal\\Demos\\Demo-001 Hall.js')
    Model.clientModel.service.calculate_all(False)

    ExportResultTablesToHtml('d:\\Sources\\results')