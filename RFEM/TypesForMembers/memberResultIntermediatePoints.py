from RFEM.initModel import Model, clearAttributes, ConvertToDlString, deleteEmptyAttributes

class MemberResultIntermediatePoint():
    def __init__(self,
                 no: int = 1,
                 members: str = "",
                 point_count: int = 2,
                 uniform_distribution: bool = True,
                 distances = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Member Result Intermediate Point Tag
            members (str): Assigned Members
            point_count (int): Assigned Point Number
            uniform_distribution (bool): Uniform Distrubition Option
            distances (list of lists): Distances Table
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Member Result Intermediate Point
        clientObject = model.clientModel.factory.create('ns0:member_result_intermediate_point')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Member Result Intermediate Point No.
        clientObject.no = no

        # Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Point Count
        clientObject.uniform_distribution = uniform_distribution
        if uniform_distribution:
            clientObject.point_count = point_count

        else:
            clientObject.distances = Model.clientModel.factory.create('ns0:member_result_intermediate_point.distances')

            for i,j in enumerate(distances):
                mlvlp = Model.clientModel.factory.create('ns0:member_result_intermediate_point_distances_row')
                mlvlp.no = i+1
                mlvlp.row.value = distances[i][0]
                mlvlp.row.note = None

                clientObject.distances.member_result_intermediate_point_distances.append(mlvlp)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Member Result Intermediate Point to client model
        model.clientModel.service.set_member_result_intermediate_point(clientObject)
