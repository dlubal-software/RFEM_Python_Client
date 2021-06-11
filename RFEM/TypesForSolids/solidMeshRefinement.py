from RFEM.initModel import *
from RFEM.enums import SetType

class SolidMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 comment: str = ''):

        # Client model | Solid Mesh Refinement
        clientObject = clientModel.factory.create('ns0:solid_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Solid Mesh Refinement No.
        clientObject.no = no

        # Add Solid Mesh Refinement to client model
        clientModel.service.set_solid_mesh_refinement(clientObject)