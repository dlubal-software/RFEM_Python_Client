import os
from RFEM.initModel import client, Model

def importFrom(targetFilePath: str):
    '''
    Allowed file extensions are .xml, .saf and .xlsx.

    Args:
        targetFilePath (string): Destination path to the file
    '''
    client.service.import_from(targetFilePath)
    head, tail = os.path.split(targetFilePath)
    if '.' in tail:
            tail = tail.split('.')[0]
    Model(False, tail)

def getConversionTables():
    '''
    Get conversion tables.
    '''
    return client.service.get_conversion_tables()

def setConversionTables(ConversionTables):
    '''
    Set conversion tables.

    Args:
        ConversionTables (ns0:ConversionTables): Conversion tables structure
    '''
    client.service.set_conversion_tables(ConversionTables)

def getSAFSettings():
    '''
    Get SAF import/export settings.
    '''
    return client.service.get_saf_settings()

def setSAFSettings(SafConfiguration):
    '''
    Set SAF import/export settings.

    Args:
        SafConfiguration (ns0:SafConfiguration) SAF settings obtained by getSAFSettings()
    '''
    client.service.set_saf_settings(SafConfiguration)