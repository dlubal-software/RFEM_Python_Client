import sys
import enum
from RFEM.initModel import Model
from RFEM.enums import PlausibilityCheckType

class PlausibilityCheck():

    def __init__(self,
                 plausibility_check_type:enum = PlausibilityCheckType.PLAUSIBILITY_CHECK,
                 skip_warnings:bool = False,
                 model = Model):

        response = model.clientModel.service.plausibility_check(plausibility_check_type.name, skip_warnings)

        if response["errors_and_warnings"] and response["errors_and_warnings"][0] and not skip_warnings:
            errormessage = ''
            for item in response["errors_and_warnings"][0]:
                errors_and_warnings = ''
                if item.message_type == "ERROR":
                    errors_and_warnings = "".join([item.message_type, '!\nObject: ', item.input_field,", ", item.object,", current value: ", item.current_value,", message: ", item.message])
                elif item.message_type == "WARNING":
                    errors_and_warnings =  "".join([item.message_type, '!\n', item.message])
                errormessage += '\n'+errors_and_warnings.replace('<br>','\n')

            sys.exit(errormessage)
