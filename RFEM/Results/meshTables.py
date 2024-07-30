from RFEM.initModel import Model
from RFEM.Results.resultTables import ConvertResultsToListOfDct
from RFEM.enums import CaseObjectType

class MeshTables():

    @staticmethod
    def GetAllFENodes(
        include_base: bool = False,
        model = Model):
        '''
        Args:
            model (class, optional): Model instance
        '''
        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_nodes_original_mesh(), include_base)

    @staticmethod
    def GetAllFE1DElements(
        include_base: bool = False,
        model = Model):
        '''
        Args:
            model (class, optional): Model instance
        '''
        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_1D_elements(), include_base)

    @staticmethod
    def GetAllFE2DElements(
        include_base: bool = False,
        model = Model):
        '''
        Args:
            model (class, optional): Model instance
        '''
        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_2D_elements(), include_base)

    @staticmethod
    def GetAllFE3DElements(
        include_base: bool = False,
        model = Model):
        '''
        Args:
            model (class, optional): Model instance
        '''
        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_3D_elements(), include_base)

    @staticmethod
    def GetFENodeOriginalMesh(
        nodeNo: int = 1,
        model = Model):
        '''
        Args:
            nodeNo (int): Node Number
            model (class, optional): Model instance
        '''

        return model.clientModel.service.get_FE_node_original_mesh(nodeNo)

    @staticmethod
    def GetFE1DElement(
        elementNo: int = 1,
        model = Model):
        '''
        Args:
            elementNo (int): Element Number
            model (class, optional): Model instance
        '''

        return model.clientModel.service.get_FE_1D_element(elementNo)

    @staticmethod
    def GetFE2DElement(
        elementNo: int = 1,
        model = Model):
        '''
        Args:
            elementNo (int): Element Number
            model (class, optional): Model instance
        '''

        return model.clientModel.service.get_FE_2D_element(elementNo)

    @staticmethod
    def GetFE3DElement(
        elementNo: int = 1,
        model = Model):
        '''
        Args:
            elementNo (int): Element Number
            model (class, optional): Model instance
        '''

        return model.clientModel.service.get_FE_3D_element(elementNo)

    @staticmethod
    def GetAllFENodesInitialState(
        loading_type = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        increment_number: int = 1,
        include_base: bool = False,
        model = Model):
        '''
        Args:
            loading_type (emun): Case Object Loading Type Enumeration
            loading_no (int): Loading Number
            increment_number (int): Increment Number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_nodes_initial_state_mesh({'case_object': {'type': loading_type.name, 'id': loading_no}, 'increment_number': increment_number}), include_base)

    @staticmethod
    def GetAllFENodesDeformed(
        loading_type = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        increment_number: int = 1,
        include_base: bool = False,
        model = Model):
        '''
        Args:
            loading_type (emun): Case Object Loading Type Enumeration
            loading_no (int): Loading Number
            increment_number (int): Increment Number
            model (class, optional): Model instance
        '''

        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_nodes_deformed_mesh({'case_object': {'type': loading_type.name, 'id': loading_no}, 'increment_number': increment_number}), include_base)

    @staticmethod
    def GetFENodeInitialState(
        nodeNo:int = 1,
        loading_type = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        increment_number: int = 1,
        model = Model):
        '''
        Args:
            nodeNo (int): Node Number
            loading_type (emun): Case Object Loading Type Enumeration
            loading_no (int): Loading Number
            increment_number (int): Increment Number
            model (class, optional): Model instance
        '''

        return model.clientModel.service.get_FE_node_initial_state_mesh(nodeNo, {'case_object': {'type': loading_type.name, 'id': loading_no}, 'increment_number': increment_number})

    @staticmethod
    def GetFENodeDeformed(
        nodeNo:int = 1,
        loading_type = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
        loading_no: int = 1,
        increment_number: int = 1,
        model = Model):
        '''
        Args:
            nodeNo (int): Node Number
            loading_type (emun): Case Object Loading Type Enumeration
            loading_no (int): Loading Number
            increment_number (int): Increment Number
            model (class, optional): Model instance
        '''

        return model.clientModel.service.get_FE_node_deformed_mesh(nodeNo, {'case_object': {'type': loading_type.name, 'id': loading_no}, 'increment_number': increment_number})
