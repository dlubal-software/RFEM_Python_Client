from RFEM.initModel import *
from RFEM.enums import *
from enum import Enum

class FreeConcentratedLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 load_projection = LoadProjectionType.LOAD_PROJECTON_XY,
                 load_direction = FreeConcentratedLoadLoadDirection.LOAD_DIRECTION_GLOBAL_Z, #I might have to create my own class
                 magnitude: float = 0.0,
                 load_location_x: float = 0.0,
                 load_location_y: float = 0.0,
                 comment: str = '',
                 params: dict = {}):
        '''
        Bug: There is something wrong with the load direction type.
        ToDo: Add Load Type. It can be a force or a moment.
        '''
        # Client model | Free Concentrated Load
        clientObject = clientModel.factory.create('ns0:free_concentrated_load') # Ich bin mir nicht sicher, ob free_concentrated_load wirklich richtig ist.

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        clientObject.no = no
        clientObject.load_case = load_case_no
        clientObject.load_projection = load_projection
        clientObject.load_direction = load_direction
        clientObject.magnitude = magnitude
        clientObject.load_location_x = load_location_x
        clientObject.load_location_y = load_location_y
        clientObject.comment = comment
        # Test
        print(clientObject.no)
        print(clientObject.load_case)
        print(clientObject.load_projection)
        print(clientObject.load_direction)
        print(clientObject.magnitude)
        print(clientObject.load_location_x)
        print(clientObject.load_location_y)
        print(clientObject.comment)
        
        
        # End Test
        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]
        clientModel.service.set_free_concentrated_load(load_case_no, clientObject)
