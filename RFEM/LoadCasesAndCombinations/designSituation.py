from RFEM.initModel import *
from RFEM.enums import SetType

class DesignSituation():
    def __init__(self,
                 no: int = 1,
                 user_defined_name: bool = False,
                 name = None,
                 active: bool = True,
                 design_situation_type: int = 6122,
                 comment: str = '',
                 params: dict = {}):
        
        """
        Args:
            no (int): Design Situation Tag
            user_defined_name (bool): Possibility for a user-defined name
            name (str, optional): User-defined name. Only applicable for user_defined_name boolean as TRUE
            active (bool): Status of the design situation for the solver
            design_situation_type (int): Numeric codes representing intended design situation type
            comment (str, optional): Comments
            params (dict, optional): Parameters

        design_situation_type:
            6122 : ULS (EQU) - Permanent and transient,
            6993 : ULS (EQU) - Accidental - psi-1,1,
            6994 : ULS (EQU) - Accidental - psi-2,1,
            6995 : ULS (EQU) - Accidental - Snow - psi-1,1,
            6996 : ULS (EQU) - Accidental - Snow - psi-2,1,
            6997 : ULS (EQU) - Seismic,
            7007 : ULS (STR/GEO) - Permanent and transient - Eq. 6.10,
            7010 : ULS (STR/GEO) - Accidental - psi-1,1,
            7011 : ULS (STR/GEO) - Accidental - psi-2,1,
            7012 : ULS (STR/GEO) - Accidental - Snow - psi-1,1,
            7013 : ULS (STR/GEO) - Accidental - Snow - psi-2,1,
            7014 : ULS (STR/GEO) - Seismic,
            6193 : SLS - Characteristic,
            6194 : SLS - Frequent,
            6195 : SLS - Quasi-permanent
        """

        # Client model | Design Situation
        clientObject = clientModel.factory.create('ns0:design_situation')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Design Situation No.
        clientObject.no = no

        # Design Situation Name
        clientObject.user_defined_name_enabled = user_defined_name
        if user_defined_name == True:
            if name == None:
                raise Exception('WARNING: A user defined design situation name was requested. As such, the name parameter cannot be empty.')
            clientObject.name = name

        # Design Situation Active
        clientObject.active = active
        
        # Design Situation Type
        clientObject.design_situation_type = design_situation_type

        # Design Situation Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Design Situation to client model
        clientModel.service.set_design_situation(clientObject)