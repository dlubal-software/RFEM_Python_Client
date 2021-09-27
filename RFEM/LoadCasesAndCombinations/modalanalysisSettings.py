from RFEM.initModel import *
from RFEM.enums import *

class ModalAnalysisSettings():
    def __init__(self,
                 no: int = 1,
                 name: str = 'Modal Analysis Settings',
                 solution_method = ModalSolutionMethod.METHOD_LANCZOS,
                 mass_conversion_type = ModalMassConversionType.MASS_CONVERSION_TYPE_Z_COMPONENTS_OF_LOADS,
                 mass_matrix_type = ModalMassMatrixType.MASS_MATRIX_TYPE_CONSISTENT,
                 number_of_modes_method = ModalModeNumberMethod.NUMBER_OF_MODES_METHOD_USER_DEFINED,
                 number_of_modes : int = 4,
                 acting_masses = [],
                 comment: str = '',
                 params: dict = {}):

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        clientObject.user_defined_name_enabled = True
        clientObject.name = name

        # Analysis Type
        clientObject.solution_method = solution_method.name

        # Mass Conversion Type
        

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Static Analysis Settings to client model
        clientModel.service.set_static_analysis_settings(clientObject)
