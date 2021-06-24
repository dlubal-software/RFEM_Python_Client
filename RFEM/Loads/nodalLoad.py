from RFEM.initModel import *
from RFEM.enums import LoadDirectionType
from enum import Enum

class NodalLoad():
    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 nodes_no: str = '1',
                 load_direction = LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,
                 magnitude: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Nodal Force
        clientObject = clientModel.factory.create('ns0:nodal_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Nodal Force No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Nodes No. (e.g. '5 6 7 12')
        clientObject.nodes = ConvertToDlString(nodes_no)

        # Force Direction
        clientObject.load_direction = load_direction.name

        # Magnitude
        clientObject.force_magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Nodal Force to client model
        clientModel.service.set_nodal_load(load_case_no, clientObject)
