import enum
from RFEM.initModel import Model
from RFEM.enums import PlausibilityCheckResult, PlausibilityCheckType

from RFEM.Calculate.calculate import ErrorMessage



class PlausibilityCheck():

    # plausibility_check_info = None
    plausibility_check_result: PlausibilityCheckResult = PlausibilityCheckResult.CHECK_FAILED
    error_messages: list[type[ErrorMessage]] = []
    messages: str = ''

    def __init__(self,
                 skip_warnings: bool = False,
                 plausibility_check_type: PlausibilityCheckType = PlausibilityCheckType.CALCULATION,
                 model: type[Model] = Model) -> None:

        try:
            plausibility_check = model.clientModel.service.plausibility_check(plausibility_check_type.name,skip_warnings)
        except Exception as inst:
            model.ModelLogger.exception(inst.fault.faultstring)
            # plausibility_check_info = HandleCalculationException(inst.fault.faultstring)
        else:
            if plausibility_check.succeeded:
                self.plausibility_check_result = PlausibilityCheckResult.CHECK_IS_OK
            else:
                self.plausibility_check_result = PlausibilityCheckResult.CHECK_FAILED
                if any(plausibility_check.messages.message):
                    for message in plausibility_check.messages.message:
                        err = ErrorMessage(message)
                        self.error_messages.append(err)
                        model.ModelLogger.error(err.GetErrorMessageString())

    def IsModelOK(self) -> bool:
                 plausibility_check_type:enum = PlausibilityCheckType.PLAUSIBILITY_CHECK,
                 skip_warnings:bool = False,
                 model = Model):

        response = model.clientModel.service.plausibility_check(plausibility_check_type.name, skip_warnings)

    def GetErrorMessage(self) -> list[type[ErrorMessage]]:

        return self.error_messages

    def GetPlausibilityCheckResult(self) -> PlausibilityCheckResult:

        return self.plausibility_check_result
