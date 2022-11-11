from RFEM.initModel import Model, clearAttributes
from RFEM.dataTypes import inf

class LineHinge():
    # Slab Wall Connection definition
    slabWallConnection = {'slab_wall_connection': True,
                          'slab_wall_with_slab_edge_block': True,
                          'slab_wall_connection_offset': 0.15,
                          'slab_edge_block_width':0.1}

    def __init__(self,
                 no: int = 1,
                 assigned_to: str = '3/5; 2/5',
                 translational_release: list = [800, inf, inf],
                 rotational_release_phi: int = inf,
                 comment: str = '',
                 params: dict = {}):

        """
        assigned_to doesn't work. Can't figure why.
        Assignment in surfaces also doesn't work (surface.has_line_hinges = True).
        """

        # Client model | Line Hinge
        clientObject = Model.clientModel.factory.create('ns0:line_hinge')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Line Hinge No.
        clientObject.no = no

        # Assigned to surface and its line (format 1/3)
        clientObject.assigned_to = assigned_to

        # Translatioonal and totational release
        clientObject.translational_release_u_x = translational_release[0]
        clientObject.translational_release_u_y = translational_release[1]
        clientObject.translational_release_u_z = translational_release[2]
        clientObject.rotational_release_phi_x = rotational_release_phi

        # Slab connection
        clientObject.slab_wall_connection = False

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line Hinge to client model
        Model.clientModel.service.set_line_hinge(clientObject)

