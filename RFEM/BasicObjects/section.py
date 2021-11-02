from RFEM.initModel import *

class Section():
    def __init__(self,
                 no: int = 1,
                 name: str = 'IPE 300',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Section
        clientObject = Model.clientModel.factory.create('ns0:section')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Section No.
        clientObject.no = no

        # Section nNme
        clientObject.name = name

        # Material No.
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Section to client model
        Model.clientModel.service.set_section(clientObject)
