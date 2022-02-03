from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import SetType

class SolidSet():
    def __init__(self,
                 no: int = 1,
                 solids_no: str = '1 2',
                 solid_set_type = SetType.SET_TYPE_GROUP,
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Solid Set Tag
            solids_no (str): Tags of Solids Contained Within Solid Set
            solid_set_type (enum): Solid Set Type Enumeration
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Solid Set
        clientObject = Model.clientModel.factory.create('ns0:solid_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Set No.
        clientObject.no = no

        # Solids number
        clientObject.solids = ConvertToDlString(solids_no)

        # Solid Set Type
        clientObject.set_type = solid_set_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Set to client model
        Model.clientModel.service.set_solid_set(clientObject)

    def ContinuousSolids(self,
                 no: int = 1,
                 solids_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Solid Set Tag
            solids_no (str): Tags of Solids Contained Within Continuous Solid Set
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Solid Set
        clientObject = Model.clientModel.factory.create('ns0:solid_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Set No.
        clientObject.no = no

        # Solids number
        clientObject.solids = ConvertToDlString(solids_no)

        # Solid Set Type
        clientObject.set_type = SetType.SET_TYPE_CONTINUOUS.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Set to client model
        Model.clientModel.service.set_solid_set(clientObject)

    def GroupOfSolids(self,
                 no: int = 1,
                 solids_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Solid Set Tag
            solids_no (str): Tags of Solids Contained Within Group of Solids Solid Set
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Solid Set
        clientObject = Model.clientModel.factory.create('ns0:solid_set')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Set No.
        clientObject.no = no

        # Solids number
        clientObject.solids = ConvertToDlString(solids_no)

        # Solid Set Type
        clientObject.set_type = SetType.SET_TYPE_GROUP.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Solid Set to client model
        Model.clientModel.service.set_solid_set(clientObject)
