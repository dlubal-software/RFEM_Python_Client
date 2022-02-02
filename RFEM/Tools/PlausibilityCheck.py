from RFEM.initModel import Model
from RFEM.enums import PlausibilityCheckResult

class PlausiblityCheck():

    def __init__(self,
                 skip_warnings:bool = False):

        response = Model.clientModel.service.plausibility_check(skip_warnings)

        if "failed" in response:
            self.checkresult = PlausibilityCheckResult.CHECK_FAILED.name
            self.message = response.split("Messages received:", 1)[1]
            self.errormessage = self.message.split("Result 'false'", 1)[0]
        else:
            self.checkresult = PlausibilityCheckResult.CHECK_IS_OK.name
            self.message = 'Success'
            self.errormessage = ""

    def IsModelOK(self):

        return self.checkresult == PlausibilityCheckResult.CHECK_IS_OK.name

    def GetErrorMessage(self):

        return self.errormessage
