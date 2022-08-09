from RFEM.initModel import Model, clearAtributes
from RFEM.enums import SurfaceContactPerpendicularType, SurfaceContactParallelType, SurfaceContactFrictionType

class SurfaceContactType():
    def __init__(self,
                 no: int = 1,
                 perpendicular_contact = SurfaceContactPerpendicularType.FAILURE_UNDER_TENSION,
                 parallel_contact = SurfaceContactParallelType.FULL_FORCE_TRANSMISSION,
                 contact_parameters = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Surface Contact Type

        Args:
            no (int): Surface Contact Type Tag
            perpendicular_contact (enum): Surface Contact Perpendicular Type Enumeration
            parallel_contact (enum): Surface Contact Parallel Type Enumeration
            contact_parameters (list): Contact Parameters List
                for parallel_contact == SurfaceContactParallelType.RIGID_FRICTION:
                    contact_parameters = [enum rigid_friction_type, rigid_friction_coefficient or rigid_friction_limit_stress]
                for parallel_contact == SurfaceContactParallelType.ELASTIC_FRICTION:
                    contact_parameters = [elastic_friction_shear_stiffness, enum elastic_friction_type, elastic_friction_coefficient or elastic_friction_limit_stress]
                for parallel_contact == SurfaceContactParallelType.ELASTIC_SURFACE:
                    contact_parameters = [elastic_behavior_shear_stiffness]
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited

        Raises:
            ValueError: There are no paramters for given parallel contact.
        """

        # Client model | Surface Contact
        clientObject = model.clientModel.factory.create('ns0:surfaces_contact_type')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Contact No.
        clientObject.no = no

        # Contact Perpendicular to Surface
        clientObject.perpendicular_to_surface = perpendicular_contact.name

        # Contact Paralle to Surface
        clientObject.parallel_to_surface = parallel_contact.name

        # Contact Parameters
        if parallel_contact == SurfaceContactParallelType.RIGID_FRICTION:
            clientObject.rigid_friction_type = contact_parameters[0].name
            if contact_parameters[0] == SurfaceContactFrictionType.FRICTION_COEFFICIENT:
                clientObject.rigid_friction_coefficient = contact_parameters[1]
            elif contact_parameters[0] == SurfaceContactFrictionType.LIMIT_STRESS:
                clientObject.rigid_friction_limit_stress = contact_parameters[1]

        elif parallel_contact == SurfaceContactParallelType.ELASTIC_FRICTION:
            clientObject.elastic_friction_shear_stiffness = contact_parameters[0]
            clientObject.elastic_friction_type = contact_parameters[1].name
            if contact_parameters[1] == SurfaceContactFrictionType.FRICTION_COEFFICIENT:
                clientObject.elastic_friction_coefficient = contact_parameters[2]
            elif contact_parameters[1] == SurfaceContactFrictionType.LIMIT_STRESS:
                clientObject.elastic_friction_limit_stress = contact_parameters[2]

        elif parallel_contact == SurfaceContactParallelType.ELASTIC_SURFACE:
            clientObject.elastic_behavior_shear_stiffness = contact_parameters[0]

        elif contact_parameters:
            raise ValueError(f'There are no parameters for contact {parallel_contact.name}')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Contact to client model
        model.clientModel.service.set_surfaces_contact_type(clientObject)

    @staticmethod
    def FullForce(
                 no: int = 1,
                 perpendicular_contact = SurfaceContactPerpendicularType.FAILURE_UNDER_TENSION,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Full Force Transmission Surface Contact Type

        Args:
            no (int): Surface Contact Type Tag
            perpendicular_contact (enum): Surface Contact Perpendicular Type Enumeration
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Contact
        clientObject = model.clientModel.factory.create('ns0:surfaces_contact_type')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Contact No.
        clientObject.no = no

        # Contact Perpendicular to Surface
        clientObject.perpendicular_to_surface = perpendicular_contact.name

        # Contact Paralle to Surface
        clientObject.parallel_to_surface = SurfaceContactParallelType.FULL_FORCE_TRANSMISSION.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Contact to client model
        model.clientModel.service.set_surfaces_contact_type(clientObject)

    @staticmethod
    def RigidFriction(
                      no: int = 1,
                      perpendicular_contact = SurfaceContactPerpendicularType.FAILURE_UNDER_TENSION,
                      rigid_friction_type = SurfaceContactFrictionType.FRICTION_COEFFICIENT,
                      rigid_friction_value: float = 0.25,
                      comment: str = '',
                      params: dict = None,
                      model = Model):
        """
        Rigid Friction Surface Contact Type

        Args:
            no (int): Surface Contact Type Tag
            perpendicular_contact (enum): Surface Contact Perpendicular Type Enumeration
            rigid_friction_type (enum): Surface Contact Friction Type Enumeration
            rigid_friction_value (float): Value of rigid_friction_coefficient or rigid_friction_limit_stress
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Contact
        clientObject = model.clientModel.factory.create('ns0:surfaces_contact_type')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Contact No.
        clientObject.no = no

        # Contact Perpendicular to Surface
        clientObject.perpendicular_to_surface = perpendicular_contact.name

        # Contact Paralle to Surface
        clientObject.parallel_to_surface = SurfaceContactParallelType.RIGID_FRICTION.name

        # Rigid Friction Type
        clientObject.rigid_friction_type = rigid_friction_type.name

        # Rigid Friction Type Value
        if rigid_friction_type == SurfaceContactFrictionType.FRICTION_COEFFICIENT:
            clientObject.rigid_friction_coefficient = rigid_friction_value
        elif rigid_friction_type == SurfaceContactFrictionType.LIMIT_STRESS:
            clientObject.rigid_friction_limit_stress = rigid_friction_value

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Contact to client model
        model.clientModel.service.set_surfaces_contact_type(clientObject)

    @staticmethod
    def ElasticFriction(
                      no: int = 1,
                      perpendicular_contact = SurfaceContactPerpendicularType.FAILURE_UNDER_TENSION,
                      shear_stiffness: float = 2000,
                      elastic_friction_type = SurfaceContactFrictionType.FRICTION_COEFFICIENT,
                      elastic_friction_value: float = 0.25,
                      comment: str = '',
                      params: dict = None,
                      model = Model):
        """
        Elastic Friction Surface Contact Type

        Args:
            no (int): Surface Contact Type Tag
            perpendicular_contact (enum): Surface Contact Perpendicular Type Enumeration
            shear_stiffness (float): Shear Stiffness
            elastic_friction_type (enum): Surface Contact Friction Type Enumeration
            elastic_friction_value (float): Value of elastic_friction_coefficient or elastic_friction_limit_stress
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Contact
        clientObject = model.clientModel.factory.create('ns0:surfaces_contact_type')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Contact No.
        clientObject.no = no

        # Contact Perpendicular to Surface
        clientObject.perpendicular_to_surface = perpendicular_contact.name

        # Contact Paralle to Surface
        clientObject.parallel_to_surface = SurfaceContactParallelType.ELASTIC_FRICTION.name

        # Elastic Friction Type
        clientObject.rigid_friction_type = elastic_friction_type.name

        # Elastic Friction Type Values
        clientObject.elastic_friction_shear_stiffness = shear_stiffness

        clientObject.elastic_friction_type = elastic_friction_type.name
        if elastic_friction_type == SurfaceContactFrictionType.FRICTION_COEFFICIENT:
            clientObject.elastic_friction_coefficient = elastic_friction_value
        elif elastic_friction_type == SurfaceContactFrictionType.LIMIT_STRESS:
            clientObject.elastic_friction_limit_stress = elastic_friction_value

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Contact to client model
        model.clientModel.service.set_surfaces_contact_type(clientObject)

    @staticmethod
    def ElasticSurface(
                      no: int = 1,
                      perpendicular_contact = SurfaceContactPerpendicularType.FAILURE_UNDER_TENSION,
                      shear_stiffness: float = 2500,
                      comment: str = '',
                      params: dict = None,
                      model = Model):
        """
        Elastic Friction Surface Contact Type

        Args:
            no (int): Surface Contact Type Tag
            perpendicular_contact (enum): Surface Contact Perpendicular Type Enumeration
            shear_stiffness (float): Shear Stiffness Value
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Contact
        clientObject = model.clientModel.factory.create('ns0:surfaces_contact_type')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Contact No.
        clientObject.no = no

        # Contact Perpendicular to Surface
        clientObject.perpendicular_to_surface = perpendicular_contact.name

        # Contact Paralle to Surface
        clientObject.parallel_to_surface = SurfaceContactParallelType.ELASTIC_SURFACE.name

        # Elastic Surface Shear Stiffness
        clientObject.elastic_behavior_shear_stiffness = shear_stiffness

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Contact to client model
        model.clientModel.service.set_surfaces_contact_type(clientObject)
