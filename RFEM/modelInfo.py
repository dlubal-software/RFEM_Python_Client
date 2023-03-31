from RFEM.initModel import Model, client


class ModelInfo():
    def __init__(self,
                 model = Model):

        '''
        Args:
            model (RFEM Class, optional): Model to be edited
        '''

        # Client Model | Get Model Info
        modelInfo = model.clientModel.service.get_model_info()


class ModelMainParameters():
    def ModelMainParameters(model = Model):

        '''
        Args:
            model (RFEM Class, optional): Model to be edited
        '''

        # Client Model | Get Model Main Parameters
        clientObject = model.clientModel.service.get_model_main_parameters()

        return clientObject

    def ModelId(model = Model):

        '''
        Args:
            model (RFEM Class, optional): Model to be edited
        '''

        # Client Model | Get Model ID
        clientModelId = model.clientModel.service.get_model_main_parameters().model_id

        return clientModelId


class ModelParameters():
    def ModelParameters(model = Model):

        '''
        Args:
            model (RFEM Class, optional): Model to be edited
        '''

        # Client Model | Get Model Parameters
        clientObject = model.clientModel.service.get_model_parameters()

        return clientObject


class SessionId():
    def SessionId(model = Model):

        '''
        Args:
            model (RFEM Class, optional): Model to be edited
        '''

        # Client Model | Get Session Id
        clientObject = model.clientModel.service.get_session_id()


class ApplicationInfo():

    @staticmethod
    def GetName():

        # Client Application | Get Information
        clientName = client.service.get_information().name

        return clientName

    @staticmethod
    def GetVersion():

        # Client Application | Get Information
        clientVersion = client.service.get_information().version

        return clientVersion

    @staticmethod
    def GetLanguage():

        # Client Application | Get Information
        clientLanguage = client.service.get_information().language_name

        return clientLanguage


class ApplicationSessionId():
    @staticmethod
    def GetSessionId():

        # Client Application | Get Session ID
        clientsessionId = client.service.get_session_id()

        return clientsessionId
