from RFEM.initModel import *
from RFEM.enums import *
from enum import Enum

class SectionDialogue():

    def __init__(self):
        pass

    def CreateSectionFavoriteList(self,
                                  name: str = "Favorites"):

        if type(name) == str:
            clientModel.service.create_section_favorite_list(name)            
        else:
            print("WARNING:Name of the section favorite list should be a string. Please kindly check the inputs.")

    def AddSectionToFavoriteList(self,
                                 list_name: str = "Favorites",
                                 section_name: str = "IPE 300"):

        if type(list_name) == str and type(section_name) == str:
            return clientModel.service.add_section_to_favorite_list(list_name, section_name)
        else:
            print("WARNING:Name of the section favorite list and the section should be a string. Please kindly check the inputs.")

    def DeleteSectionFromFavoriteList(self,
                                     list_name: str = "Favorites",
                                     section_name: str = "IPE 300"):

        if type(list_name) == str and type(section_name) == str:
            return clientModel.service.delete_section_from_favorite_list(list_name, section_name)
        else:
            print("WARNING:Name of the section favorite list and the section should be a string. Please kindly check the inputs.")

    def GetSectionFromFavoriteLists(self):

        return clientModel.service.get_section_favorite_lists()

    def DeleteSectionFavoriteList(self,
                                  name: str = "Favorites"):

        if type(name) == str:
            return clientModel.service.delete_section_favorite_list(name)
        else:
            print("WARNING:Name of the section favorite list should be a string. Please kindly check the inputs.")

    def CreateSectionFromRsectionFile(self,
                                      no: int = 1, 
                                      file_path: str = "/rsection_file_path/"):
        
        if type(no) == int and type(file_path) == str:
            return clientModel.service.create_section_from_rsection_file(no, file_path)
        else:
            print("WARNING:Type of file_path argument should be string and the type of the no argument should be integer. Please kindly check the inputs.")
