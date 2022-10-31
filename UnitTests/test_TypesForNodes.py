import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

import pytest
from RFEM.enums import NodalMeshRefinementType, NodalSupportType
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.thickness import Thickness
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForNodes.nodalMeshRefinement import NodalMeshRefinement, FElengthArrangement
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.dataTypes import inf


if Model.clientModel is None:
    Model()

def test_typesForNodes():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Thickness(1, 'Thick', 1, 0.35)

    Node(1, 0, 0, 0)
    Node(2, 5, 0, 0)
    Node(3, 5, 5, 0)
    Node(4, 0, 5, 0)
    Node(5,2.5,2.5,-2.5)

    NodalSupport(1, '1 2', [inf, inf, inf, 0.0, 0.0, inf])
    NodalSupport(2, '3', NodalSupportType.FIXED)
    NodalSupport(3, '4', NodalSupportType.ROLLER_IN_X)
    with pytest.raises(ValueError):
        NodalSupport(4, '5', [inf, inf, inf, 0.0])

    NodalMeshRefinement(1, NodalMeshRefinementType.TYPE_CIRCULAR, [2.2, 0.1, 0.5, FElengthArrangement.LENGTH_ARRANGEMENT_RADIAL])
    NodalMeshRefinement.Circular(2, 3)
    NodalMeshRefinement.Rectangular(3, 2.7)
    Model.clientModel.service.finish_modification()

    nodalSupport = Model.clientModel.service.get_nodal_support(1)
    assert nodalSupport.spring_x == inf
    assert nodalSupport.spring_y == inf
    assert nodalSupport.spring_z == inf
    assert nodalSupport.rotational_restraint_x == 0
    assert nodalSupport.rotational_restraint_y == 0
    assert nodalSupport.rotational_restraint_z == inf

    nodalSupport = Model.clientModel.service.get_nodal_support(2)
    assert nodalSupport.spring_x == inf
    assert nodalSupport.spring_y == inf
    assert nodalSupport.spring_z == inf
    assert nodalSupport.rotational_restraint_x == inf
    assert nodalSupport.rotational_restraint_y == inf
    assert nodalSupport.rotational_restraint_z == inf

    nodalSupport = Model.clientModel.service.get_nodal_support(3)
    assert nodalSupport.spring_x == 0
    assert nodalSupport.spring_y == inf
    assert nodalSupport.spring_z == inf
    assert nodalSupport.rotational_restraint_x == 0
    assert nodalSupport.rotational_restraint_y == 0
    assert nodalSupport.rotational_restraint_z == inf

    nodalMeshRefinement = Model.clientModel.service.get_nodal_mesh_refinement(1)
    assert nodalMeshRefinement.circular_radius == 2.2

    nodalMeshRefinement = Model.clientModel.service.get_nodal_mesh_refinement(2)
    assert nodalMeshRefinement.circular_radius == 3

    nodalMeshRefinement = Model.clientModel.service.get_nodal_mesh_refinement(3)
    assert nodalMeshRefinement.rectangular_side == 2.7
