from RFEM.initModel import *

class Material():
    def __init__(self,
                 no: int = 1,
                 name: str = 'S235',
                 comment: str = ''):

        # Client model | Material
        clientObject = clientModel.factory.create('ns0:material')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Material No.
        clientObject.no = no

        # Material Name
        clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Add material to client model
        clientModel.service.set_material(clientObject)
