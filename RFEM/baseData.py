from RFEM.initModel import Model, clearAttributes
from RFEM.enums import ModelType

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
            mp.row = Model.clientModel.factory.create('ns0:model_parameters')
            clearAttributes(mp.row)
            mp.row.name = model_parameters[i][0]
            mp.row.description_1 = model_parameters[i][1]
            mp.row.description_2 = model_parameters[i][2]

            clientObject.model_parameters.append(mp)

        # Add Base Data Model Parameters to client model
        model.clientModel.service.set_model_parameters(clientObject)

class ModelParametersLocation():

    def __init__(self,
                 model_parameters_location: list = None,
                 model = Model):

        '''
        Args:
            model_parameters_location (list of lists): Model Parameters Location Table
                model_parameters_location = [[ModelLocationRowType Enumeration, name, value, unit_group],...]
            model (RFEM Class, optional): Model to be edited
        '''

        # Client Model | Get Model Parameters Location
        clientObject = model.clientModel.service.get_model_parameters_location()

        # Add Model Parameters

        for i,j in enumerate(model_parameters_location):
            mpl = Model.clientModel.factory.create('ns0:model_parameters_location_row')
            mpl.no = i+1
            mpl.description = str(i+1)
            mpl.row = Model.clientModel.factory.create('ns0:model_parameters_location')
            clearAttributes(mpl.row)
            mpl.row.location_row_type = model_parameters_location[i][0].name
            mpl.row.name = model_parameters_location[i][1]
            mpl.row.value = model_parameters_location[i][2]
            mpl.row.unit_group = model_parameters_location[i][3]

            clientObject.model_parameters_location.append(mpl)

        # Add Base Data Model Parameters to client model
        model.clientModel.service.set_model_parameters_location(clientObject)

class Modeltype():

    def __init__(self,
                 model_type = ModelType.E_MODEL_TYPE_3D,
                 model = Model):
        '''
        Args:
            model_type (enum): Model Type Enumeration
            model (RFEM Class, optional): Model to be edited
        '''

        # Add Model Type to Client Model
        model.clientModel.service.set_model_type(model_type.name)
