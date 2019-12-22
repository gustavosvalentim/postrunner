import logging

from postrunner.environment import environment


class Runner:
    __collections = list()
    __response_storage = dict()

    def use_collection(self, collection_ins):
        self.__collections.append(collection_ins)

    def run(self, **env):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        environment.update(env)
        requests = dict([[col.info['name'], col.get_requests()] for col in self.__collections])
        for col_name, col_requests in requests.items():
            self.__response_storage[col_name] = dict([[req.name, req.run()] for req in col_requests])

    def __getattr__(self, attr):
        if attr not in self.__response_storage:
            raise AttributeError('Collection %s not found' % attr)

        return self.__response_storage[attr]


class RunnerFactory:
    @classmethod
    def get_runner(cls):
        return Runner()


runner = RunnerFactory.get_runner()
