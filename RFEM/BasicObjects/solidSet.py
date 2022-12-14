from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import SetType

class SolidSet():
    def __init__(self,
                 no: int = 1,
                 solids_no: str = '1 2',
                 solid_set_type = SetType.SET_TYPE_GROUP,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Solid Set Tag
            solids_no (str): Numbers of Solids Contained Within Solid Set
            solid_set_type (enum): Solid Set Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Solid Set
        clientObject = model.clientModel.factory.create('ns0:solid_set')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid Set No.
        clientObject.no = no

        # Solids number
        clientObject.solids = ConvertToDlString(solids_no)

        # Solid Set Type
        clientObject.set_type = solid_set_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Solid Set to client model
        model.clientModel.service.set_solid_set(clientObject)

    @staticmethod
    def ContinuousSolids(
                 no: int = 1,
                 solids_no: str = '1 2',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Solid Set Tag
            solids_no (str): Numbers of Solids Contained Within Continuous Solid Set
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Solid Set
        clientObject = model.clientModel.factory.create('ns0:solid_set')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid Set No.
        clientObject.no = no

        # Solids number
        clientObject.solids = ConvertToDlString(solids_no)

        # Solid Set Type
        clientObject.set_type = SetType.SET_TYPE_CONTINUOUS.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Solid Set to client model
        model.clientModel.service.set_solid_set(clientObject)

    @staticmethod
    def GroupOfSolids(
                 no: int = 1,
                 solids_no: str = '1 2',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Solid Set Tag
            solids_no (str): Numbers of Solids Contained Within Group of Solids Solid Set
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Solid Set
        clientObject = model.clientModel.factory.create('ns0:solid_set')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid Set No.
        clientObject.no = no

        # Solids number
        clientObject.solids = ConvertToDlString(solids_no)

        # Solid Set Type
        clientObject.set_type = SetType.SET_TYPE_GROUP.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Solid Set to client model
        model.clientModel.service.set_solid_set(clientObject)
