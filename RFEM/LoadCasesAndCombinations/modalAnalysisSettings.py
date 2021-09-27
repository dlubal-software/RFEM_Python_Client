from RFEM.initModel import *
from RFEM.enums import *

class ModalAnalysisSettings():
    def __init__(self,
                 no: int = 1,
                 name: str = 'Modal Analysis Settings',
                 solution_method = ModalSolutionMethod.METHOD_LANCZOS,
                 mass_matrix_type = ModalMassMatrixType.MASS_MATRIX_TYPE_DIAGONAL,
                 mass_conversion_type = ModalMassConversionType.MASS_CONVERSION_TYPE_Z_COMPONENTS_OF_LOADS,
                 number_of_modes : int = 4,
                 acting_masses = [],
                 comment: str = '',
                 params: dict = {}):
        """
        Args:
            no (int, optional): 
            name (str, optional): 
            solution_method ([type], optional): 
            mass_matrix_type ([type], optional): 
            mass_conversion_type ([type], optional): 
            number_of_modes (int, optional): 
            acting_masses (list, optional): 
            comment (str, optional): 
            params (dict, optional): 
        """

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:modal_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        clientObject.user_defined_name_enabled = True
        clientObject.name = name

        # Analysis Type
        clientObject.solution_method = solution_method.name

        # Mass Matrix Type
        clientObject.mass_matrix_type = mass_matrix_type.name

        # Mass Conversion Type
        clientObject.mass_conversion_type = mass_conversion_type.name

        # Number of Modes
        clientObject.number_of_modes_method = "NUMBER_OF_MODES_METHOD_USER_DEFINED"
        clientObject.number_of_modes = number_of_modes

        # Acting Masses Directions
        clientObject.acting_masses_about_axis_x_enabled = acting_masses[0]
        clientObject.acting_masses_about_axis_y_enabled = acting_masses[1]
        clientObject.acting_masses_about_axis_z_enabled = acting_masses[2]
        clientObject.acting_masses_in_direction_x_enabled = acting_masses[3]
        clientObject.acting_masses_in_direction_y_enabled = acting_masses[4]
        clientObject.acting_masses_in_direction_z_enabled = acting_masses[5]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        clientModel.service.set_modal_analysis_settings(clientObject)
