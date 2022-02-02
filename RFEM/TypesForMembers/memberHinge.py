from RFEM.initModel import Model, clearAtributes
from RFEM.dataTypes import inf

class MemberHinge():
    def __init__(self,
                 no: int = 1,
                 coordinate_system: str = "Local",
                 translational_release_n: float = inf,
                 translational_release_vy: float = inf,
                 translational_release_vz: float = inf,
                 rotational_release_mt: float = inf,
                 rotational_release_my: float = 0.0,
                 rotational_release_mz: float = inf,
                 comment: str = 'Rotational Release My',
                 params: dict = {}):

        # Client model | Member Hinge
        clientObject = Model.clientModel.factory.create('ns0:member_hinge')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Memeber Hinge No.
        clientObject.no = no

        # Coordinate System
        clientObject.coordinate_system = coordinate_system

        # Translational Release/Spring [kN/m] N
        clientObject.axial_release_n = translational_release_n

        # Translational Release/Spring [kN/m] Vy
        clientObject.axial_release_vy = translational_release_vy

        # Translational Release/Spring [kN/m] Vz
        clientObject.axial_release_vz = translational_release_vz

        # Rotational Release/Spring [kNm/rad] Mt
        clientObject.moment_release_mt = rotational_release_mt

        # Rotational Release/Spring [kNm/rad] My
        clientObject.moment_release_my = rotational_release_my

        # Rotational Release/Spring [kNm/rad] Mz
        clientObject.moment_release_mz = rotational_release_mz

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_member_hinge(clientObject)
