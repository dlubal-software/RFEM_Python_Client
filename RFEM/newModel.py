from RFEM.initModel import client
import os


class NewModelAsCopy():
    def __init__(self,
                 old_model_name: str = '',
                 old_model_folder: str = ''):

        '''
        Args:
            old_model_name (str): Old Model Name
            old_model_folder (str): Old Model Folder
        '''

        # Old Model Name
        new_model_name = ''
        if '.rf6' in old_model_name:
            new_model_name = old_model_name[:-4] + '_copy'

        else:
             assert TypeError('Model ' + old_model_name +  ' does not exist')

        old_model_path = os.path.join(old_model_folder, old_model_name)

        # New Model Name
        client.service.new_model_as_copy(new_model_name, old_model_path)
