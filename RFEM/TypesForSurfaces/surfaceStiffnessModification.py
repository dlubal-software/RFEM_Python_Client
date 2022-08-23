from RFEM.initModel import Model, clearAtributes
from RFEM.enums import SurfaceStiffnessModificationType

class SurfaceStiffnessModification():
    def __init__(self,
                 no: int = 1,
                 type = SurfaceStiffnessModificationType.TYPE_TOTAL_STIFFNESS_FACTOR,
                 factors: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Surface Stiffeness Modification

        Args:
            no (int): Surface Stiffness Modification Tag
            type (enum): Surface Stiffness Modification Type Enumeration
            factors (list): Stiffeness Modification Factors
                for type == SurfaceStiffnessModificationType.TYPE_TOTAL_STIFFNESS_FACTOR:
                    factors = [factor_of_total_stiffness]
                for type == SurfaceStiffnessModificationType.TYPE_PARTIAL_STIFFNESSES_FACTORS:
                    factors = [factor_of_bending_stiffness, factor_of_shear_stiffness, factor_of_membrane_stiffness, factor_of_eccentric_effects, and factor_of_weight]
                for type == SurfaceStiffnessModificationType.TYPE_STIFFNESS_MATRIX_ELEMENTS_FACTORS:
                    factors = list of all 21 factors from kd11 to kd38
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Stifness Modification
        clientObject = model.clientModel.factory.create('ns0:surface_stiffness_modification')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Stifness Modification No.
        clientObject.no = no

        # Modification Type
        clientObject.type = type.name

        # Stiffeness factors
        if type == SurfaceStiffnessModificationType.TYPE_TOTAL_STIFFNESS_FACTOR:
            clientObject.factor_of_total_stiffness = factors[0]
        elif type == SurfaceStiffnessModificationType.TYPE_PARTIAL_STIFFNESSES_FACTORS:
            clientObject.factor_of_bending_stiffness = factors[0]
            clientObject.factor_of_shear_stiffness = factors[1]
            clientObject.factor_of_membrane_stiffness = factors[2]
            clientObject.factor_of_eccentric_effects = factors[3]
            clientObject.factor_of_weight = factors[4]
        elif type == SurfaceStiffnessModificationType.TYPE_STIFFNESS_MATRIX_ELEMENTS_FACTORS:
            if len(factors) == 1:
                clientObject.kd11 = factors[0]
                clientObject.kd12 = factors[0]
                clientObject.kd13 = factors[0]
                clientObject.kd22 = factors[0]
                clientObject.kd23 = factors[0]
                clientObject.kd33 = factors[0]
                clientObject.kd44 = factors[0]
                clientObject.kd45 = factors[0]
                clientObject.kd55 = factors[0]
                clientObject.kd66 = factors[0]
                clientObject.kd67 = factors[0]
                clientObject.kd68 = factors[0]
                clientObject.kd77 = factors[0]
                clientObject.kd78 = factors[0]
                clientObject.kd88 = factors[0]
                clientObject.kd16 = factors[0]
                clientObject.kd17 = factors[0]
                clientObject.kd18 = factors[0]
                clientObject.kd27 = factors[0]
                clientObject.kd28 = factors[0]
                clientObject.kd38 = factors[0]
            elif len(factors) == 21:
                clientObject.kd11 = factors[0]
                clientObject.kd12 = factors[1]
                clientObject.kd13 = factors[2]
                clientObject.kd22 = factors[3]
                clientObject.kd23 = factors[4]
                clientObject.kd33 = factors[5]
                clientObject.kd44 = factors[6]
                clientObject.kd45 = factors[7]
                clientObject.kd55 = factors[8]
                clientObject.kd66 = factors[9]
                clientObject.kd67 = factors[10]
                clientObject.kd68 = factors[11]
                clientObject.kd77 = factors[12]
                clientObject.kd78 = factors[13]
                clientObject.kd88 = factors[14]
                clientObject.kd16 = factors[15]
                clientObject.kd17 = factors[16]
                clientObject.kd18 = factors[17]
                clientObject.kd27 = factors[18]
                clientObject.kd28 = factors[19]
                clientObject.kd38 = factors[20]
            else:
                raise IndexError('Size of "factors" can by either 1 or 21.')

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Stifness Modification to client model
        model.clientModel.service.set_surface_stiffness_modification(clientObject)
