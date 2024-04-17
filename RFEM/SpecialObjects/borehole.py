from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes

class Borehole:

    def __init__(self,
                 no: int = 1,
                 coordinates: list = [0.0, 0.0, 0.0],
                 groundwater: float = 0,
                 layers : list = [[1, 2.0], [2, 2.0], [3, 2.0]],
                 name: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        """
        Args:
            no (int): Borehole tag
            coordinates (list): Borehole Coordinate List
                coordinates = [coordinate_x, coordinate_y, coordinate_z]
            groundwater (float): Groundwater Ordinate
            layers (liast of lists): Soil Layers Table
                layers = [[soil_material_no(int), thickness(float)], ...]
            name (str, optional): User Defined Borehole Name
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Borehole
        clientObject = model.clientModel.factory.create('ns0:borehole')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Borehole No.
        clientObject.no = no

        # Coordinates
        clientObject.coordinate_0 = coordinates[0]
        clientObject.coordinate_1 = coordinates[1]
        clientObject.coordinate_2 = coordinates[2]

        # Groundater
        if groundwater:
            clientObject.groundwater = True
            clientObject.groundwater_ordinate = groundwater

        else:
            clientObject.groundwater = False

        # Soil Layer Table
        clientObject.layers_table = Model.clientModel.factory.create('ns0:borehole.layers_table')

        for i, j in enumerate(layers):
            sl = Model.clientModel.factory.create('ns0:borehole_layers_table_row')
            sl.no = i+1
            sl.row = Model.clientModel.factory.create('ns0:borehole_layers_table')
            clearAttributes(sl.row)
            sl.row.layer_no = i+1
            sl.row.soil_material = layers[i][0]
            sl.row.thickness = layers[i][1]

            clientObject.layers_table.borehole_layers_table.append(sl)

        # User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Nodal Support to client model
        model.clientModel.service.set_borehole(clientObject)

    @staticmethod
    def GetBorehole(object_index: int = 1, model = Model):

        '''
        Args:
            obejct_index (int): Borehole Index
            model (RFEM Class, optional): Model to be edited
        '''

        # Get Node from client model
        return model.clientModel.service.get_borehole(object_index)
