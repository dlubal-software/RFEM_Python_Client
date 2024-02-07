import enum
from RFEM.initModel import Model
from RFEM.enums import PlausibilityCheckType

class PlausibilityCheck():

    def __init__(self,
                 plausibility_check_type:enum = PlausibilityCheckType.PLAUSIBILITY_CHECK,
                 skip_warnings:bool = False,
                 model = Model):

        response = model.clientModel.service.plausibility_check(plausibility_check_type.name, skip_warnings)
        
        self.errormessage = ""

        if response["errors_and_warnings"] and response["errors_and_warnings"][0]:
            errors_and_warnings = ["".join([item.message_type,\
                                            ": Input field: ", item.input_field,\
                                                ", object: ", item.object,\
                                                    ", current value: ", item.current_value,\
                                                        ". Message: ", item.message]) if item.message_type == "ERROR"\
                                                            else "".join([item.message_type, ": ", item.message]) if not skip_warnings else None for item in response["errors_and_warnings"][0]]
            self.errormessage = "\n".join(errors_and_warnings)

    
    def IsModelOK(self):
        return not self.errormessage
    

    def GetErrorsAndWarnings(self):
        return self.errormessage
