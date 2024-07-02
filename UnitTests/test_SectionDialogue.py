import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model
from RFEM.connectionGlobals import url
from RFEM.Tools.sectionDialogue import *
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
import pytest

if Model.clientModel is None:
    Model()


@pytest.mark.skipif(url != 'http://127.0.0.1', reason="This test fails on remote PC due to incorrect file path. \
                    Althought it is easy to change, it would not be easy to update on every remote computer.\
                    It is not necessary to evaluate Client as functional. Localy this tests still gets executed.")

def test_section_dialogue():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material()
    Section(1, "IPE 300")
    Section(2, "HEA 200")

    #Create a Section Favorite List
    CreateSectionList("Favs_1")
    CreateSectionList("Favs_2")

    #Add Section to Favorite List
    AddSectionToMySectionList("Favs_1", "IPE 300")
    AddSectionToMySectionList("Favs_1", "HEA 200")

    #Delete Section From Favorite List
    DeleteSectionFromSectionList("Favs_1", "HEA 200")

    #Get Section Favorite List
    GetMySectionLists()

    #Delete Section Favorite List
    DeleteSectionList("Favs_2")
    DeleteSectionList("Favs_1")

    #Create Section from Rsection File
    CreateSectionFromRsectionFile(3, os.path.dirname(__file__)+'\\src\\rsection_test.rsc')

    Model.clientModel.service.finish_modification()
