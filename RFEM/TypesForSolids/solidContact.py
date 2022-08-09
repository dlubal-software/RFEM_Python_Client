from RFEM.initModel import Model, clearAtributes
from RFEM.enums import SolidContactPerpendicularType, SolidContactParallelType

class SolidContact():
    def __init__(self,
                 no: int = 1,
                 perpendicular_contact = SolidContactPerpendicularType.FAILURE_UNDER_TENSION,
                 parallel_contact = SolidContactParallelType.FULL_FORCE_TRANSMISSION,
                 contact_parameters: list = None,
                 solids: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Solid Contact

        Args:
            no (int): Solid Contact Tag
            perpendicular_contact (enum): Solid Contact Perpendicular Type Enumeration
            parallel_contact (enum): Solid Contact Parallel Type Enumeration
            contact_parameters (list): Contact Parameters List
                for parallel_contact == SolidContactParallelType.RIGID_FRICTION:
                    contact_parameters = [friction_coefficient]
                for parallel_contact == SolidContactParallelType.RIGID_FRICTION_LIMIT:
                    contact_parameters = [limit_stress]
                for parallel_contact == SolidContactParallelType.ELASTIC_FRICTION:
                    contact_parameters = [shear_stiffness, friction_coefficient]
                for parallel_contact == SolidContactParallelType.ELASTIC_FRICTION_LIMIT:
                    contact_parameters = [shear_stiffness, limit_stress]
                for parallel_contact == SolidContactParallelType.ELASTIC_SOLID:
                    contact_parameters = [shear_stiffness]
            solids (str): Assigned to Solids
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited

        Raises:
            ValueError: There are no parameters for given parallel contact.
        """

        # Client model | Solid Contact
        clientObject = model.clientModel.factory.create('ns0:solid_contacts')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Contact No.
        clientObject.no = no

        # Contact Perpendicular to Surface
        clientObject.perpendicular_to_surface = perpendicular_contact.name

        # Contact Paralle to Surface
        clientObject.parallel_to_surface = parallel_contact.name

        # Contact Parameters
        if parallel_contact == SolidContactParallelType.RIGID_FRICTION:
            clientObject.friction_coefficient = contact_parameters[0]
        elif parallel_contact == SolidContactParallelType.RIGID_FRICTION_LIMIT:
            clientObject.limit_stress = contact_parameters[0]
        elif parallel_contact == SolidContactParallelType.ELASTIC_FRICTION:
            clientObject.shear_stiffness = contact_parameters[0]
            clientObject.friction_coefficient = contact_parameters[1]
        elif parallel_contact == SolidContactParallelType.ELASTIC_FRICTION_LIMIT:
            clientObject.shear_stiffness = contact_parameters[0]
            clientObject.limit_stress = contact_parameters[1]
        elif parallel_contact == SolidContactParallelType.ELASTIC_SOLID:
            clientObject.shear_stiffness = contact_parameters[0]
        elif contact_parameters:
            raise ValueError(f'There are no parameters for contact {parallel_contact.name}')

        # Assigned to Solids
        clientObject.solids = solids

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Solid Contact to client model
        model.clientModel.service.set_solid_contacts(clientObject)
