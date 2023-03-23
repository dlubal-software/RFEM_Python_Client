from RFEM.initModel import Model, client
from RFEM.enums import ApplicationTypes

class NewModelAsCopy():
    def __init__(self,
                 model_name: str = '',
                 file_path: str =''):

        # Application Model | New Model As Copy
        clientNewModelCopy = client.service.new_model_as_copy()

        # Model Name
        clientNewModelCopy.model_name = model_name

        # File Path
        clientNewModelCopy.file_path = file_path


class NewModelFromTemplate():
    def __init__(self,
                 model_name: str = '',
                 file_path: str =''):

        # Application Model | New Model As Copy
        clientNewModelTemplate = client.service.new_model_from_template()

        # Model Name
        clientNewModelTemplate.model_name = model_name

        # File Path
        clientNewModelTemplate.file_path = file_path
