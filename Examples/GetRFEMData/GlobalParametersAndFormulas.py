import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.Loads.surfaceLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.nodalLoad import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.BasicObjects.solidSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.material import *
from RFEM.initModel import *
from RFEM.dataTypes import *
from RFEM.enums import *


if __name__ == "__main__":

    objectLocation = clientModel.factory.create('ns0:object_location')
    objectLocation.type = ObjectTypes.E_OBJECT_TYPE_SECTION.name
    objectLocation.no = 1
    objectLocation.parent_no = 0

    objectParameterLocation = clientModel.factory.create('ns0:object_parameter_location_type')
    objectParameterLocation.attribute = "parametrization"
    parameterPathInNestedModelsHierarchy = clientModel.factory.create('ns0:object_parameter_location_type.parameter_path_in_nested_models_hierarchy')
    parameterPathInNestedModelsHierarchyNode = clientModel.factory.create('ns0:object_parameter_location_type.parameter_path_in_nested_models_hierarchy.node')
    parameterPathInNestedModelsHierarchyNode.row_path =  "0, 0"
    parameterPathInNestedModelsHierarchyNode.column_string_id = "section_parameter_value"
    parameterPathInNestedModelsHierarchy.node = parameterPathInNestedModelsHierarchyNode
    objectParameterLocation.parameter_path_in_nested_models_hierarchy = parameterPathInNestedModelsHierarchy
    formula = clientModel.service.get_formula(objectLocation,objectParameterLocation)
    print('formula: ' + formula.formula)
    print('Calculated value: ' + str(formula.calculated_value))
    print('Validation results: ' + formula.validation_result)

