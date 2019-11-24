class Environment:

    def __init__(self, start = dict()):
        self.__env = start

    def __repr__(self):
        str = ''
        for k, v in self.__env.items():
            str += f'{k} = {v}\n'

        return str

    def get(self, key = None, default = None):
        if not key:
            return self.__env
            
        elif key in self.__env:
            return self.__env['key']

        else:
            return default

    def set(self, key, value):
        self.__env[key] = value

    def update(self, obj):
        self.__env.update(obj)


class EnvironmentFactory:
    @classmethod
    def getEnvironment(self, start = dict()):
        return Environment(start)


environment = EnvironmentFactory.getEnvironment()