from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes

class SolidGas():
    def __init__(self,
                 no: int = 1,
                 pressure: float = 100000,
                 temperature: float = 283.15,
                 solids: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Gas Solids

        Args:
            no (int): Solid Contact Tag
            pressure (float): Preassure in Pascals
            temperature (float): Temperature in Kelvins
            solids (str): Assigned to solids
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Solid Gas
        clientObject = model.clientModel.factory.create('ns0:solid_gas')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Solid Gas No.
        clientObject.no = no

        # Solid Gas Pressure
        clientObject.pressure = pressure

        # Solid Gas Temperature
        clientObject.temperature = temperature

        # Assigned to Solids
        clientObject.solids = solids

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Solid Gas to client model
        model.clientModel.service.set_solid_gas(clientObject)
