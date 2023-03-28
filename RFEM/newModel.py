from RFEM.initModel import Model, client

url = 'http://127.0.0.1'

class NewModelAsCopy():
    def __init__(self,
                 old_model_name: str = 'TestModel.rf6',
                 new_model_name: str = 'TestModel_copy.rf6'):

        # New Model Name
        clientNewModelCopy.model_name = new_model_name
        clientNewModelCopy = client.service.new_model_as_copy(new_model_name)

        # Old Model Path
        modelPath =  client.service.get_model(old_model_name)
        modelPort = modelPath[-5:-1]
        modelUrlPort = url+':'+modelPort
        modelCompletePath = modelUrlPort+'/wsdl'

        clientNewModelCopy.file_path = modelCompletePath


class NewModelFromTemplate():
    def __init__(self):

        # Application Model | New Model As Copy
        clientNewModelTemplate = client.service.new_model_from_template()

        return clientNewModelTemplate
