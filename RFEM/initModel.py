import sys

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

# Instantiate SOAP client model
cModel = modelLst = None
try:
    modelLst = client.service.get_model_list()
except:
    print('Error: Please check if all RFEM dialogs are closed.')
    input('Press Enter to exit...')
    sys.exit()

if modelLst:
    new = client.service.get_active_model() + 'wsdl'
    cModel = Client(new)
    print('Resetting model...')
    cModel.service.delete_all_results()
    cModel.service.reset()
else:
    new = client.service.new_model('My Model') + 'wsdl'
    cModel = Client(new)

# Init client model
clientModel = cModel


def clearAtributes(obj):
    '''
    Clears object atributes
    Sets all atributes to None

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
    Calculates model

    Params:
    - generateXmlSolverInput: generate XML solver input
    '''

    clientModel.service.calculate_all(generateXmlSolverInput)
