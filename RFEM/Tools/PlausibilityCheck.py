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
        else:
            self.checkresult = PlausibilityCheckResult.CHECK_IS_OK.name
            self.message = 'Success'
            self.errormessage = ""

    def IsModelOK(self):

        return self.checkresult

    def GetErrorMessage(self):

        return self.errormessage
