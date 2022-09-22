from RFEM.initModel import Model,clearAttributes

class DesignSituation():
    def __init__(self,
                 no: int = 1,
                 user_defined_name: bool = False,
                 name = None,
                 active: bool = True,
                 design_situation_type: int = 6122,
                 comment: str = '',
                 params: dict = {}):

        """
        Args:
            no (int): Design Situation Tag
            user_defined_name (bool): Enable/Disable User-Defined Name
            name (str, optional): User-Defined Name (Applicable when user_defined_name = TRUE)
            active (bool): Enable/Disable Design Situation Activity
            design_situation_type (int): Design Situation Numeric Code (Variable key inputs, dependant on Standards defined in the model)
                Applicable to Standard Group EN 1990 with National Annex CEN | 2010-04 (See Model Base Data > Standards I)
                    6122 = ULS (EQU) - Permanent and transient,
                    6993 = ULS (EQU) - Accidental - psi-1,1,
                    6994 = ULS (EQU) - Accidental - psi-2,1,
                    6997 = ULS (EQU) - Seismic,
                    7007 = ULS (STR/GEO) - Permanent and transient - Eq. 6.10,
                    7008 = ULS (STR/GEO) - Permanent and transient - Eq. 6.10a and 6.10b,
                    7010 = ULS (STR/GEO) - Accidental - psi-1,1,
                    7011 = ULS (STR/GEO) - Accidental - psi-2,1,
                    7014 = ULS (STR/GEO) - Seismic,
                    6193 = SLS - Characteristic,
                    6194 = SLS - Frequent,
                    6195 = SLS - Quasi-permanent.
                Applicable to Standard Group EN 1990 with National Annex DIN | 2012-08 (See Model Base Data > Standards I)
                    6122 = ULS (EQU) - Permanent and transient,
                    6993 = ULS (EQU) - Accidental - psi-1,1,
                    6994 = ULS (EQU) - Accidental - psi-2,1,
                    6995 = ULS (EQU) - Accidental - Snow - psi-1,1,
                    6996 = ULS (EQU) - Accidental - Snow - psi-2,1,
                    6997 = ULS (EQU) - Seismic,
                    7007 = ULS (STR/GEO) - Permanent and transient - Eq. 6.10,
                    7010 = ULS (STR/GEO) - Accidental - psi-1,1,
                    7011 = ULS (STR/GEO) - Accidental - psi-2,1,
                    7012 = ULS (STR/GEO) - Accidental - Snow - psi-1,1,
                    7013 = ULS (STR/GEO) - Accidental - Snow - psi-2,1,
                    7014 = ULS (STR/GEO) - Seismic,
                    6193 = SLS - Characteristic,
                    6194 = SLS - Frequent,
                    6195 = SLS - Quasi-permanent.
            comment (str, optional): Comments
            params (dict, optional): Parameters
        """

        # Client model | Design Situation
        clientObject = Model.clientModel.factory.create('ns0:design_situation')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Design Situation No.
        clientObject.no = no

        # Design Situation Name
        clientObject.user_defined_name_enabled = user_defined_name
        if user_defined_name:
            if name is None:
                raise Exception('WARNING: A user defined design situation name was requested. As such, the name parameter cannot be empty.')
            clientObject.name = name

        # Design Situation Active
        clientObject.active = active

        # Design Situation Type
        clientObject.design_situation_type = design_situation_type

        # Design Situation Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Design Situation to client model
        Model.clientModel.service.set_design_situation(clientObject)
