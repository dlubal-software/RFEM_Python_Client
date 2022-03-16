import sys
import csv
from RFEM.enums import ObjectTypes, ModelType, AddOn

# Import SUDS module
try:
    sys.version_info[0] == 3
except:
    print('Must be using Python 3!')
    input('Press Enter to exit...')
    sys.exit()

try:
    from suds.client import Client
except:
    print('SUDS library is not installed in your Python env.')
    instSUDS = input('Do you want to install it (y/n)? ')
    instSUDS = instSUDS.lower()
    if instSUDS == 'y':
        # Subprocess will be opened in cmd and closed automaticaly after installation.
        # Prevents invoking pip by an old script wrapper (https://github.com/pypa/pip/issues/5599)
        import subprocess
        try:
            subprocess.call('python -m pip install --upgrade pip')
            subprocess.call('python -m pip install suds-py3 --user')
            from suds.client import Client
        except:
            print('WARNING: Installation of SUDS library failed!')
            print('Please use command "pip install suds-py3 --user" in your Command Prompt.')
            input('Press Enter to exit...')
            sys.exit()
    else:
        input('Press Enter to exit...')
        sys.exit()

try:
    import requests
except:
    print('requests library is not installed in your Python env.')
    instSUDS = input('Do you want to install it (y/n)? ')
    instSUDS = instSUDS.lower()
    if instSUDS == 'y':
        # Subprocess will be opened in cmd and closed automaticaly after installation.
        # Prevents invoking pip by an old script wrapper (https://github.com/pypa/pip/issues/5599)
        import subprocess
        try:
            subprocess.call('python -m pip install requests --user')
            import requests
        except:
            print('WARNING: Installation of requests library failed!')
            print('Please use command "pip install requests --user" in your Command Prompt.')
            input('Press Enter to exit...')
            sys.exit()
    else:
        input('Press Enter to exit...')
        sys.exit()

try:
    import suds_requests
except:
    print('suds_requests library is not installed in your Python env.')
    instSUDS = input('Do you want to install it (y/n)? ')
    instSUDS = instSUDS.lower()
    if instSUDS == 'y':
        # Subprocess will be opened in cmd and closed automaticaly after installation.
        # Prevents invoking pip by an old script wrapper (https://github.com/pypa/pip/issues/5599)
        import subprocess
        try:
            subprocess.call('python -m pip install suds_requests --user')
            import suds_requests
        except:
            print('WARNING: Installation of suds_requests library failed!')
            print('Please use command "pip install suds_requests --user" in your Command Prompt.')
            input('Press Enter to exit...')
            sys.exit()
    else:
        input('Press Enter to exit...')
        sys.exit()

try:
    import xmltodict
except:
    print('xmltodict library is not installed in your Python env.')
    instXML = input('Do you want to install it (y/n)? ')
    instXML = instXML.lower()
    if instXML == 'y':
        # Subprocess will be opened in cmd and closed automaticaly after installation.
        # Prevents invoking pip by an old script wrapper (https://github.com/pypa/pip/issues/5599)
        import subprocess
        try:
            subprocess.call('python -m pip install xmltodict --user')
            import xmltodict
        except:
            print('WARNING: Installation of xmltodict library failed!')
            print('Please use command "pip install xmltodict --user" in your Command Prompt.')
            input('Press Enter to exit...')
            sys.exit()
    else:
        input('Press Enter to exit...')
        sys.exit()

# Connect to server
# Check server port range set in "Program Options & Settings"
# By default range is set between 8081 ... 8089
print('Connecting to server...')
try:
    client = Client('http://localhost:8081/wsdl')
except:
    print('Error: Connection to server failed!')
    print('Please check:')
    print('- If you have started RFEM application')
    print('- If all RFEM dialogs are closed')
    print('- If server port range is set correctly')
    print('- Check Program Options & Settings > Web Services')
    sys.exit()

try:
    modelLst = client.service.get_model_list()
except:
    print('Error: Please check if all RFEM dialogs are closed.')
    input('Press Enter to exit...')
    sys.exit()

# Persistent connection
# Without next 4 lines the connection lasts only 1 request,
# the message: 'Application is locked by external connection'
# is blinking whole time and the execution is unnecessarily long.
# This solution works with unit-tests.
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=1)
session.mount('http://', adapter)
trans = suds_requests.RequestsTransport(session)

class Model():
    clientModel = None
    def __init__(self,
                 new_model: bool=True,
                 model_name: str="TestModel",
                 delete: bool=False,
                 delete_all: bool=False):

        cModel = None
        modelLs = client.service.get_model_list()

        if new_model:
            if modelLs and model_name in modelLs.name:
                new = client.service.open_model(model_name) + 'wsdl'
                cModel = Client(new, transport=trans)
                cModel.service.delete_all_results()
                cModel.service.delete_all()
            else:
                new = client.service.new_model(model_name) + 'wsdl'
                cModel = Client(new, transport=trans)
        else:
            modelIndex = 0
            for i,j in enumerate(modelLs):
                if modelLs[i] == model_name:
                    modelIndex = i
            new = client.service.get_model(modelIndex) + 'wsdl'
            cModel = Client(new, transport=trans)
            if delete:
                print('Deleting results...')
                cModel.service.delete_all_results()
            if delete_all:
                print('Delete all...')
                cModel.service.delete_all()

        Model.clientModel = cModel

def clearAtributes(obj):
    '''
    Clears object atributes.
    Sets all atributes to None.

    Params:
        obj: object to clear
    '''

    # iterator
    it = iter(obj)
    for i in it:
        obj[i[0]] = None
    return obj

def insertSpaces(lst: list):
    '''
    Add spaces between list of numbers.
    Returns list of values.
    '''
    strLst = ''
    for i in lst:
        strLst += str(i) + ' '
    # remove trailing space
    return strLst[:-1]

def Calculate_all(generateXmlSolverInput: bool = False):
    '''
    Calculates model.
    CAUTION: Don't use it in unit tests!
    It works when executing tests individualy but when running all of them
    it causes RFEM to stuck and generates failures, which are hard to investigate.

    Params:
    - generateXmlSolverInput: generate XML solver input
    '''
    Model.clientModel.service.calculate_all(generateXmlSolverInput)

def ConvertToDlString(s):
    '''
    The function converts strings commonly used in RSTAB / RFEM so that they
    can be used In WebServices. It solved issue #4.
    Examples:
    '1,3'       -> '1 3'
    '1, 3'      -> '1 3'
    '1-3'       -> '1 2 3'
    '1,3,5-9'   -> '1 3 5 6 7 8 9'

    Params:
        RSTAB / RFEM common string

    Returns a WS conform string.
    '''

    # Parameter is not of required type.
    assert isinstance(s, (list, str))

    if isinstance(s, list):
        return ' '.join(map(str, s))

    s = s.strip()
    s = s.replace(',', ' ')
    s = s.replace('  ', ' ')
    lst = s.split(' ')
    new_lst = []
    for element in lst:
        if '-' in element:
            inLst = element.split('-')
            start = int(inLst[0])
            end   = int(inLst[1])
            inLst = []
            for i in range(start, end + 1):
                inLst.append(str(i))

            inS = ' '.join(inLst)
            new_lst.append(inS)
        else:
            new_lst.append(element)

    s = ' '.join(new_lst)
    return s

def ConvertStrToListOfInt(st):
    """
    This function coverts string to list of integers.
    """
    st = ConvertToDlString(st)
    lstInt = []
    while st:
        intNumber = 0
        if ' ' in st:
            idx = st.index(' ')
            intNumber = int(st[:idx])
            st = st[idx+1:]
        else:
            intNumber = int(st)
            st = ''
        lstInt.append(intNumber)
    return lstInt

def CheckIfMethodOrTypeExists(modelClient, method_or_type, unitTestMode=False):
    """
    Check if SOAP method or type is present in your version of RFEM/RSTAB.
    Use it only in your examples.
    Unit tests except msg from SUDS where this is checked already.

    Args:
        modelClient (Model.clientModel)
        method_or_type (string): method or type of SOAP client

    Returns:
        bool: Status of method or type.

    Note:
        To get list of methods invoke:
        list_of_methods = [method for method in Model.clientModel.wsdl.services[0].ports[0]]
    """
    assert modelClient is not None, "WARNING: modelClient is not initialized."

    if method_or_type not in str(modelClient):
        if unitTestMode:
            return True
        else:
            assert False, "WARNING: Used method/type: %s is not implemented in Web Services yet." % (method_or_type)

    return not unitTestMode


def GetAddonStatus(modelClient, addOn = AddOn.stress_analysis_active):
    """
    Check if Add-on is reachable and active.
    For some types of objects, specific Add-ons need to be ennabled.

    Args:
        modelClient (Model.clientModel)
        method_or_type (string): method or type of SOAP client

    Returns:
        (bool): Status of Add-on
    """
    if modelClient is None:
        print("WARNING: modelClient is not initialized.")
        return False

    addons = modelClient.service.get_addon_statuses()
    dct = {}
    for lstType in addons:
        if not isinstance(lstType[1], bool) and len(lstType[1]) > 1:
            addon = [lst for lst in lstType[1]]
            for item in addon:
                dct[str(item[0])] = bool(item[1])
        elif isinstance(lstType[1], bool):
            dct[str(lstType[0])] = bool(lstType[1])
        else:
            assert False

    # sanity check
    assert addOn.name in dct, f"WARNING: {addOn.name} Add-on can not be reached."

    return dct[addOn.name]

def SetAddonStatus(modelClient, addOn = AddOn.stress_analysis_active, status = True):
    """
    Activate or deactivate Add-on.
    For some types of objects, specific Add-ons need to be ennabled.

    Analysis addOns list:
        material_nonlinear_analysis_active
        structure_stability_active
        construction_stages_active
        time_dependent_active
        form_finding_active
        cutting_patterns_active
        torsional_warping_active
        cost_estimation_active

    Design addOns list:
        stress_analysis_active
        concrete_design_active
        steel_design_active
        timber_design_active
        aluminum_design_active
        steel_joints_active
        timber_joints_active
        craneway_design_active

    Dynamic addOns list:
        modal_active
        spectral_active
        time_history_active
        pushover_active
        harmonic_response_active

    Special aadOns list:
        building_model_active
        wind_simulation_active
        geotechnical_analysis_active

    Args:
        modelClient (Model.clientModel)
        method_or_type (string): method or type of SOAP client
        status (bool): in/active
    """

    # this will also provide sanity check
    currentStatus = GetAddonStatus(modelClient, addOn)
    if currentStatus != status:
        addonLst = modelClient.service.get_addon_statuses()
        if addOn.name in addonLst['__keylist__']:
            addonLst[addOn.name] = status
        else:
            for listType in addonLst['__keylist__']:
                if not isinstance(addonLst[listType], bool) and addOn.name in addonLst[listType]:
                    addonLst[listType][addOn.name] = status

        modelClient.service.set_addon_statuses(addonLst)

def CalculateSelectedCases(loadCases: list = None, designSituations: list = None, loadCombinations: list = None):
    '''
    This method calculate just selected objects - load cases, desingSituations, loadCombinations
    Args:
        loadCases (list, optional): [description]. Defaults to None.
        designSituations (list, optional): [description]. Defaults to None.
        loadCombinations (list, optional): [description]. Defaults to None.
    '''
    specificObjectsToCalculate = Model.clientModel.factory.create('ns0:array_of_calculate_specific_objects_elements')
    if loadCases is not None:
        for loadCase in loadCases:
            specificObjectsToCalculateLC = Model.clientModel.factory.create('ns0:array_of_calculate_specific_objects_elements.element')
            specificObjectsToCalculateLC.no = loadCase
            specificObjectsToCalculateLC.parent_no = 0
            specificObjectsToCalculateLC.type = ObjectTypes.E_OBJECT_TYPE_LOAD_CASE.name
            specificObjectsToCalculate.element.append(specificObjectsToCalculateLC)

    if designSituations is not None:
        for designSituation in designSituations:
            specificObjectsToCalculateDS = Model.clientModel.factory.create('ns0:array_of_calculate_specific_objects_elements.element')
            specificObjectsToCalculateDS.no = designSituation
            specificObjectsToCalculateDS.parent_no = 0
            specificObjectsToCalculateDS.type = ObjectTypes.E_OBJECT_TYPE_DESIGN_SITUATION.name
            specificObjectsToCalculate.element.append(specificObjectsToCalculateDS)

    if loadCombinations is not None:
        for loadCombination in loadCombinations:
            specificObjectsToCalculateLC = Model.clientModel.factory.create('ns0:array_of_calculate_specific_objects_elements.element')
            specificObjectsToCalculateLC.no = loadCombination
            specificObjectsToCalculateLC.parent_no = 0
            specificObjectsToCalculateLC.type = ObjectTypes.E_OBJECT_TYPE_LOAD_CASE.name
            specificObjectsToCalculate.element.append(specificObjectsToCalculateLC)

    Model.clientModel.service.calculate_specific_objects(specificObjectsToCalculate)

def ExportResultTablesToCsv(TargetDirectoryPath: str):

    Model.clientModel.service.export_result_tables_to_csv(TargetDirectoryPath)

def ExportResultTablesToXML(TargetFilePath: str):

    Model.clientModel.service.export_result_tables_to_xml(TargetFilePath)

def ExportResultTablesWithDetailedMembersResultsToCsv(TargetDirectoryPath: str):

    Model.clientModel.service.export_result_tables_with_detailed_members_results_to_csv(TargetDirectoryPath)

def ExportResultTablesWithDetailedMembersResultsToXML(TargetFilePath: str):

    Model.clientModel.service.export_result_tables_with_detailed_members_results_to_xml(TargetFilePath)

def ParseCSVResultsFromSelectedFileToDict(filePath: str):

    # Using encoding parameter ensures proper data translation, leaving out BOM etc.
    # TODO: fix the value assigment; it only works with simple one-line header
    #       consider all corner cases
    with open(filePath, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f,delimiter=';')
        my_dictionary = []
        for line in reader:
            my_dictionary.append(line)
    return my_dictionary

def ParseXMLResultsFromSelectedFileToDict(filePath: str):

    with open(filePath, "rb") as f:
        my_dictionary = xmltodict.parse(f, xml_attribs=True)
    return my_dictionary

def GenerateMesh():

    Model.clientModel.service.generate_mesh()

def GetMeshStatistics():

    mesh_stats = Model.clientModel.service.get_mesh_statistics()
    return Model.clientModel.dict(mesh_stats)

def FirstFreeIdNumber(memType = ObjectTypes.E_OBJECT_TYPE_MEMBER, parent_no: int = 0):
    '''
    This method returns the next available Id Number for the selected object type
    Args:
        type (enum): Object Type
        parent_no (int): Object Parent Number
            Note:
            (1) A geometric object has, in general, a parent_no = 0
            (2) The parent_no parameter becomes significant for example with loads
    '''
    return Model.clientModel.service.get_first_free_number(memType.name, parent_no)

def SetModelType(model_type = ModelType.E_MODEL_TYPE_3D):
    '''
    This method sets the model type. The model type is E_MODEL_TYPE_3D by default.

    Args:
        model_type (enum): The available model types are listed below.
            ModelType.E_MODEL_TYPE_1D_X_3D
            ModelType.E_MODEL_TYPE_1D_X_AXIAL
            ModelType.E_MODEL_TYPE_2D_XY_3D
            ModelType.E_MODEL_TYPE_2D_XY_PLATE
            ModelType.E_MODEL_TYPE_2D_XZ_3D
            ModelType.E_MODEL_TYPE_2D_XZ_PLANE_STRAIN
            ModelType.E_MODEL_TYPE_2D_XZ_PLANE_STRESS
            ModelType.E_MODEL_TYPE_3D
    '''

    Model.clientModel.service.set_model_type(model_type.name)

def GetModelType():

    '''
    The method returns a string of the current model type.
    '''

    return Model.clientModel.service.get_model_type()
