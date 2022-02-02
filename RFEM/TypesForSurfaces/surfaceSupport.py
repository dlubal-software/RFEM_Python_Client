from RFEM.initModel import Model, ConvertToDlString, clearAtributes

class SurfaceSupport():
    def __init__(self,
                 no: int = 1,
                 surfaces_no: str = '1',
                 c_1_x: float = 0.0,
                 c_1_y: float = 0.0,
                 c_1_z: float = 0.0,
                 c_2_x: float = 0.0,
                 c_2_y: float = 0.0,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Surface Support
        clientObject = Model.clientModel.factory.create('ns0:surface_support')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Support No.
        clientObject.no = no

        # Surface No. (e.g. "5 6 7 12")
        clientObject.surfaces = ConvertToDlString(surfaces_no)

        # Surface Support Conditions
        clientObject.translation_x = c_1_x
        clientObject.translation_y = c_1_y
        clientObject.translation_z = c_1_z
        clientObject.shear_xz = c_2_x
        clientObject.shear_yz = c_2_y

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Surface Support to client model
        Model.clientModel.service.set_surface_support(clientObject)
