from json import JSONDecodeError


class Response:
    def __init__(self, response_obj, exec_time=None):
        self.status_code = response_obj.status_code
        self.text = response_obj.content.decode('utf-8')
        self.headers = response_obj.headers
        self.time = round(exec_time, 2)

        try:
            self.json = response_obj.json()
            self.is_json = True

        except JSONDecodeError as err:
            self.json = {}
            self.is_json = False
