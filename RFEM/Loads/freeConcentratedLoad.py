from RFEM.initModel import *
from RFEM.enums import *
from enum import Enum

class FreeConcentratedLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 load_projection = LoadProjectionType.LOAD_PROJECTON_XY,
                 load_direction = LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, #I might have to create my own class
                 magnitude: float = 0.0,
                 load_location_y: float = 0.0,
                 load_location_x: float = 0.0,
                 comment: str = '',
                 params: dict = {}):
        pass