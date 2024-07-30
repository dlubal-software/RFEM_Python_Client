from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString, ConvertStrToListOfInt
from RFEM.enums import TimberMoistureClassType, ObjectTypes

class TimberMoistureClass():
    def __init__(self,
                no: int = 1,
                name: str = '',
                members: str = '',
                member_sets: str = '',
                surfaces: str = '',
                surface_sets: str = '',
                moisture_class = TimberMoistureClassType.TIMBER_MOISTURE_CLASS_TYPE_1,
                comment: str = '',
                params: dict = None,
                model = Model):
        """
        Args:
            no (int): Timber Moisture Class Tag
            name (str): User Defined Moisture Class Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            surfaces (str): Assigned Surfaces
            surface_sets (str): Assigned Surface Sets
            moisture_class (enum): Timber Moisture Class Enumeration
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

         # Client Model | Types For Timber Design Moisture Class
        clientObject = model.clientModel.factory.create('ns0:timber_moisture_class')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Service Class
        clientObject.no = no

        # Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Assigned Surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Assigned Surface Sets
        clientObject.surface_sets = ConvertToDlString(surface_sets)

        # Moisture Class
        clientObject.moisture_class = moisture_class.name

        # User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Service Class to client model
        model.clientModel.service.set_timber_moisture_class(clientObject)

    @staticmethod
    def Delete(numbers: str = '1 2', model = Model):

        '''
        Args:
            numbers (str): Numbers of Timber Moisture Class to be deleted
            model (RFEM Class, optional): Model to be edited
        '''

        # Delete from client model
        for i in ConvertStrToListOfInt(numbers):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_TIMBER_MOISTURE_CLASS.name, i)

    @staticmethod
    def Get(idx: int = 1, model = Model):

        '''
        Args:
            idx (int): Timber Moisture Class Index
            model (RFEM Class, optional): Model to be edited
        '''

        # Get Timber Moisture Class from client model
        return model.clientModel.service.get_timber_moisture_class(idx)
