from RFEM.initModel import Model
from RFEM.enums import ModelType


class ModelInfo():
    def __init__(self,
                 model = Model):

        # Client Model | Get Model Info
        modelInfo = model.clientModel.service.get_model_info()


class ModelMainParameters():
    def __init__(self,
                model_main_parameters_model: list = [str, str, str, str, str],
                model_main_parameters_project: list = [str, str, str, str],
                model = Model):

        # Client Model | Get Model Main Parameters
        clientObject = model.clientModel.service.get_model_main_parameters()

        # Model Id
        clientObject.model_id = model_main_parameters_model[0]

        # Model Name
        clientObject.model_name = model_main_parameters_model[1]

        # Model Description
        clientObject.model_description = model_main_parameters_model[2]

        # Model Comment
        clientObject.model_comment = model_main_parameters_model[3]

        # Model Path
        clientObject.model_path = model_main_parameters_model[4]

        # Project ID
        clientObject.project_id = model_main_parameters_project[0]

        # Project Name
        clientObject.project_name = model_main_parameters_project[1]

        # Project Description
        clientObject.project_description = model_main_parameters_project[2]

        # Project Folder
        clientObject.project_folder = model_main_parameters_project[3]

        # Add Base Data Model Parameters to client model
        model.clientModel.service.set_model_main_parameters(clientObject)


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


class SessionID():
    def __init__(self,
                 value: str = '',
                 model = Model):
        '''
        Args:
            value (string): Value
            model (RFEM Class, optional): Model to be edited
        '''

        # Client Model | Get Session Id
        clientObject = model.clientModel.service.get_session_id()

        # Value
        clientObject.value = value

        # Add Base Data Session Id to client model
        model.clientModel.service.set_session_id(clientObject)



class ApplicationInfo():
    def __init__(self):
        pass

    def GetName():
        pass

    def GetVersion():
        pass

    def GetLanguage():
        pass