import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Reports.html import ExportResultTablesToHtml

#if Model.clientModel is None:
#    Model()

def test_html_report():
    ExportResultTablesToHtml('d:\\Sources\\results')