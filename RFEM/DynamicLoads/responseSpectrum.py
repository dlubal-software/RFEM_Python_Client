from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import ResponseSpectrumDefinitionType

class ResponseSpectrum():

    def __init__(self,
                 no: int = 1,
                 name: str = '',
                 constant_period_step: float = None,
                 sort_table: bool = True,
                 user_defined_spectrum: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Response Spectrum Tag
            name (str): User Defined Name
            constant_period_step (float): Enables Constant Period Step
            sort_table (bool): Sort Table Option
            user_defined_spectrum (list): User Defined Spectrum

                user_defined_spectrum = [[period, acceleration], [period, acceleration], ...]

            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # client model | response spectrum
        clientObject = model.clientModel.factory.create('ns0:response_spectrum')

        # clear object atributes | sets all the atributes to none
        clearAttributes(clientObject)

        # response spectrum no.
        clientObject.no = no

        # response spectrum definition type
        clientObject.definition_type = ResponseSpectrumDefinitionType.USER_DEFINED.name

        # user defined name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # constant period step option
        if constant_period_step:
            clientObject.user_defined_response_spectrum_step_enabled = True
            clientObject.user_defined_response_spectrum_period_step = constant_period_step

        # sort table option
        clientObject.user_defined_spectrum_sorted = sort_table

        # user defined spectrum
        clientObject.user_defined_response_spectrum = model.clientModel.factory.create('ns0:response_spectrum.user_defined_response_spectrum')

        for i,j in enumerate(user_defined_spectrum):
            rsp = model.clientModel.factory.create('ns0:response_spectrum_user_defined_response_spectrum_row')
            rsp.no = i+1
            rsp.row.period = user_defined_spectrum[i][0]
            rsp.row.acceleration = user_defined_spectrum[i][1]

            clientObject.user_defined_response_spectrum.response_spectrum_user_defined_response_spectrum.append(rsp)

        # comment
        clientObject.comment = comment

        # adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add global parameter to client model
        model.clientModel.service.set_response_spectrum(clientObject)


    @staticmethod
    def UserDefinedGFactor(no: int = 1,
                           name: str = '',
                           constant_period_step: float = None,
                           sort_table: bool = True,
                           user_defined_spectrum: list = None,
                           comment: str = '',
                           params: dict = None,
                           model = Model):

        """
        Args:
            no (int): Response Spectrum Tag
            name (str): User Defined Name
            constant_period_step (float): Enables Constant Period Step
            sort_table (bool): Sort Table Option
            user_defined_spectrum (list): User Defined Spectrum

                user_defined_spectrum = [[period, acceleration], [period, acceleration], ...]

            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # client model | response spectrum
        clientObject = model.clientModel.factory.create('ns0:response_spectrum')

        # clear object atributes | sets all the atributes to none
        clearAttributes(clientObject)

        # response spectrum no.
        clientObject.no = no

        # response spectrum definition type
        clientObject.definition_type = ResponseSpectrumDefinitionType.USER_DEFINED_IN_G_FACTOR.name

        # user defined name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # constant period step option
        if constant_period_step:
            clientObject.user_defined_response_spectrum_step_enabled = True
            clientObject.user_defined_response_spectrum_period_step = constant_period_step

        # sort table option
        clientObject.user_defined_spectrum_sorted = sort_table

        # user defined spectrum
        clientObject.user_defined_response_spectrum = model.clientModel.factory.create('ns0:response_spectrum.user_defined_response_spectrum')

        for i,j in enumerate(user_defined_spectrum):
            rsp = model.clientModel.factory.create('ns0:response_spectrum_user_defined_response_spectrum_row')
            rsp.no = i+1
            rsp.row.period = user_defined_spectrum[i][0]
            rsp.row.acceleration = user_defined_spectrum[i][1]

            clientObject.user_defined_response_spectrum.response_spectrum_user_defined_response_spectrum.append(rsp)

        # comment
        clientObject.comment = comment

        # adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # add global parameter to client model
        model.clientModel.service.set_response_spectrum(clientObject)


