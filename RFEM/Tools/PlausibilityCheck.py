#pylint: disable=W0614, W0401, W0622, C0103, C0114, C0115, C0116, C0301, C0413, R0913, R0914, R0915, C0305, C0411, W0102, W0702, E0602, E0401

from RFEM.initModel import *
from RFEM.enums import *

class PlausiblityCheck():

    def __init__(self):

        response = clientModel.service.plausibility_check()

        if "failed" in response:
            self.checkresult = PlausibilityCheckResult.CHECK_FAILED
            self.message = response.split("Messages received:", 1)[1]
            self.errormessage = self.message.split("Result 'false'", 1)[0]
        else:
            self.checkresult = PlausibilityCheckResult.CHECK_IS_OK
            self.errormessage = ""

    def IsModelOK(self):

        if self.checkresult == PlausibilityCheckResult.CHECK_FAILED:
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
