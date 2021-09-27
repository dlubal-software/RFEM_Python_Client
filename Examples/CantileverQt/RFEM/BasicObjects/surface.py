from RFEM.initModel import *

class Surface():
    def __init__(self,
                 no: int = 1,
                 boundary_lines_no: str = '1 2 3 4 1',
                 thickness_no: int = 1,
                 comment: str = ''):

        # Client model | Surface
        clientObject = clientModel.factory.create('ns0:surface')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface No.
        clientObject.no = no

        # Lines No. (e.g. "5 7 8 12 5")
        clientObject.boundary_lines = boundary_lines_no

        # Comment
        clientObject.comment = comment

        # Add Surface to client model
        clientModel.service.set_surface(clientObject)
