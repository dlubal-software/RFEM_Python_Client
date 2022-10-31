import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

import pytest
from RFEM.dataTypes import inf
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model
from RFEM.enums import SurfaceStiffnessModificationType
from RFEM.TypesForSurfaces.surfaceSupport import SurfaceSupport
from RFEM.TypesForSurfaces.surfaceEccentricity import SurfaceEccentricity
from RFEM.TypesForSurfaces.surfaceStiffnessModification import SurfaceStiffnessModification
from RFEM.TypesForSurfaces.surfaceMeshRefinements import SurfaceMeshRefinement


if Model.clientModel is None:
    Model()

def test_types_for_surfaces():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Thickness
    Thickness(1, '1', 1, 0.01)

    # Create Nodes
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 0.0, 2.0, 0.0)
    Node(3, 2.0, 2.0, 0.0)
    Node(4, 2.0, 0.0, 0.0)
    Node(5, 0.0, 4.0, 0.0)
    Node(6, 2.0, 4.0, 0.0)

    Node(7, 5, 0, 0)
    Node(8, 7, 0, 0)
    Node(9, 5, 0, 2)
    Node(10, 7, 0, 2)
    Node(11, 5, 0, -2)
    Node(12, 7, 0, -2)

    # Create Lines
    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line(5, '2 5')
    Line(6, '5 6')
    Line(7, '6 3')

    Line(8, '9 7')
    Line(9, '7 8')
    Line(10, '8 10')
    Line(11, '10 9')
    Line(12, '8 12')
    Line(13, '12 11')
    Line(14, '11 7')

    # Create Surfaces
    Surface(1, '1 2 3 4', 1)
    Surface(2, '2 5 6 7', 1)

    Surface(3, '8 9 10 11', 1)
    Surface(4, '12 13 14 9', 1)

    # Surface Support
    SurfaceSupport()

    # Surface Eccentricities
    SurfaceEccentricity(1, 0.15, '')

    # Surface Stiffness Modification
    SurfaceStiffnessModification(1, SurfaceStiffnessModificationType.TYPE_TOTAL_STIFFNESS_FACTOR, factors=[1.09])
    SurfaceStiffnessModification(2, SurfaceStiffnessModificationType.TYPE_PARTIAL_STIFFNESSES_FACTORS, factors=[1.01, 1.02, 1.03, 1.04, 1.05])
    SurfaceStiffnessModification(3, SurfaceStiffnessModificationType.TYPE_STIFFNESS_MATRIX_ELEMENTS_FACTORS, factors=[1.09])
    SurfaceStiffnessModification(4, SurfaceStiffnessModificationType.TYPE_STIFFNESS_MATRIX_ELEMENTS_FACTORS, factors=[1, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.20])
    with pytest.raises(IndexError):
        SurfaceStiffnessModification(4, SurfaceStiffnessModificationType.TYPE_STIFFNESS_MATRIX_ELEMENTS_FACTORS, factors=[1, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17])

    # Surface Mesh Refinements
    SurfaceMeshRefinement()

    Model.clientModel.service.finish_modification()

    surfaceSupport = Model.clientModel.service.get_surface_support(1)
    assert surfaceSupport.translation_x == 10000
    assert surfaceSupport.translation_z == inf

    surfaceEccentricity = Model.clientModel.service.get_surface_eccentricity(1)
    assert surfaceEccentricity.transverse_offset_reference_type == 'TRANSVERSE_OFFSET_TYPE_FROM_SURFACE_THICKNESS'
    assert surfaceEccentricity.transverse_offset_reference_surface == 1

    surfaceStiffnessModification1 = Model.clientModel.service.get_surface_stiffness_modification(2)
    assert surfaceStiffnessModification1.factor_of_shear_stiffness == 1.02
    assert surfaceStiffnessModification1.factor_of_weight == 1.05

    surfaceStiffnessModification2 = Model.clientModel.service.get_surface_stiffness_modification(3)
    assert surfaceStiffnessModification2.kd11 == 1.09
    assert surfaceStiffnessModification2.kd38 == 1.09

    surfaceStiffnessModification3 = Model.clientModel.service.get_surface_stiffness_modification(4)
    assert surfaceStiffnessModification3.kd11 == 1
    assert surfaceStiffnessModification3.kd38 == 1.2

    surfaceMeshRefinement = Model.clientModel.service.get_surface_mesh_refinement(1)
    assert surfaceMeshRefinement.surfaces == '1'
    assert round(surfaceMeshRefinement.target_length, 2) == 0.2

