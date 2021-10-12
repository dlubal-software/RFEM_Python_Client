from RFEM.initModel import *
from RFEM.enums import ModelType

class ModelType():

    def __init__(model_type = ModelType.E_MODEL_TYPE_3D):

        # Client model | Model Type
        clientObject = clientModel.factory.create('ns0:model_type')

        # Clears object attributes | Sets all attributes to None
        clearAtributes(clientObject)

        # Model Type
        clientObject.model_type = model_type.name
        
        # Add Global Parameter to client model          
        clientModel.service.set_model_type(clientObject)