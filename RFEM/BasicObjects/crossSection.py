from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertStrToListOfInt
from RFEM.enums import ObjectTypes

class CrossSection():
    def __init__(self,
                 no: int = 1,
                 name: str = 'IPE 300',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Cross Section Tag
            name (str): Name of Desired Cross Section (As Named in RFEM Database)
            material_no (int): Tag of Material assigned to Cross Section
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Cross Section
        clientObject = model.clientModel.factory.create('ns0:cross_section')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Cross Section No.
        clientObject.no = no

        # Cross Section Name
        clientObject.name = name

        # Material No.
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Cross Section to client model
        model.clientModel.service.set_cross_section(clientObject)

    @staticmethod
    def DeleteCrossSection(cross_sections_no: str = '1 2', model = Model):

        '''
        Args:
            cross_sections_no (str): Numbers of Cross Sections to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete from client model
        for cs in ConvertStrToListOfInt(cross_sections_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_CROSS_SECTION.name, cs)

    @staticmethod
    def GetCrossSection(object_index: int = 1, model = Model):

        '''
        Args:
            obejct_index (int): Cross Section Index
            model (RFEM Class, optional): Model to be edited
        '''

        # Get Section from client model
        return model.clientModel.service.get_cross_section(object_index)
