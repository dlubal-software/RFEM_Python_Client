from RFEM.initModel import Model


class RfemObject:
    def __init__(self,
                 key: str,
                 comment: str = '',
                 params: dict = None):

        # Mutable Default Arguments
        if params is None:
            params = {}

        # Client model | Node
        self.clientObject = Model.clientModel.factory.create(key)

        # Clears object attributes | Sets all attributes to None
        for i in iter(self.clientObject):
            self.clientObject[i[0]] = None

        # Adding optional parameters via dictionary
        # This happens first to prevent overwriting of other properties
        for key in params:
            self.clientObject[key] = params[key]

        # Comment
        self.clientObject.comment = comment
