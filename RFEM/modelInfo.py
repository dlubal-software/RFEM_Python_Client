from RFEM.initModel import Model
from RFEM.enums import ModelType


class ModelInfo():
    def __init__(self,
                 model = Model):

        # Client Model | Get Model Info
        modelInfo = model.clientModel.service.get_model_info()


class ModelMainParameters():
    def __init__(self,
                 model_id: str = '',
                 model_name: str = '',
                 model_description: str = '',
                 model_comment: str = '',
                 model_path: str = '',
                 project_id: str = '',
                 project_name: str = '',
                 project_description: str = '',
                 project_folder: str = '',
                 model = Model):

        # Client Model | Get Model Main Parameters
        # clientObject = model.clientModel.service.get_model_main_parameters()
        clientObject = model.clientModel.factory.create('ns0:model_main_parameters')

        # Model Id
        # mid = model.clientModel.factory.create('ns0:model_id')
        clientObject.model_id = model_id

        # Model Name
        clientObject.model_name = model_name

        # Model Description
        clientObject.model_description = model_description

        # Model Comment
        clientObject.model_comment = model_comment

        # Model Path
        clientObject.model_path = model_path

        # Project ID
        clientObject.project_id = project_id

        # Project Name
        clientObject.project_name = project_name

        # Project Description
        clientObject.project_description = project_description

        # Project Folder
        clientObject.project_folder = project_folder

        # Add Base Data Model Main Parameters to client model
        model.clientModel.service.set_model_parameters(clientObject)


class ModelParameters():
    def __init__(self,
                 model_parameters: list = None,
                 model = Model):

        '''
        Args:
            model_parameters (list of lists): Model Parameters Table
                model_parameters = [[name, description_1, description_2],...]
            model (RFEM Class, optional): Model to be edited
        '''

        # Client Model | Get Model Parameters
        clientObject = model.clientModel.service.get_model_parameters()

        # Add Model Parameters

        for i,j in enumerate(model_parameters):
            mp = Model.clientModel.factory.create('ns0:model_parameters_row')
            mp.no = i+3
            mp.description = i+3
            mp.row.name = model_parameters[i][0]
            mp.row.description_1 = model_parameters[i][1]
            mp.row.description_2 = model_parameters[i][2]

            clientObject.model_parameters.append(mp)

        # Add Base Data Model Parameters to client model
        model.clientModel.service.set_model_parameters(clientObject)


class ModelHistory():
    def __init__(self,
                model_history: list = None,
                model = Model):

        '''
        Args:
            model_history (list of lists): Model History Table
                model_history = [[time, username, ModelHistoryStatusType Enumeration, comment],...]
            model (RFEM Class, optional): Model to be edited
        '''

        # Client Model | Get Model History
        clientObject = model.clientModel.service.get_model_history()

        # Add Model History

        for i,j in enumerate(model_history):
            mh = Model.clientModel.factory.create('ns0:model_history_row')
            mh.no = i+1
            mh.description = i+1
            mh.row.time = model_history[i][0]
            mh.row.user = model_history[i][1]
            mh.row.history_status_type = model_history[i][2].name
            mh.row.comment = model_history[i][3]

            clientObject.model_history.append(mh)

        # Add Base Data Model History to client model
        model.clientModel.service.set_model_history(clientObject)


class SessionId():
    def __init__(self,
                 model = Model):

        # Client Model | Get Session Id
        clientObject = model.clientModel.service.get_session_id()



class ApplicationInfo():
    def __init__(self):
        pass

    def GetName():
        pass

    def GetVersion():
        pass

    def GetLanguage():
        pass