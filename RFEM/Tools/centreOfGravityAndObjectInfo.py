from RFEM.initModel import Model

def GetCOGTableParameters(results):
    '''
    Returns dict with attributes: base, row, and error.
    '''
    params = {'base': [], 'row': [], 'error': None}

    if not results:
        return params

    if results[0][0]:
        for section in results[0]:
            params['base'] = list(set(params['base'] + section.__keylist__))
            if 'rows' in section.__keylist__ and 'row' in section['rows']:
                for row in section['rows']['row']:
                    params['row'] = list(set(params['row'] + row.__keylist__))
            else:
                params['error'] = "Result table doesn't have attribute 'rows' or 'row'."

    return params

def ConvertCOGInfoToListOfDct(cog):
    '''
    Args:
        cog (dict): Dictionary object of center of gravity and objects information
    Returns:
        List of dictionaries. Each dictionary corresponds to one line in center of gravity and objects information table.
    '''
    if not cog:
        return ''

    params = GetCOGTableParameters(cog)
    lstOfDct = []

    for c in cog[0]:
        dct1 = {}
        if 'title' in params['base']:
            try:
                dct1['title'] = float(c['title'])
            except:
                try:
                    dct1['title'] = c['title']
                except:
                    pass

        if 'rows' in params['base']:

            for row in c['rows'][0]:
                dct = {}
                dct.update(dct1)
                for y in params['row']:
                    try:
                        dct[y] = float(row[y])
                    except:
                        try:
                            dct[y] = row[y]
                        except:
                            pass
                lstOfDct.append(dct)

    if params['error']:
        return lstOfDct.append({'error': params['error']})

    return lstOfDct

class ObjectsInfo():

    @staticmethod
    def AllInfo(objects: list = None,
                 model = Model):
        '''
        Args:
            objects (list of lists): List of Selected Objects
                objects = [[ObjectTypes enumeration, Object number], ...]   (e.g. [[ObjectTypes.E_OBJECT_TYPE_MEMBER,1], [ObjectTypes.E_OBJECT_TYPE_MEMBER, 2]])
            model (class, optional): Model instance

        Returns:
            List of dictionaries.
        '''

        if objects:
            cog_objects = {'center_of_gravity_objects' : []}

            for obj in objects:
                cog_objects["center_of_gravity_objects"].append({
                    "type": obj[0].name,
                    "no": obj[1]
                })
            return ConvertCOGInfoToListOfDct(model.clientModel.service.get_center_of_gravity_and_objects_info(cog_objects))

        else:
            raise AssertionError('WARNING! Please give at lease one object.')

    @staticmethod
    def CenterofGravity(objects: list = None,
                        model = Model):
        '''
        Args:
            objects (list of lists): List of Selected Objects
                objects = [[ObjectTypes enumeration, Object number], ...]   (e.g. [[ObjectTypes.E_OBJECT_TYPE_MEMBER,1], [ObjectTypes.E_OBJECT_TYPE_MEMBER, 2]])
            model (class, optional): Model instance

        Returns:
            List of dictionary.
        '''

        allList = ObjectsInfo.AllInfo(objects, model)
        cog_Info = {}
        for item in allList:
            if item['title'] == 'Center of Gravity':
               cog_Info[item.get('name')] = item.get('value')

        return cog_Info

    @staticmethod
    def AllSelectedObjectsInfo(objects: list = None,
                           model = Model):
        '''
        Args:
            objects (list of lists): List of Selected Objects
                objects = [[ObjectTypes enumeration, Object number], ...]   (e.g. [[ObjectTypes.E_OBJECT_TYPE_MEMBER,1], [ObjectTypes.E_OBJECT_TYPE_MEMBER, 2]])
            model (class, optional): Model instance

        Returns:
            List of dictionary.
        '''

        allList = ObjectsInfo.AllInfo(objects, model)
        cog_Info = {}
        for item in allList:
            if item['title'] == 'Information About All Selected Objects':
               cog_Info[item.get('name')] = item.get('value')

        return cog_Info

    @staticmethod
    def MembersInfo(objects: list = None,
                model = Model):
        '''
        Args:
            objects (list of lists): List of Selected Objects
                objects = [[ObjectTypes enumeration, Object number], ...]   (e.g. [[ObjectTypes.E_OBJECT_TYPE_MEMBER,1], [ObjectTypes.E_OBJECT_TYPE_MEMBER, 2]])
            model (class, optional): Model instance

        Returns:
            List of dictionary.
        '''

        allList = ObjectsInfo.AllInfo(objects, model)
        cog_Info = {}
        for item in allList:
            if item['title'] == 'Information About Members':
               cog_Info[item.get('name')] = item.get('value')

        return cog_Info

    @staticmethod
    def SurfacesInfo(objects: list = None,
                 model = Model):
        '''
        Args:
            objects (list of lists): List of Selected Objects
                objects = [[ObjectTypes enumeration, Object number], ...]   (e.g. [[ObjectTypes.E_OBJECT_TYPE_MEMBER,1], [ObjectTypes.E_OBJECT_TYPE_MEMBER, 2]])
            model (class, optional): Model instance

        Returns:
            List of dictionary.
        '''

        allList = ObjectsInfo.AllInfo(objects, model)
        cog_Info = {}
        for item in allList:
            if item['title'] == 'Information About Surfaces':
               cog_Info[item.get('name')] = item.get('value')

        return cog_Info

    @staticmethod
    def SolidsInfo(objects: list = None,
               model = Model):
        '''
        Args:
            objects (list of lists): List of Selected Objects
                objects = [[ObjectTypes enumeration, Object number], ...]   (e.g. [[ObjectTypes.E_OBJECT_TYPE_MEMBER,1], [ObjectTypes.E_OBJECT_TYPE_MEMBER, 2]])
            model (class, optional): Model instance

        Returns:
            List of dictionary.
        '''

        allList = ObjectsInfo.AllInfo(objects, model)
        cog_Info = {}
        for item in allList:
            if item['title'] == 'Information About Solids':
               cog_Info[item.get('name')] = item.get('value')

        return cog_Info

    @staticmethod
    def EnvelopeSize(objects: list = None,
                     model = Model):
        '''
        Args:
            objects (list of lists): List of Selected Objects
                objects = [[ObjectTypes enumeration, Object number], ...]   (e.g. [[ObjectTypes.E_OBJECT_TYPE_MEMBER,1], [ObjectTypes.E_OBJECT_TYPE_MEMBER, 2]])
            model (class, optional): Model instance

        Returns:
            List of dictionary.
        '''

        allList = ObjectsInfo.AllInfo(objects, model)
        cog_Info = {}
        for item in allList:
            if item['title'] == 'Envelope Size':
               cog_Info[item.get('name')] = item.get('value')

        return cog_Info
