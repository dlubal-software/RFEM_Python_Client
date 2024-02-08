import os
import sys
dirName = os.path.dirname(__file__)
sys.path.append(dirName + r'/..')

from RFEM.initModel import Model, openFile, CalculateSelectedCases
from RFEM import connectionGlobals

def close_all_models():
    opened_models = connectionGlobals.client.service.get_model_list()
    for _ in opened_models["name"]:
        connectionGlobals.client.service.close_model(0, False)

if __name__ == "__main__":
    Model()
    print("Closing models...")
    close_all_models()

    dir_name = os.path.join(os.getcwd(), os.path.dirname(__file__))

    print("Opening file...")
    model = openFile(os.path.join(dirName, "bug157811.rf6"))

    load_cases = model.clientModel.service.get_all_object_numbers_by_type("E_OBJECT_TYPE_LOAD_CASE")

    load_cases_no = []
    for item in load_cases.item:
        load_cases_no.append(item.no)
    
    calculation_messages = CalculateSelectedCases(loadCases=load_cases_no)
    
            