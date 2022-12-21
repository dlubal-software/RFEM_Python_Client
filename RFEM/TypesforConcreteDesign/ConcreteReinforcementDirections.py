from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import ReinforcementDirectionType
from math import pi

class ConcreteReinforcementDirection():
    def __init__(self,
                no: int = 1,
                name: str = "RD 1",
                surfaces: str = "1",
                reinforcement_direction_type = ReinforcementDirectionType.REINFORCEMENT_DIRECTION_TYPE_FIRST_REINFORCEMENT_IN_X,
                rotation_parameters: list = None,
                comment: str = '',
                params: dict = None,
                model = Model):
        """
        Args:
            no (int): Concrete Reinforcement Direction Tag
            name (str): User Defined Name
            surfaces (str): Assigned Surfaces
            reinforcement_direction_type (enum): Reinforcement Direction Enumeration
            rotation_parameters (list): Rotation Parameters List
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Concrete Durabilities
        clientObject = model.clientModel.factory.create('ns0:reinforcement_direction')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Concrete Durability No.
        clientObject.no = no

        # User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Reinforcement Direction Type
        clientObject.reinforcement_direction_type = reinforcement_direction_type.name

        if reinforcement_direction_type.name == "REINFORCEMENT_DIRECTION_TYPE_ROTATED":
            clientObject.first_reinforcement_angle = rotation_parameters[0] * pi/180
            clientObject.second_reinforcement_angle = rotation_parameters[1] * pi/180

        # Assigned Surfaces
        clientObject.surfaces = ConvertToDlString(surfaces)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Global Parameter to client model
        model.clientModel.service.set_reinforcement_direction(clientObject)
