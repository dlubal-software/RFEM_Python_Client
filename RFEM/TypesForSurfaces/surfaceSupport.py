from RFEM.initModel import Model, ConvertToDlString, clearAttributes, deleteEmptyAttributes
from RFEM.dataTypes import inf

class SurfaceSupport():
    def __init__(self,
                 no: int = 1,
                 surfaces_no: str = '1',
                 c_ux: float = 10000.0,
                 c_uy: float = 0.0,
                 c_uz: float = inf,
                 c_vxz: float = inf,
                 c_vyz: float = inf,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Surface Support

        Args:
            no (int): Surface Support Tag
            surfaces_no (str): Assigned to Surfaces
            c_ux (float): Translational Support in X direction
            c_uy (float): Translational Support in Y direction
            c_uz (float): Translational Support in Z direction
            c_vxz (float): Shear Support in XZ direction
            c_vyz (float): Shear Support in YZ direction
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Surface Support
        clientObject = model.clientModel.factory.create('ns0:surface_support')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Surface Support No.
        clientObject.no = no

        # Surface No. (e.g. "5 6 7 12")
        clientObject.surfaces = ConvertToDlString(surfaces_no)

        # Surface Support Conditions
        clientObject.translation_x = c_ux
        clientObject.translation_y = c_uy
        clientObject.translation_z = c_uz
        clientObject.shear_xz = c_vxz
        clientObject.shear_yz = c_vyz

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Surface Support to client model
        model.clientModel.service.set_surface_support(clientObject)
