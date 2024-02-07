import enum
from RFEM.initModel import Model
from RFEM.enums import PlausibilityCheckResult, PlausibilityCheckType

class PlausibilityCheck():

    def __init__(self,
                 plausibility_check_type:enum = PlausibilityCheckType.PLAUSIBILITY_CHECK,
                 skip_warnings:bool = False,
                 model = Model):

        response = model.clientModel.service.plausibility_check(plausibility_check_type.name, skip_warnings)
        
        self.checkresult = PlausibilityCheckResult.CHECK_IS_OK
        self.errormessage = {}

        if response["errors_and_warnings"]:
            if len(errors := [error for error in response["errors_and_warnings"][0] if error.message_type=="ERROR"]) > 0:
                self.checkresult |= PlausibilityCheckResult.CHECK_ERROR
                errors = ["".join(["Input field: ", error.input_field, ", object: ", error.object, ", current value: ", error.current_value, ". Message: ", error.message]) for error in errors]
                self.errormessage[PlausibilityCheckResult.CHECK_ERROR] = "\n".join(errors)
            if not skip_warnings and len(warnings := [error_or_warning.message for error_or_warning in response["errors_and_warnings"][0] if error_or_warning.message_type=="WARNING"]) > 0:
                self.checkresult |= PlausibilityCheckResult.CHECK_WARNING
                self.errormessage[PlausibilityCheckResult.CHECK_WARNING] = "\n".join(warnings)

    def IsModelOK(self):
        return self.checkresult == PlausibilityCheckResult.CHECK_IS_OK
    
    def IsError(self):
        return PlausibilityCheckResult.CHECK_ERROR in self.checkresult
    
    def IsWarning(self):
        return PlausibilityCheckResult.CHECK_WARNING in self.checkresult

    def GetErrorMessages(self):
        return self.errormessage[PlausibilityCheckResult.CHECK_ERROR]
    
    def GetWarningMessages(self):
        return self.errormessage[PlausibilityCheckResult.CHECK_WARNING]
