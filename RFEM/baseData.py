from RFEM.initModel import Model
from RFEM.enums import ModelType

class ModalHistory():

    def __init__(self,
                 model_history: list = None,
                 model = Model):

        '''
        Args:

        '''

        # Client Model | Get Model History
        clientObject = model.clientModel.service.get_model_history()

        # Add Model History

        clientObject.table_values = Model.clientModel.factory.create('ns0:array_of_model_history')

        for i,j in enumerate(model_history):
            mh = Model.clientModel.factory.create('ns0:model_history_row')
            mh.no = i+1
            mh.description = i+1
            mh.row.time = model_history[i][0]
            mh.row.user = model_history[i][1]
            mh.row.history_status_type = model_history[i][2].name
            mh.row.comment = model_history[i][3]

            clientObject.table_values.model_history.append(mh)

        # Add Base Data Model History to client model
        model.clientModel.service.set_model_history(clientObject)


class ModalParameters():

    def __init__(self,
                 model_parameters: list = None,
                 model = Model):

        '''
        Args:

        '''

        # Client Model | Get Model Parameters
        clientObject = model.clientModel.service.get_model_parameters()

        # Add Model Parameters

        clientObject.table_values = Model.clientModel.factory.create('ns0:array_of_model_parameters')

        for i,j in enumerate(model_parameters):
            mp = Model.clientModel.factory.create('ns0:model_parameters_row')
            mp.no = i+1
            mp.description = i+1
            mp.row.name = model_parameters[i][0]
            mp.row.description_1 = model_parameters[i][1]
            mp.row.description_2 = model_parameters[i][2]

            clientObject.table_values.model_parameters.append(mp)

        # Add Base Data Model Parameters to client model
        model.clientModel.service.set_model_parameters(clientObject)

