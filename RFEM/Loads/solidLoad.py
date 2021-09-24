from RFEM.initModel import *
from RFEM.enums import *

class SolidLoad():

    def __init__(self,
                 no: int =1,
                 load_case_no: int = 1,
                 solids_no: str= '1',
                 load_type = SolidLoadType.LOAD_TYPE_FORCE,
                 load_distribution = SolidLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = SolidLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,
                 magnitude: float = 0,
                 comment: str = '',
                 params: dict = {}):
        pass

    def Force():
        # Siehe lineLoad.Force()
        pass

    def Temperature():
        # Siehe memberLoad.Temperature()
        pass

    def Strain():
        pass

    def Motion():
        pass

    def Buoyancy():
        pass

    def Gass():
        pass