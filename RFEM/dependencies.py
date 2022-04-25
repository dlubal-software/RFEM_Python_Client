import sys

# Check Python version
if not sys.version_info[0] == 3:
    print('Must be using Python 3!')
    input('Press Enter to exit...')
    sys.exit()

# Check all dependencies
try:
    import requests
    import six
    import xmltodict
    import pytest
    import mock
    import suds.transport
    import suds.client # suds-py3
except:
    print('One of the required modules is not installed in your Python env.')
    instSUDS = input('\nDo you want to install all dependencies and check all their versions (y/n)? ')
    instSUDS = instSUDS.lower()
    if instSUDS == 'y':
        # Subprocess will be opened in cmd and closed automaticaly after installation.
        # Prevents invoking pip by an old script wrapper (https://github.com/pypa/pip/issues/5599)
        import subprocess
        try:
            subprocess.call('python -m pip install --upgrade pip')
            subprocess.call('python -m pip install requests six suds-py3 xmltodict pytest mock --user')
        except:
            print('WARNING: Installation of modules failed!')
            print('Please use command "python -m pip install requests six suds-py3 xmltodict pytest mock --user" in your Command Prompt.')
            input('Press Enter to exit...')
            sys.exit()
    else:
        input('Press Enter to exit...')
        sys.exit()