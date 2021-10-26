from RFEM.initModel import *
from RFEM.enums import *
from enum import *
import math

class ConcreteReinforcementDirection():
    def __init__(self,
                no: int = 1, 
                name: str = "RD 1",
                surfaces = "1",
                reinforcement_direction_type = ReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_FIRST_REINFORCEMENT_IN_X,
                rotation_parameters = [],
                comment: str = '', 
                params: dict = {}):
        """
        Args:
            no (int): Reinforcement Direction Tag
            name (str): User Defined Name
            surfaces (str): Assigned Surfaces
            reinforcement_direction_type (enum): Reinforcement Direction Enumeration 
            rotation_parameters (list): Rotation Parameters
            comment (str, optional): Comments
            params (dict, optional): Parameters
        """

        # Client model | Concrete Durabilities
        clientObject = clientModel.factory.create('ns0:reinforcement_direction')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Concrete Durability No.
        clientObject.no = no

        # User Defined Name
        clientObject.user_defined_name_enabled = True
        clientObject.name = name

        # Reinforcement Direction Type
        clientObject.reinforcement_direction_type = reinforcement_direction_type.name

        if reinforcement_direction_type.name == "REINFORCEMENT_DIRECTION_TYPE_ROTATED":
            clientObject.first_reinforcement_angle = rotation_parameters[0] * math.pi/180
            clientObject.second_reinforcement_angle = rotation_parameters[1] * math.pi/180

        # Assigned Surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)
            
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Global Parameter to client model          
        clientModel.service.set_reinforcement_direction(clientObject)





        
        

