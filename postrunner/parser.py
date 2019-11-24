import json

from postrunner.environment import environment


def parse_kwargs(kwargs):
    if isinstance(kwargs, str):
        return kwargs.replace('{{', '{').replace('}}', '}').format(**environment.get())

    elif isinstance(kwargs, dict):
        d = {}
        for k, v in kwargs.items():
            d[k] = parse_kwargs(v)
            
        return d
    
    else:
        return kwargs


def parse_headers(header_obj):
    return dict([ [ x['key'], x['value'] ] for x in header_obj ])


def parse_body(body_obj):
    body_mode = body_obj['mode']
    is_json = False
    body = dict()
    if body_mode == 'raw':
        body_raw = body_obj['raw']
        try:
            json_body = json.loads(body_raw)
            is_json = True
            body.update(json_body)

        except json.JSONDecodeError as err:
            return [ is_json, body_raw ]
    
    if body_mode == 'urlencoded':
        body.update(dict([ [ x['key'], x['value'] ] for x in body_obj['urlencoded'] ]))

    return [ is_json, body ]


def parse_scripts(scripts_obj):
    scripts = dict(before = [], after = [])
    for s in scripts_obj:
        if s['listen'] == 'prerequest':
            scripts['before'] = s['script']['exec']
        elif s['listen'] == 'test':
            scripts['after'] = s['script']['exec']

    return scripts