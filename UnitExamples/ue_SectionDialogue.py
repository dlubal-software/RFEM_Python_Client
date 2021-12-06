import sys
sys.path.append(".")
from RFEM.BasicObjects.section import Section
from RFEM.initModel import *
from RFEM.Tools.sectionDialogue import SectionDialogue


if __name__ == '__main__':

    Model(True, "SectionDialogue")
    Model.clientModel.service.begin_modification()
          
    #Create a Section Favorite List
    SectionDialogue.CreateSectionFavoriteList(0, "Favs_1")
    SectionDialogue.CreateSectionFavoriteList(0, "Favs_2")

    #Add Section to Favorite List
    SectionDialogue.AddSectionToFavoriteList(0, "Favs_1", "IPE 300")
    SectionDialogue.AddSectionToFavoriteList(0, "Favs_1", "HEA 200")

    #Delete Section From Favorite List
    SectionDialogue.DeleteSectionFromFavoriteList(0, "Favs_1", "HEA 200")

    #Get Section Favorite List
    fav_list = SectionDialogue.GetSectionFavoriteLists(0)
    print(fav_list)

    #Delete Section Favorite List
    SectionDialogue.DeleteSectionFavoriteList(0, "Favs_2")

    #Create Section from Rsection File
    SectionDialogue.CreateSectionFromRsectionFile(0, 3, 'UnitTests\\src\\rsection_test.rsc')
    
    Model.clientModel.service.finish_modification()