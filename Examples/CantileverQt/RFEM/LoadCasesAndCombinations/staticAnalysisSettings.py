from RFEM.initModel import *
from RFEM.enums import StaticAnalysisType

class StaticAnalysisSettings():
    def __init__(self,
                 no: int = 1,
                 name: str = 'Geometric linear analysis',
                 analysis_type = StaticAnalysisType.GEOMETRICALLY_LINEAR,
                 comment: str = ''):

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:static_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Static Analysis Settings No.
        clientObject.no = no

        # Name
        clientObject.name = name

        # Analysis Type
        clientObject.analysis_type = analysis_type.name

        # Comment
        clientObject.comment = comment

        # Add Static Analysis Settings to client model
        clientModel.service.set_static_analysis_settings(clientObject)
