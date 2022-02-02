from RFEM.initModel import Model
from RFEM.enums import PlausibilityCheckResult

class PlausiblityCheck():

    def __init__(self):

        response = Model.clientModel.service.plausibility_check()

        if "failed" in response:
            self.checkresult = PlausibilityCheckResult.CHECK_FAILED
            self.message = response.split("Messages received:", 1)[1]
            self.errormessage = self.message.split("Result 'false'", 1)[0]
        else:
            self.checkresult = PlausibilityCheckResult.CHECK_IS_OK
            self.errormessage = ""

    def IsModelOK(self):

        if self.checkresult == PlausibilityCheckResult.CHECK_IS_OK:
            return True
        else:
            return False

    def GetErrorMessage(self):

        return self.errormessage

    def GetModelCheckStatus(self):

        if self.checkresult == PlausibilityCheckResult.CHECK_IS_OK:
            print("Plausibility check succeeded.\nModel is OK")
        elif self.checkresult == PlausibilityCheckResult.CHECK_FAILED:
            print("Plausibility check failed.\nModel is not OK")
        else:
            print("No plausibility check result.")
