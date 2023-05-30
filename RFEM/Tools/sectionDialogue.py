from RFEM.initModel import Model

def CreateSectionList(name: str = "Favorites", model = Model):

    if isinstance(name, str):
        model.clientModel.service.create_my_section_list(name)
    else:
        raise ValueError("WARNING:Name of the section favorite list should be a string. Please kindly check the inputs.")

def AddSectionToMySectionList(list_name: str = "Favorites",
                             section_name: str = "IPE 300",
                             model = Model):

    if isinstance(list_name, str) and isinstance(section_name, str):
        model.clientModel.service.add_section_to_my_section_list(list_name, section_name)
    else:
        raise ValueError("WARNING:Name of the section favorite list and the section should be a string. Please kindly check the inputs.")

def DeleteSectionFromSectionList(list_name: str = "Favorites",
                                  section_name: str = "IPE 300",
                                  model = Model):

    if isinstance(list_name, str) and isinstance(section_name, str):
        model.clientModel.service.delete_section_from_my_section_list(list_name, section_name)
    else:
        raise ValueError("WARNING:Name of the section favorite list and the section should be a string. Please kindly check the inputs.")

def GetMySectionLists(model = Model):

    return model.clientModel.service.get_my_section_lists()

def DeleteSectionList(name: str = "Favorites", model = Model):

    if isinstance(name, str):
        model.clientModel.service.delete_my_section_list(name)
    else:
        raise ValueError("WARNING:Name of the section favorite list should be a string. Please kindly check the inputs.")

def CreateSectionFromRsectionFile(no: int = 1,
                                  file_path: str = "/rsection_file_path/",
                                  model = Model):

    if isinstance(no, int) and isinstance(file_path, str):
        model.clientModel.service.create_section_from_rsection_file(no, file_path)
    else:
        raise ValueError("WARNING: Type of file_path argument should be string and the type of the no argument should be integer. Please kindly check the inputs.")

def CreateSectionByName(id: int = 1,
                        material_id: str = "1",
                        name: str = 'my_section',
                        model = Model):

    if isinstance(id, int) and isinstance(material_id, int) and isinstance(name, str):
        model.clientModel.service.create_section_by_name(id, material_id, name)
    else:
        raise ValueError("WARNING: Type of id and material_id argument should be integer and the type of the name argument should be string. Please kindly check the inputs.")
