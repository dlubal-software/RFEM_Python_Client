from RFEM.initModel import *
from RFEM.enums import SetType

class StabilityAnalysisSettings():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Stability Analysis Settings
        clientObject = clientModel.factory.create('ns0:stability_analysis_settings')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Stability Analysis Settings No.
        clientObject.no = no

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Stability Analysis Settings to client model
        clientModel.service.set_stability_analysis_settings(clientObject)