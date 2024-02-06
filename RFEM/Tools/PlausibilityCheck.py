import enum
from RFEM.initModel import Model
from RFEM.enums import PlausibilityCheckResult, PlausibilityCheckType

class PlausibilityCheck():

    def __init__(self,
                 plausibility_check_type:enum = PlausibilityCheckType.PLAUSIBILITY_CHECK,
                 skip_warnings:bool = False,
                 model = Model):

        response = model.clientModel.service.plausibility_check(plausibility_check_type.name, skip_warnings)

        if "failed" in response:
            self.checkresult = PlausibilityCheckResult.CHECK_FAILED.name
            self.message = response.split("Messages received:", 1)[1]
            self.errormessage = self.message.split("Result 'false'", 1)[0]
        elif len((errors := [error_or_warning.message for error_or_warning in response["errors_and_warnings"][0] if error_or_warning.message_type=="ERROR"])) > 0:
            self.checkresult = PlausibilityCheckResult.CHECK_ERRORS.name
            self.message = 'Errors'
            self.errormessage = "\n".join(errors)
        elif not skip_warnings and "errors_and_warnings" in response and \
                len(warnings := [error_or_warning.message for error_or_warning in response["errors_and_warnings"][0] if error_or_warning.message_type=="WARNING"]) > 0:
            self.checkresult = PlausibilityCheckResult.CHECK_WARNINGS.name
            self.message = 'Warnings'
            self.errormessage = "\n".join(warnings)
        else:
            self.checkresult = PlausibilityCheckResult.CHECK_IS_OK.name
            self.message = 'Success'
            self.errormessage = ""

    def IsModelOK(self):

        return self.checkresult

    def GetErrorMessage(self):

        return self.errormessage
