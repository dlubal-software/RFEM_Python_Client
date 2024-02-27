from RFEM.initModel import Model
from RFEM.Results.resultTables import ConvertResultsToListOfDct

class MeshTables():

    @staticmethod
    def GetAllFENodes(
        include_base: bool = False,
        model = Model):
        '''
        Args:
            model(class, optional): Model instance
        '''
        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_nodes_original_mesh(), include_base)

    @staticmethod
    def getAllFE1DElements(
        include_base: bool = False,
        model = Model):
        '''
        Args:
            model(class, optional): Model instance
        '''
        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_1D_elements(), include_base)

    @staticmethod
    def getAllFE2DElements(
        include_base: bool = False,
        model = Model):
        '''
        Args:
            model(class, optional): Model instance
        '''
        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_2D_elements(), include_base)

    @staticmethod
    def getAllFE3DElements(
        include_base: bool = False,
        model = Model):
        '''
        Args:
            model(class, optional): Model instance
        '''
        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_3D_elements(), include_base)

    @staticmethod
    def getFENodeOriginalMesh(
        nodeNo: int = 1,
        model = Model):

        return model.clientModel.service.get_FE_node_original_mesh(nodeNo)

    @staticmethod
    def getFE1DElement(
        elementNo: int = 1,
        model = Model):

        return model.clientModel.service.get_FE_1D_element(elementNo)

    @staticmethod
    def getFE2DElement(
        elementNo: int = 1,
        model = Model):

        return model.clientModel.service.get_FE_2D_element(elementNo)

    @staticmethod
    def getFE3DElement(
        elementNo: int = 1,
        model = Model):

        return model.clientModel.service.get_FE_3D_element(elementNo)
