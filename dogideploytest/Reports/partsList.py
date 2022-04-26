
from RFEM.initModel import Model

def GetPartsListAllByMaterial(model = Model):
    '''
    Returns Parts List All By Material
    '''
    try:
        return model.clientModel.service.get_parts_list_all_by_material()
    except:
        model.clientModel.service.generate_parts_lists()
        return model.clientModel.service.get_parts_list_all_by_material()

def GetPartsListMemberRepresentativesByMaterial(model = Model):
    '''
    Returns Parts List Member Representatives By Material
    '''
    try:
        return model.clientModel.service.get_parts_list_member_representatives_by_material()
    except:
        model.clientModel.service.generate_parts_lists()
        return model.clientModel.service.get_parts_list_member_representatives_by_material()

def GetPartsListMemberSetsByMaterial(model = Model):
    '''
    Returns Parts List Member Sets By Material
    '''
    try:
        return model.clientModel.service.get_parts_list_member_sets_by_material()
    except:
        model.clientModel.service.generate_parts_lists()
        return model.clientModel.service.get_parts_list_member_sets_by_material()

def GetPartsListMembersByMaterial(model = Model):
    '''
    Returns Parts List Members By Material
    '''
    try:
        return model.clientModel.service.get_parts_list_members_by_material()
    except:
        model.clientModel.service.generate_parts_lists()
        return model.clientModel.service.get_parts_list_members_by_material()

def GetPartsListSolidsByMaterial(model = Model):
    '''
    Returns Parts List Solids By Material
    '''
    try:
        return model.clientModel.service.get_parts_list_solids_by_material()
    except:
        model.clientModel.service.generate_parts_lists()
        return model.clientModel.service.get_parts_list_solids_by_material()

def GetPartsListSurfacessByMaterial(model = Model):
    '''
    Returns Parts List Surfaces By Material
    '''
    try:
        return model.clientModel.service.get_parts_list_surfaces_by_material()
    except:
        model.clientModel.service.generate_parts_lists()
        return model.clientModel.service.get_parts_list_surfaces_by_material()
