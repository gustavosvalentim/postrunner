from postrunner.environment import environment


class Runner:
    __collections = list()
    __response_storage = dict()

    def use_collection(self, collection_ins):
        self.__collections.append(collection_ins)

    def run(self, **env):
        environment.update(env)
        requests = [col.get_requests() for col in self.__collections]
        result = {}
        for col_req_list in requests:
            for req in col_req_list:
                result[req.name] = req.run()
        
        return result


class RunnerFactory:
    @classmethod
    def get_runner(cls):
        return Runner()


runner = RunnerFactory.get_runner()
