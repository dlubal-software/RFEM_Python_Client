from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertStrToListOfInt
from RFEM.enums import NodalReleaseTypeAxialReleaseNonlinearity, NodalReleaseTypeDiagram
from RFEM.enums import NodalReleaseTypePartialActivityAlong, NodalReleaseTypePartialActivityAround
from RFEM.dataTypes import inf


class NodalReleaseType():
    def __init__(self,
                 no: int = 1,
                 coordinate_system: str = "Local",
                 member : str = "",
                 translational_release_n: float = inf,
                 translational_release_vy: float = inf,
                 translational_release_vz: float = inf,
                 rotational_release_mt: float = inf,
                 rotational_release_my: float = 0.0,
                 rotational_release_mz: float = 0.0,
                 translational_release_n_nonlinearity = [NodalReleaseTypeAxialReleaseNonlinearity.NONLINEARITY_TYPE_NONE],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
         Args:
            no (int): Node Tag
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        '''
        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:node')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Node No.
        clientObject.no = no

        # Nodal Release Typ
        clientObject.coordinate_system = coordinate_system

         # Translational Release/Spring [N/m] N
        clientObject.axial_release_n = translational_release_n

        # Translational Release/Spring [N/m] Vy
        clientObject.axial_release_vy = translational_release_vy

        # Translational Release/Spring [N/m] Vz
        clientObject.axial_release_vz = translational_release_vz

        # Rotational Release/Spring [Nm/rad] Mt
        clientObject.moment_release_mt = rotational_release_mt

        # Rotational Release/Spring [Nm/rad] My
        clientObject.moment_release_my = rotational_release_my

        # Rotational Release/Spring [Nm/rad] Mz
        clientObject.moment_release_mz = rotational_release_mz

        # Translational Release N Nonlinearity

        # Nonlinearity Types None, Fixed if Negative N, Fixed if Positive N
        if translational_release_n_nonlinearity[0].name == "NONLINEARITY_TYPE_NONE" \
        or translational_release_n_nonlinearity[0].name == "NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE" \
        or translational_release_n_nonlinearity[0].name == "NONLINEARITY_TYPE_FAILURE_IF_POSITIVE" :
            clientObject.axial_release_n_nonlinearity = translational_release_n_nonlinearity[0].name



        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Node to client model
        model.clientModel.service.set_node(clientObject)
