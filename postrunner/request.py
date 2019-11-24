import requests

from postrunner.scripts_handler import interpret_lines, parse_using_response
from postrunner.parser import parse_kwargs, parse_body, parse_headers, parse_scripts
from postrunner.environment import environment


class Request:
    name = str()
    __url = str()
    __method = str()
    __body = dict()
    __headers = dict()
    __scripts = list()
    __is_json = False

    def __init__(self, request_obj):
        request_props = request_obj['request']

        self.name = request_obj['name']
        self.__url = request_props['url']['raw']
        self.__method = request_props['method']
        self.__is_json, self.__body = parse_body(request_props['body'])
        self.__headers = parse_headers(request_props['header'])
        self.__scripts = parse_scripts(request_obj['event'])

    def __before(self):
        events = interpret_lines(self.__scripts['before'])
        for etype, evalue in events.items():
            if etype == 'env':
                environment.update(evalue)

    def __after(self, jsonResponse):
        events = interpret_lines(self.__scripts['after'])
        parsed_events = parse_using_response(events, jsonResponse)
        for etype, evalue in parsed_events.items():
            if etype == 'env':
                environment.update(evalue)

    def run(self, **env):
        request_kwargs = dict(url = self.__url, method = self.__method, headers = self.__headers)
        if self.__method.lower() == 'get':
            request_kwargs['params'] = self.__body
            
        else:
            if self.__is_json:
                request_kwargs['json'] = self.__body

            else:
                request_kwargs['data'] = self.__body

        parsed_kwargs = parse_kwargs(request_kwargs)
        response = requests.request(**parsed_kwargs)

        self.__after(response.json())

        return response.content.decode('utf-8')