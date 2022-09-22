from RFEM.initModel import Model, clearAttributes

class SurfaceResultsAdjustment():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Surface Result Adjustment
        clientObject = Model.clientModel.factory.create('ns0:surface_results_adjustment')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Result Adjustment No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface Result Adjustmentto client model
        Model.clientModel.service.set_surface_results_adjustment(clientObject)
