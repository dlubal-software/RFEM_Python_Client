import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

import pytest
from RFEM.enums import SolidContactPerpendicularType, SolidContactParallelType
from RFEM.initModel import Model
from RFEM.TypesForSolids.solidGas import SolidGas
from RFEM.TypesForSolids.solidContact import SolidContact
from RFEM.TypesForSolids.solidMeshRefinement import SolidMeshRefinement

if Model.clientModel is None:
    Model()

def test_types_for_solids():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    SolidMeshRefinement(1, 0.23)

    SolidGas(1, 130000, 284)

    SolidContact(1, SolidContactPerpendicularType.FAILURE_UNDER_COMPRESSION, SolidContactParallelType.FAILURE_IF_CONTACT_PERPENDICULAR_TO_SURFACES_FAILED)
    SolidContact(2, SolidContactPerpendicularType.FAILURE_UNDER_TENSION, SolidContactParallelType.FULL_FORCE_TRANSMISSION)
    SolidContact(3, SolidContactPerpendicularType.FULL_FORCE_TRANSMISSION, SolidContactParallelType.RIGID_FRICTION, [2])
    SolidContact(4, SolidContactPerpendicularType.FAILURE_UNDER_COMPRESSION, SolidContactParallelType.RIGID_FRICTION_LIMIT, [10000000])
    SolidContact(5, SolidContactPerpendicularType.FAILURE_UNDER_COMPRESSION, SolidContactParallelType.ELASTIC_FRICTION, [510, 0.5])
    SolidContact(6, SolidContactPerpendicularType.FAILURE_UNDER_COMPRESSION, SolidContactParallelType.ELASTIC_FRICTION_LIMIT, [520, 11000000])
    SolidContact(7, SolidContactPerpendicularType.FAILURE_UNDER_COMPRESSION, SolidContactParallelType.ELASTIC_SOLID, [530])
    with pytest.raises(ValueError):
        SolidContact(8, SolidContactPerpendicularType.FAILURE_UNDER_TENSION, SolidContactParallelType.FULL_FORCE_TRANSMISSION, [0.15])

    Model.clientModel.service.finish_modification()

    solidMeshrefinement = Model.clientModel.service.get_solid_mesh_refinement(1)
    assert round(solidMeshrefinement.target_length, 3) == 0.23

    solidGas = Model.clientModel.service.get_solid_gas(1)
    assert solidGas.pressure == 130000
    assert round(solidGas.temperature) == 284

    contact = Model.clientModel.service.get_solid_contacts(1)
    assert contact.perpendicular_to_surface == SolidContactPerpendicularType.FAILURE_UNDER_COMPRESSION.name
    assert contact.parallel_to_surface == SolidContactParallelType.FAILURE_IF_CONTACT_PERPENDICULAR_TO_SURFACES_FAILED.name

    contact = Model.clientModel.service.get_solid_contacts(2)
    assert contact.perpendicular_to_surface == SolidContactPerpendicularType.FAILURE_UNDER_TENSION.name
    assert contact.parallel_to_surface == SolidContactParallelType.FULL_FORCE_TRANSMISSION.name

    contact = Model.clientModel.service.get_solid_contacts(3)
    assert contact.parallel_to_surface == SolidContactParallelType.RIGID_FRICTION.name
    assert round(contact.friction_coefficient, 2) == 2

    contact = Model.clientModel.service.get_solid_contacts(4)
    assert contact.parallel_to_surface == SolidContactParallelType.RIGID_FRICTION_LIMIT.name
    assert round(contact.limit_stress) == 10000000

    contact = Model.clientModel.service.get_solid_contacts(5)
    assert contact.parallel_to_surface == SolidContactParallelType.ELASTIC_FRICTION.name
    assert round(contact.shear_stiffness, 2) == 510
    assert round(contact.friction_coefficient, 2) == 0.5

    contact = Model.clientModel.service.get_solid_contacts(6)
    assert contact.parallel_to_surface == SolidContactParallelType.ELASTIC_FRICTION_LIMIT.name
    assert round(contact.shear_stiffness) == 520
    assert round(contact.limit_stress) == 11000000

    contact = Model.clientModel.service.get_solid_contacts(7)
    assert contact.parallel_to_surface == SolidContactParallelType.ELASTIC_SOLID.name
    assert round(contact.shear_stiffness) == 530
