import time
from typing import List
from RFEM.enums import ResultOfCalculation, MessageType, ObjectTypes
from RFEM.initModel import Model


class ErrorMessage():

    message_type: MessageType
    message: str = ''
    input_field: str = ''
    object: str = ''
    current_value: str = ''
    result: bool = False

    def __init__(self, message) -> None:

        self.message = message.message
        if hasattr(message, 'input_field'):
            self.input_field = message.input_field
        if hasattr(message, 'object'):
            self.object = message.object
        if hasattr(message, 'current_value'):
            self.current_value = message.current_value
        self.result = message.result
        if 'WARNING' in message.message_type:
            self.message_type = MessageType.WARNING
        elif 'ERROR' in message.message_type:
            self.message_type = MessageType.ERROR
        elif 'INFO' in message.message_type:
            self.message_type = MessageType.INFO

    def GetErrorMessageString(self) -> str:
        error = str(f"{self.message_type.name}  {self.message} {self.input_field if self.input_field is not None else ''} {self.object  if self.object is not None else ''} {self.current_value if self.current_value is not None else ''} {str(self.result)}")
        return error


class CalculationError():

    calculation_error_no: int = 0
    description: str = ''
    analysis_type: str = ''
    calculation_error_description: str = ''
    calculation_error_or_warnings_number: str = ''
    calculation_error_object: str = ''

    def __init__(self, calculation_error) -> None:

        self.calculation_error_no = calculation_error.no
        self.description = calculation_error.description
        self.analysis_type = calculation_error.row.analysis_type
        self.calculation_error_description = calculation_error.row.description
        self.calculation_error_or_warning_number = calculation_error.row.error_or_warning_number
        self.calculation_error_object = calculation_error.row.object

    def GetCalculationErrorString(self) -> str:
        error = str(f"{self.calculation_error_no} {self.calculation_error_description} {self.analysis_type} {self.calculation_error_or_warning_number} {self.description} {self.calculation_error_object}")
        return error


def GetCalculationError( model: type[Model] = Model) -> List[type[CalculationError]]:

    errors = model.clientModel.service.get_calculation_errors()
    calculation_errors: list[type[CalculationError]] = []

    if any(errors.errors):
        for error in errors.errors:
            calculation_error = CalculationError(error)
            calculation_errors.append(calculation_error)
            model.ModelLogger.error(calculation_error.GetCalculationErrorString())

    return calculation_errors


class CalculationResult():

    succeeded: bool = False
    messages: str = ''
    errors_and_warnings: list[type[object]] = []

    def __init__(self, succeeded: bool = False, messages: str = '') -> None:
        self.succeeded = succeeded
        self.messages = messages


class CalculationResultInfo():

    result_of_calculation = None
    error_messages: list[ErrorMessage] = []
    calculation_messages: str = ''
    calculation_errors: list[type[CalculationError]] = []
    get_calculation_error: bool = False

    def __init__(self,
                 calculation_result: object,
                 get_calculation_error: bool = True,
                 model: type[Model] = Model)-> None:

        self.get_calculation_error = get_calculation_error

        if calculation_result.succeeded and not calculation_result.messages:
            self.result_of_calculation = ResultOfCalculation.SUCCESSFUL_CALCULATION
            model.ModelLogger.info('Calculation finished successfully')
        else:
            self.result_of_calculation = ResultOfCalculation.UNSUCCESSFUL_CALCULATION
            model.ModelLogger.error('Calculation finished unsuccessfully')
            if (calculation_result.messages):
                self.calculation_messages = calculation_result.messages
                model.ModelLogger.error(f"{calculation_result.messages}")
            if any(calculation_result.errors_and_warnings):
                for message in calculation_result.errors_and_warnings.message:
                    err = ErrorMessage(message)
                    self.error_messages.append(err)
                    model.ModelLogger.error(err.GetErrorMessageString())

        if self.result_of_calculation is ResultOfCalculation.UNSUCCESSFUL_CALCULATION:
            if self.calculation_messages and self.get_calculation_error:
                self.calculation_errors = GetCalculationError(model)

    def IsCalculationSucessful(self) -> bool:
        if self.result_of_calculation is ResultOfCalculation.SUCCESSFUL_CALCULATION:
            return True
        else:
            return False

    def GetErrorMessages(self) -> List[ErrorMessage]:
        return self.error_messages

    def GetCalculationMessages(self):
        return self.calculation_messages


def HandleCalculationException(faultstring: str = '', model: type[Model] = Model):

    calculation_result = CalculationResult(False, faultstring)
    calculation_results_info = CalculationResultInfo(calculation_result, False, model)

    return calculation_results_info


def Calculate_all(skip_warnings: bool = True, get_calculation_errors: bool = True, model: type[Model] = Model) -> CalculationResultInfo:
    '''
    Calculates model.
    CAUTION: Don't use it in unit tests!
    It works when executing tests individually but when running all of them
    it causes RFEM to stuck and generates failures, which are hard to investigate.

    Args:
        skip_warnings (bool): if calculation can skip warnings
        get_calculation_errors: if function should call get_calculation_errors after unsuccessful calculation
        model (RFEM Class, optional): Model to be edited
    '''
    model.ModelLogger.info('Staring calculation')
    start_time: float = time.time()
    calculation_result = None
    calculation_results_info: CalculationResultInfo

    try:
        calculation_result = model.clientModel.service.calculate_all(skip_warnings)
    except Exception as inst:
        model.ModelLogger.exception(inst.fault.faultstring)
        calculation_results_info = HandleCalculationException(inst.fault.faultstring)
    else:
        if isinstance(calculation_result, str) and not calculation_result:
            calculation_result_new = CalculationResult(True)
            calculation_results_info = CalculationResultInfo(calculation_result_new,False, model)
        else:
            calculation_results_info = CalculationResultInfo(calculation_result,get_calculation_errors, model)

    end_time: float = time.time()
    elapsed_time: float = end_time - start_time
    model.ModelLogger.info(f'Elapsed calculation time: {elapsed_time}')

    return calculation_results_info


def CalculateSelectedCases(loadCases: list = None, designSituations: list = None, loadCombinations: list = None,skipWarnings: bool = True, get_calculation_errors: bool  = True, model: type[Model] = Model) -> CalculationResultInfo:
    '''
    This method calculate just selected objects - load cases, designSituations, loadCombinations

    Args:
        loadCases (list, optional): Load Case List
        designSituations (list, optional): Design Situations List
        loadCombinations (list, optional): Load Combinations List
        skip_warnings (bool): if calculation can skip warnings
        get_calculation_errors: if function should call get_calculation_errors after unsuccessful calculation
        model (RFEM Class, optional): Model to be edited
    '''
    specificObjectsToCalculate = model.clientModel.factory.create('ns0:calculate_specific_loadings')
    if loadCases:
        for loadCase in loadCases:
            specificObjectsToCalculateLS = model.clientModel.factory.create('ns0:calculate_specific_loadings.loading')
            specificObjectsToCalculateLS.no = loadCase
            specificObjectsToCalculateLS.type = ObjectTypes.E_OBJECT_TYPE_LOAD_CASE.name
            specificObjectsToCalculate.loading.append(specificObjectsToCalculateLS)

    if designSituations:
        for designSituation in designSituations:
            specificObjectsToCalculateDS = model.clientModel.factory.create('ns0:calculate_specific_loadings.loading')
            specificObjectsToCalculateDS.no = designSituation
            specificObjectsToCalculateDS.type = ObjectTypes.E_OBJECT_TYPE_DESIGN_SITUATION.name
            specificObjectsToCalculate.loading.append(specificObjectsToCalculateDS)

    if loadCombinations:
        for loadCombination in loadCombinations:
            specificObjectsToCalculateCC = model.clientModel.factory.create('ns0:calculate_specific_loadings.loading')
            specificObjectsToCalculateCC.no = loadCombination
            specificObjectsToCalculateCC.type = ObjectTypes.E_OBJECT_TYPE_LOAD_COMBINATION.name
            specificObjectsToCalculate.loading.append(specificObjectsToCalculateCC)

    model.ModelLogger.info('Staring calculation')
    start_time: float = time.time()
    calculation_result = None
    calculation_results_info: CalculationResultInfo

    try:
        calculation_result = model.clientModel.service.calculate_specific(specificObjectsToCalculate,skipWarnings)
    except Exception as inst:
        model.ModelLogger.exception(inst.fault.faultstring)
        calculation_results_info = HandleCalculationException(inst.fault.faultstring)
    else:
        if isinstance(calculation_result, str) and not calculation_result:
            calculation_result_new = CalculationResult(True)
            calculation_results_info = CalculationResultInfo(calculation_result_new,False, model)
        else:
            calculation_results_info = CalculationResultInfo(calculation_result,get_calculation_errors, model)

    end_time: float = time.time()
    elapsed_time: float = end_time - start_time
    model.ModelLogger.info(f'Elapsed calculation time: {elapsed_time}')

    return calculation_results_info


def HasAnyResults() -> None:
    pass