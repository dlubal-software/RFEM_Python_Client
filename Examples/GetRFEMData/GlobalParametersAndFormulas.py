import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.Loads.surfaceLoad import SurfaceLoad
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.BasicObjects.solidSet import SolidSet
from RFEM.BasicObjects.surfaceSet import SurfaceSet
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.BasicObjects.lineSet import LineSet
from RFEM.BasicObjects.opening import Opening
from RFEM.BasicObjects.solid import Solid
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.thickness import Thickness 
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
from RFEM.initModel import *
from RFEM.enums import *

if __name__ == "__main__":
    
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
    formula = Model.clientModel.service.get_formula(objectLocation,objectParameterLocation)
    print('formula: ' + formula.formula)
    print('Calculated value: ' + str(formula.calculated_value))
    print('Validation results: ' + formula.validation_result)

