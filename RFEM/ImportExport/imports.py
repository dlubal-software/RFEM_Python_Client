import os
import sys
# In order to use connectionGlobals we need to adjust the sys path
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.clear()
sys.path.append(PROJECT_ROOT)
from RFEM.initModel import Model
from RFEM import connectionGlobals

def importFrom(targetFilePath: str):
    '''
    Allowed file extensions are .xml, .saf and .xlsx.

    Args:
        targetFilePath (string): Destination path to the file
    '''
    connectionGlobals.client.service.import_from(targetFilePath)
    head, tail = os.path.split(targetFilePath)
    if '.' in tail:
            tail = tail.split('.')[0]
    Model(False, tail)

def getConversionTables():
    '''
    Get conversion tables.
    '''
    return connectionGlobals.client.service.get_conversion_tables()

def setConversionTables(ConversionTables):
    '''
    Set conversion tables.

    Args:
        ConversionTables (ns0:ConversionTables): Conversion tables structure
    '''
    connectionGlobals.client.service.set_conversion_tables(ConversionTables)

def getSAFSettings():
    '''
    Get SAF import/export settings.
    '''
    return connectionGlobals.client.service.get_saf_settings()

def setSAFSettings(SafConfiguration):
    '''
    Set SAF import/export settings.

    Args:
        SafConfiguration (ns0:SafConfiguration) SAF settings obtained by getSAFSettings()
    '''
    connectionGlobals.client.service.set_saf_settings(SafConfiguration)