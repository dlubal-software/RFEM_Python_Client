from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import ModalSolutionMethod, ModalMassConversionType, ModalMassMatrixType, ModalNeglectMasses

class ModalAnalysisSettings():

    def __init__(self,
                 no: int = 1,
                 name: str = 'Modal Analysis Settings',
                 solution_method = ModalSolutionMethod.METHOD_LANCZOS,
                 mass_conversion_type = ModalMassConversionType.MASS_CONVERSION_TYPE_Z_COMPONENTS_OF_LOADS,
                 mass_matrix_type = ModalMassMatrixType.MASS_MATRIX_TYPE_CONSISTENT,
                 number_of_modes : int = 4,
                 acting_masses: list = None,
                 neglect_masses = ModalNeglectMasses.E_NEGLECT_MASSES_NO_NEGLECTION,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Setting Tag
            name (str): Setting Name
            solution_method (enum): Modal Solution Method Enumeration
            mass_conversion_type (enum): Modal Mass Conversion Type Enumeration
            mass_matrix_type (enum): Modal Mass Matrix Type Enumeration
            number_of_modes (int): Number of Modes
            acting_masses (list): Acting Masses Directions List
            neglect_masses (enum): Modal Neglect Masses Enumeration
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """
        # Client model | Surface
        clientObject = model.clientModel.factory.create('ns0:modal_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Analysis Type
        clientObject.solution_method = solution_method.name

        # Mass Conversion Type
        clientObject.mass_conversion_type = mass_conversion_type.name

        # Mass Matrix Type
        clientObject.mass_matrix_type = mass_matrix_type.name

        # Number of Modes
        clientObject.number_of_modes_method = "NUMBER_OF_MODES_METHOD_USER_DEFINED"
        clientObject.number_of_modes = number_of_modes

        # Acting Masses
        if len(acting_masses) == 6:
            clientObject.acting_masses_about_axis_x_enabled = acting_masses[0]
            clientObject.acting_masses_about_axis_y_enabled = acting_masses[1]
            clientObject.acting_masses_about_axis_z_enabled = acting_masses[2]
            clientObject.acting_masses_in_direction_x_enabled = acting_masses[3]
            clientObject.acting_masses_in_direction_y_enabled = acting_masses[4]
            clientObject.acting_masses_in_direction_z_enabled = acting_masses[5]
        else:
            raise ValueError('WARNING: The acting masses array needs to be of length 6. Kindly check list inputs for completeness and correctness.')

        # Neglect Masses
        clientObject.neglect_masses = neglect_masses.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Static Analysis Settings to client model
        model.clientModel.service.set_modal_analysis_settings(clientObject)
