import sys
import os
import pytest
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, CheckIfMethodOrTypeExists
from RFEM.Tools.sectionDialogue import *
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material

if Model.clientModel is None:
    Model()

#TODO: US-8351
@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'create_section_favorite_list', True), reason="create_section_favorite_list not in RFEM GM yet")
def test_section_dialogue():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material()
    Section(1, "IPE 300")
    Section(2, "HEA 200")

    #Create a Section Favorite List
    CreateSectionFavoriteList("Favs_1")
    CreateSectionFavoriteList("Favs_2")

    #Add Section to Favorite List
    AddSectionToFavoriteList("Favs_1", "IPE 300")
    AddSectionToFavoriteList("Favs_1", "HEA 200")

    #Delete Section From Favorite List
    DeleteSectionFromFavoriteList("Favs_1", "HEA 200")

    #Get Section Favorite List
    GetSectionFavoriteLists()

    #Delete Section Favorite List
    DeleteSectionFavoriteList("Favs_2")
    DeleteSectionFavoriteList("Favs_1")

    #Create Section from Rsection File
    CreateSectionFromRsectionFile(3, os.path.dirname(__file__)+'\\src\\rsection_test.rsc')

    Model.clientModel.service.finish_modification()
