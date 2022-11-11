from RFEM.initModel import Model, clearAttributes

class SurfaceStiffnessModification():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Surface Stifness Modification
        clientObject = Model.clientModel.factory.create('ns0:surface_stiffness_modification')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Stifness Modification No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface Stifness Modification to client model
        Model.clientModel.service.set_surface_stiffness_modification(clientObject)
