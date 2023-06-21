from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import DesignSituationType

class DesignSituation():

    def __init__(self,
                 no: int = 1,
                 design_situation_type = DesignSituationType.DESIGN_SITUATION_TYPE_A_ACCIDENTAL,
                 active: bool = True,
                 name = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        """
        Args:
            no (int): Design Situation Tag
            design_situation_type (enum): Design Situation Type Enumeration
            active (bool): Enable/Disable Design Situation Activity
            name (str, optional): User-Defined Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Design Situation
        clientObject = model.clientModel.factory.create('ns0:design_situation')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Design Situation No.
        clientObject.no = no

        # Design Situation Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Design Situation Active
        clientObject.active = active

        # Design Situation Type
        clientObject.design_situation_type = design_situation_type.name

        # Design Situation Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Design Situation to client model
        model.clientModel.service.set_design_situation(clientObject)
