from RFEM.initModel import clearAtributes, Model

class Material():
    def __init__(self,
                 no: int = 1,
                 name: str = 'S235',
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Material Tag
            name (str): Name of Desired Material (As Named in RFEM Database)
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Material
        clientObject = Model.clientModel.factory.create('ns0:material')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Material No.
        clientObject.no = no

        # Material Name
        clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add material to client model
        Model.clientModel.service.set_material(clientObject)
