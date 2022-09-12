import sys
import RSECTION.dependencies
import requests
from suds.client import Client
from RSECTION.enums import *
from RSECTION.suds_requests import RequestsTransport

# Connect to server
# Check server port range set in "Program Options & Settings"
# By default range is set between 8101 ... 8109
print('Connecting to server...')
try:
    client = Client('http://localhost:8101/wsdl')
except:
    print('Error: Connection to server failed!')
    print('Please check:')
    print('- If you have started RSECTION application')
    print('- If all RSECTION dialogs are closed')
    print('- If server port range is set correctly')
    print('- If you have a valid Web Services license')
    print('- Check Program Options & Settings > Web Services')
    sys.exit()

try:
    modelLst = client.service.get_model_list()
except:
    print('Error: Please check if all RSECTION dialogs are closed.')
    input('Press Enter to exit...')
    sys.exit()

# Persistent connection
# Next 4 lines enables Client to work within 1 session which is much faster to execute.
# Without it the session lasts only one request which results in poor performance.
# Assigning session to application Client (here client) instead of model Client
# results also in poor performace.
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=1, pool_maxsize=1)
session.mount('http://', adapter)
trans = RequestsTransport(session)

class Model():
    clientModel = None
    clientModelLst = []
    activeSession = False

    def __init__(self,
                 new_model: bool=True,
                 model_name: str="TestModel",
                 delete: bool=False,
                 delete_all: bool=False):
        """
        Class object representing individual model in RSECTION.
        Class enables to edit multiple models in one session through holding.
        one transport session active by not setting 'trans' into Client.
        Args:
            new_model (bool, optional): Set to True if new model is requested.
            model_name (str, optional): Defaults to "TestModel".
            delete (bool, optional):  Delete results
            delete_all (bool, optional): Delete all objects in Model.
        """

        cModel = None
        modelLs = client.service.get_model_list()

        if new_model:
            if modelLs and model_name in modelLs.name:
                modelIndex = 0
                for i,j in enumerate(modelLs.name):
                    if modelLs.name[i] == model_name:
                        modelIndex = i
                new = client.service.get_model(modelIndex) + 'wsdl'
                # Set transport parameter if it is the first model
                if Model.activeSession:
                    cModel = Client(new)
                else:
                    cModel = Client(new, transport=trans)
                cModel.service.delete_all_results()
                cModel.service.delete_all()
            else:
                new = client.service.new_model(model_name) + 'wsdl'
                if Model.activeSession:
                    cModel = Client(new)
                else:
                    cModel = Client(new, transport=trans)
                if not modelLs:
                    Model.activeSession = True
        else:
            modelIndex = 0
            for i,j in enumerate(modelLs.name):
                if modelLs.name[i] == model_name:
                    modelIndex = i
            new = client.service.get_model(modelIndex) + 'wsdl'
            if Model.activeSession:
                cModel = Client(new)
            else:
                cModel = Client(new, transport=trans)
            if delete:
                print('Deleting results...')
                cModel.service.delete_all_results()
            if delete_all:
                print('Delete all...')
                cModel.service.delete_all()

        # when using multiple intances/model
        self.clientModel = cModel
        if not modelLs or not model_name in modelLs.name:
            Model.clientModelLst.append(cModel)
        # when using only one instace/model
        Model.clientModel = cModel



    def __delete__(self, index):
        if len(self.clientModelLst) == 1:
            self.clientModelLst.clear()
            self.clientModel = None
        else:
            self.clientModelLst.pop(index)
            self.clientModel = self.clientModelLst[-1]

def clearAtributes(obj):
    '''
    Clears object atributes.
    Sets all atributes to None.

    Args:
        obj: object to clear
    '''

    # iterator
    it = iter(obj)
    for i in it:
        obj[i[0]] = None
    return obj

def closeModel(index_or_name, save_changes = False):
    """
    Close any model with index or name. Be sure to close the first created
    model last (2,1, and then 0). 0 index carries whole session.

    Args:
        index_or_name : Model Index or Name to be Close
        save_changes (bool): Enable/Diable Save Changes Option
    """
    if isinstance(index_or_name, int):
        client.service.close_model(index_or_name, save_changes)
        Model.__delete__(Model, index_or_name)
    elif isinstance(index_or_name, str):
        modelLs = client.service.get_model_list()
        for i,j in enumerate(modelLs.name):
            if modelLs.name[i] == index_or_name:
                client.service.close_model(i, save_changes)
    else:
        assert False, 'Parameter index_or_name must be int or string.'

def insertSpaces(lst: list):
    '''
    Add spaces between list of numbers.
    Returns list of values.
    '''
    return ' '.join(str(item) for item in lst)

def Calculate_all(generateXmlSolverInput: bool = False, model = Model):
    '''
    Calculates model.
    CAUTION: Don't use it in unit tests!
    It works when executing tests individualy but when running all of them
    it causes RSECTION to stuck and generates failures, which are hard to investigate.

    Args:
        generateXmlSolverInput (bool): Generate XML Solver Input
        model (RSECTION Class, optional): Model to be edited
    '''
    model.clientModel.service.calculate_all(generateXmlSolverInput)

def ConvertToDlString(s):
    '''
    The function converts strings commonly used in RSTAB / RFEM / RSECTION so that they
    can be used In WebServices. It solved issue #4.
    Examples:
    '1,3'       -> '1 3'
    '1, 3'      -> '1 3'
    '1-3'       -> '1 2 3'
    '1,3,5-9'   -> '1 3 5 6 7 8 9'

    Args:
        s (str): RSTAB / RFEM / RSECTION Common String

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
    Args:
        st (str): RSTAB / RFEM / RSECTION Common String
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
    Check if SOAP method or type is present in your version of RFEM/RSTAB/RSECTION.
    Use it only in your examples.
    Unit tests except msg from SUDS where this is checked already.

    Args:
        modelClient (Model.clientModel)
        method_or_type (str): Method or Type of SOAP Client
        unitTestMode (bool): Unit Test Mode

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
