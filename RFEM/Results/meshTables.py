from RFEM.initModel import Model

def GetResultTableParameters(results):
    '''
    Returns dict with 3 atributes: base, row and error.
    '''
    params = {'base':[], 'row':[], 'error': None}

    if not results:
        return ''

    if results[0][0]:
        for i in results[0]:
            params['base'] = list(set(params['base'] + i.__keylist__))
            if 'row' in i.__keylist__ and i.row:
                params['row'] = list(set(params['row'] + i.row.__keylist__))
            else:
                params['errors'] = "Result table doesn't have attribute 'row'."

    return params

def ConvertResultsToListOfDct(results, includeBase = False):
    '''
    Args:
        results (ResultTables class): ResultTables object
        includeBase (bool): Include base information of every line. Typicaly 'object number' and 'description'. Default is False.
    Returns:
        List of dictionaries. Each dictionary corresponds to one line in result table.
    '''
    if not results:
        return ''

    params = GetResultTableParameters(results)
    lstOfDct = []

    for r in results[0]:
        dct = {}
        if includeBase and params['base']:
            for i in params['base']:
                if i == 'row':
                    for y in params['row']:
                        try:
                            dct[y] = float(r.row[y].value)
                        except:
                            try:
                                dct[y] = r.row[y].value
                            except:
                                try:
                                    dct[y] = float(r.row[y])
                                except:
                                    try:
                                        dct[y] = r.row[y]
                                    except:
                                        pass
                else:
                    try:
                        dct[i] = float(r[i])
                    except:
                        try:
                            dct[i] = r[i]
                        except:
                            pass
            lstOfDct.append(dct)
        else:
            if params['row']:
                for i in params['row']:
                    try:
                        dct[i] = float(r.row[i].value)
                    except:
                        try:
                            dct[i] = r.row[i].value
                        except:
                            try:
                                dct[i] = float(r.row[i])
                            except:
                                try:
                                    dct[i] = r.row[i]
                                except:
                                    pass
                lstOfDct.append(dct)

    if params['error']:
        return lstOfDct.append({'error': params['error']})

    return lstOfDct

class MeshTables():

    @staticmethod
    def GetAllFENodes(
        include_base: bool = False,
        model = Model):
        '''
        Args:
            model(class, optional): Model instance
        '''
        return ConvertResultsToListOfDct(model.clientModel.service.get_all_FE_nodes(), include_base)

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
    def getFENode(
        nodeNo: int = 1,
        model = Model):

        return model.clientModel.service.get_FE_node(nodeNo)

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
