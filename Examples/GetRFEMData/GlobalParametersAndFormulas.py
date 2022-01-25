import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.initModel import Model, CheckIfMethodOrTypeExists
from RFEM.enums import ObjectTypes

if __name__ == "__main__":

    Model()
    CheckIfMethodOrTypeExists(Model.clientModel,'ns0:object_location')
    CheckIfMethodOrTypeExists(Model.clientModel,'ns0:object_parameter_location_type')
    CheckIfMethodOrTypeExists(Model.clientModel,'ns0:object_parameter_location_type.parameter_path_in_nested_models_hierarchy')
    CheckIfMethodOrTypeExists(Model.clientModel,'ns0:object_parameter_location_type.parameter_path_in_nested_models_hierarchy.node')
    CheckIfMethodOrTypeExists(Model.clientModel,'get_formula')

    objectLocation = Model.clientModel.factory.create('ns0:object_location')
    objectLocation.type = ObjectTypes.E_OBJECT_TYPE_SECTION.name
    objectLocation.no = 1
    objectLocation.parent_no = 0

    objectParameterLocation = Model.clientModel.factory.create('ns0:object_parameter_location_type')
    objectParameterLocation.attribute = "parametrization"
    parameterPathInNestedModelsHierarchy = Model.clientModel.factory.create('ns0:object_parameter_location_type.parameter_path_in_nested_models_hierarchy')
    parameterPathInNestedModelsHierarchyNode = Model.clientModel.factory.create('ns0:object_parameter_location_type.parameter_path_in_nested_models_hierarchy.node')
    parameterPathInNestedModelsHierarchyNode.row_path =  "0, 0"
    parameterPathInNestedModelsHierarchyNode.column_string_id = "section_parameter_value"
    parameterPathInNestedModelsHierarchy.node = parameterPathInNestedModelsHierarchyNode
    objectParameterLocation.parameter_path_in_nested_models_hierarchy = parameterPathInNestedModelsHierarchy

    formula = Model.clientModel.service.get_formula(objectLocation, objectParameterLocation)

    print('formula: ' + formula.formula)
    print('Calculated value: ' + str(formula.calculated_value))
    print('Validation results: ' + formula.validation_result)
