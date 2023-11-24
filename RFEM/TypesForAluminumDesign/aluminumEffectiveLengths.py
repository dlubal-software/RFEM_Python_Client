from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import AluminumEffectiveLengthsDeterminationMcrEurope

class AluminumEffectiveLengths():
    def __init__(self,
                 no: int = 1,
                 members: str = '1',
                 member_sets: str = '',
                 flexural_buckling_about_y: bool = True,
                 flexural_buckling_about_z: bool = True,
                 torsional_buckling: bool = True,
                 lateral_torsional_buckling: bool = True,
                 principal_section_axes: bool = True,
                 geometric_section_axes: bool = True,
                 name: str = 'SEL1',
                 intermediate_nodes: bool = False,
                 different_properties: bool = True,
                 factors_definition_absolute: bool = False,
                 import_from_stability_analysis_enabled: bool = False,
                 determination_of_mcr = AluminumEffectiveLengthsDeterminationMcrEurope.DETERMINATION_EUROPE_EIGENVALUE,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Aluminum Effective Length Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            flexural_buckling_about_y (bool): Flexural Buckling About Y Option
            flexural_buckling_about_z (bool): Flexural Buckling About Z Option
            torsional_buckling (bool): Torsional Buckling Option
            lateral_torsional_buckling (bool): Lateral Torsional Buckling Option
            principal_section_axes (bool): Principal Section Axes Option
            geometric_section_axes (bool): Geometric Section Axes Option
            name (str): User Defined Effective Length Name
            intermediate_nodes (bool): Intermediate Nodes Option
            different_properties (bool): Different Properties Option
            factors_definition_absolute (bool): Absolute Factors Definition Option
            import_from_stability_analysis_enabled (bool): Import From Stability Analysis Option
            determination_of_mcr (enum): Aluminum Effective Lengths Determination Mcr Europe Enumeration Item
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Types For Aluminum Design Effective Lengths
        clientObject = model.clientModel.factory.create('ns0:aluminum_effective_lengths')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Effective Lengths No.
        clientObject.no = no

        # Effective Lengths Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Effective Lengths Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Effective Lengths Flexural Buckling About Y
        clientObject.flexural_buckling_about_y = flexural_buckling_about_y

        # Effective Lengths Flexural Buckling About Z
        clientObject.flexural_buckling_about_z = flexural_buckling_about_z

        # Effective Lengths Torsional Buckling
        clientObject.torsional_buckling = torsional_buckling

        # Effective Lengths Lateral Torsional Buckling
        clientObject.lateral_torsional_buckling = lateral_torsional_buckling

        # Effective Lengths Principal Section Axes
        clientObject.principal_section_axes = principal_section_axes

        # Effective Lengths Geometric Section Axes
        clientObject.geometric_section_axes = geometric_section_axes

        # Effective Lengths User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Effective Lengths Intermediate Points
        clientObject.intermediate_nodes = intermediate_nodes

        # Effective Lengths Different Properties
        clientObject.different_properties = different_properties

        # Effective Lengths Factors Definition Absolute
        clientObject.factors_definition_absolute = factors_definition_absolute

        # Effective Lengths Import From Stability Analysis Enabled
        clientObject.import_from_stability_analysis_enabled = import_from_stability_analysis_enabled

        # Effective Lengths Determination MCR Europe
        clientObject.determination_mcr_europe = determination_of_mcr.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Aluminum Effective Lengths to client model
        model.clientModel.service.set_aluminum_effective_lengths(clientObject)
