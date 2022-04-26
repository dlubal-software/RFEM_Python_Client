from RFEM.initModel import Model

def GetDesignOverview(model = Model):
    '''
    Returns whole Design Overview list.
    '''
    # Return Design Overview
    return model.clientModel.service.get_design_overview()

def GetPartialDesignOverview(comply: bool = False):
    """
    Returns part of Design Overview that do(esn't) comply.
    If comply == False, function resturns checks with Design Ration > 1
    If comply == True, function resturns checks with Design Ration  <= 1
    """
    designOverview = GetDesignOverview()

    designRatioLessThanOne = []
    designRationOverOne = []
    for do in designOverview[0]:
        if round(do['design_ratio'], 5) <= 1.0:
            designRatioLessThanOne.append(do)
        else:
            designRationOverOne.append(do)

    if comply:
        return designRatioLessThanOne
    else:
        return designRationOverOne


