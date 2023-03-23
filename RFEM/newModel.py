from RFEM.initModel import Model, client


class NewModelAsCopy():
    def __init__(self):

        # Application Model | New Model As Copy
        clientNewModelCopy = client.service.new_model_as_copy()

        return clientNewModelCopy

class NewModelFromTemplate():
    def __init__(self):

        # Application Model | New Model As Copy
        clientNewModelTemplate = client.service.new_model_from_template()

        return clientNewModelTemplate
