from RFEM.initModel import Model, ErrorMessage
from RFEM.enums import PlausibilityCheckResult,PlausibilityCheckType

class PlausibilityCheck():

    plausibility_check_messages = []
    checkresult = None

    def __init__(self,
                 skip_warnings:bool = False,
                 plausibility_check_type:PlausibilityCheckType = PlausibilityCheckType.CALCULATION,
                 model = Model):

        response = model.clientModel.service.plausibility_check(plausibility_check_type.name,skip_warnings)

        if any(response.messages.message):
            self.checkresult = PlausibilityCheckResult.CHECK_FAILED
            for message in response.messages.message:
                err = ErrorMessage(message)
                self.plausibility_check_messages.append(err)
                model.ModelLogger.error(err.GetErrorMessageString())
        else:
            self.checkresult = PlausibilityCheckResult.CHECK_IS_OK

        # if "failed" in response:
        #     self.checkresult = PlausibilityCheckResult.CHECK_FAILED.name
        #     self.message = response.split("Messages received:", 1)[1]
        #     self.errormessage = self.message.split("Result 'false'", 1)[0]
        # else:
        #     self.checkresult = PlausibilityCheckResult.CHECK_IS_OK.name
        #     self.message = 'Success'
        #     self.errormessage = ""

    def IsModelOK(self):

        return self.checkresult.name

    def GetErrorMessage(self):

        return self.plausibility_check_messages
