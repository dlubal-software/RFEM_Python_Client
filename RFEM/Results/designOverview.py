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
        if round(do.row['design_ratio'], 5) <= 1.0:
            designRatioLessThanOne.append(do[0])
        else:
            designRationOverOne.append(do[0])

    if comply:
        return designRatioLessThanOne
    else:
        return designRationOverOne


