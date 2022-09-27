from RFEM.initModel import Model, clearAttributes

class SurfaceEccentricity():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Surface Eccentricity
        clientObject = Model.clientModel.factory.create('ns0:surface_eccentricity')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Eccentricity No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface Eccentricity to client model
        Model.clientModel.service.set_surface_eccentricity(clientObject)
