from json import JSONDecodeError

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
    __certificate = None
    __verify_certificate = True

    def __init__(self, request_obj, certificate=None, verify_certificate=True):
        request_props = request_obj['request']

        self.name = request_obj['name']
        self.__url = request_props['url']['raw']
        self.__method = request_props['method']

        if 'body' in request_props:
            self.__is_json, self.__body = parse_body(request_props['body'])

        self.__headers = parse_headers(request_props['header'])

        if 'event' in request_obj:
            self.__scripts = parse_scripts(request_obj['event'])

        self.__certificate = certificate
        self.__verify_certificate = verify_certificate

    def __before(self):
        events = interpret_lines(self.__scripts['before'])
        for etype, evalue in events.items():
            if etype == 'env':
                environment.update(evalue)

    def __after(self, json_response):
        events = interpret_lines(self.__scripts['after'])
        parsed_events = parse_using_response(events, json_response)
        for etype, evalue in parsed_events.items():
            if etype == 'env':
                environment.update(evalue)

    def run(self):
        request_kwargs = dict(url=self.__url, method=self.__method, headers=self.__headers)
        if self.__method.lower() == 'get':
            request_kwargs['params'] = self.__body
            
        else:
            if self.__is_json:
                request_kwargs['json'] = self.__body

            else:
                request_kwargs['data'] = self.__body

        parsed_kwargs = parse_kwargs(request_kwargs)
        response = requests.request(
            **parsed_kwargs,
            cert=self.__certificate,
            verify=self.__verify_certificate
        )

        response_content = None
        try:
            response_content = response.json()
            self.__after(response_content) 

        except JSONDecodeError:
            response_content = response.content.decode('utf-8')

        return response_content
