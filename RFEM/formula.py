from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes
from RFEM.enums import ObjectTypes, FormulaParameter

class Formula():

    def __init__(self,
                 object_type = ObjectTypes.E_OBJECT_TYPE_NODE,
                 object_no: int = 1,
                 attribute: str = 'coordinate_1',
                 formula: str = '2*3',
                 model = Model):
        '''
        Args:
            object_type (enum): Type of object for which parameters are searched where formulas are allowed
            object_no (int): Object number
            attribute (str): Attribute identificator
            formula (str): Formula in text format
            model (RFEM Class, optional): Model to be edited
        '''

        # Client model | Object Location
        lc = model.clientModel.factory.create('ns0:object_location')
        opl = model.clientModel.factory.create('ns0:object_parameter_location')

        lstOfAttributes = self.GetListOfParametersFormulaAllowedFor(object_type, object_no, model)

        # Check if attribute is valid
        if attribute not in lstOfAttributes:
            raise ValueError('WARNING: It is not allowed to insert a formula for attribute:"'+attribute+'.')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(lc)
        clearAttributes(opl)

        lc.type = object_type.name
        lc.no = object_no
        lc.parent_no = 0

        opl.attribute = attribute

        # Delete None attributes for improved performance
        deleteEmptyAttributes(lc)
        deleteEmptyAttributes(opl)

        # Add Formula to client model
        model.clientModel.service.set_formula(lc, opl, formula)


    @staticmethod
    def Get(object_type = ObjectTypes.E_OBJECT_TYPE_NODE,
            object_no: int = 1,
            attribute: str = 'coordinate_1',
            formula_param = FormulaParameter.FORMULA,
            model = Model):
        '''
        Args:
            object_type (enum): Type of object for which parameters are searched where formulas are allowed
            object_no (int): Object number
            attribute (str): Attribute identificator
            formula_param (enum): Formula parameters. You can choose from ALL, FORMULA, IS_VALID, CALCULATED_VALUE.
            model (RFEM Class, optional): Model to be edited
        Returns:
            Formula for given type, number and attribute according to chosen formula_param.
        '''

        # Client model | Object Location
        lc = model.clientModel.factory.create('ns0:object_location')
        opl = model.clientModel.factory.create('ns0:object_parameter_location')

        lstOfAttributes = Formula.GetListOfParametersFormulaAllowedFor(object_type, object_no, model)

        # Check if attribute is valid
        if attribute not in lstOfAttributes:
            raise ValueError('WARNING: For the attribute "'+attribute+'" the formula is not allowed.')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(lc)
        clearAttributes(opl)

        lc.type = object_type.name
        lc.no = object_no
        lc.parent_no = 0

        opl.attribute = attribute
        formulaDict = model.clientModel.service.get_formula(lc, opl)
        resultFormula = None

        # Return specific parameter of formula
        if formula_param == FormulaParameter.ALL:
            resultFormula = formulaDict
        elif formula_param == FormulaParameter.FORMULA:
            resultFormula = formulaDict['formula']
        elif formula_param == FormulaParameter.IS_VALID:
            resultFormula = formulaDict['is_valid']
        elif formula_param == FormulaParameter.CALCULATED_VALUE:
            resultFormula = formulaDict['calculated_value']
        else:
            raise ValueError("WARNING: Chosen formula_param doesn't exist.")

        return resultFormula

    @staticmethod
    def GetListOfParametersFormulaAllowedFor(
                     object_type = ObjectTypes.E_OBJECT_TYPE_NODE,
                     object_no: int = 1,
                     model = Model):
        '''
        Args:
            object_type (enum): Type of object for which parameters are searched where formulas are allowed
            object_no (int): Object number
            model (RFEM Class, optional): Model to be edited
        Returns:
            attr_lst (list): List of attriburtes for which formulas are allowed
        '''

        # Client model | Object Location
        clientObject = model.clientModel.factory.create('ns0:object_location')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

        clientObject.type = object_type.name
        clientObject.no = object_no
        clientObject.parent_no = 0
        lst = model.clientModel.service.get_list_of_parameters_formula_allowed_for(clientObject)

        attr_lst = []
        for i in lst[0]:
            attr_lst.append(i.attribute)

        return attr_lst
