class Routers(object):
    def __init__(self, routers , apis):
        self.__routers = routers
        self.__apis = apis
        self.__all_apis = list()
        self.__regist_all_apis()
        print(self.__all_apis)
    
    def __regist_all_apis(self):
        self.__recursive_find(self.__routers, self.__apis)

    def __recursive_find(self, routers, api):
        if type(api) == dict:
            for k, v in api.items():
                self.__recursive_find(routers, v)
        elif type(api) == list:
            routers.add(api[0], api[1], action=api[2])
            self.__all_apis.append(api)
