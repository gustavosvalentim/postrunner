import re


def process_set_environment(line):
    substr = re.sub(r'pm\.environment\.set', '', line)[1:-1]
    key, value = substr.split(',')
    key = key.strip()
    value = value.strip()
    if key.startswith('"') or key.startswith("'"):
        key = key[1:-1]
    
    if value.startswith('"') or value.startswith("'"):
        value = value[1:-1]

    return ['env', [key, value]]


SCRIPTS_MAPPING = {
    r'pm\.environment\.set\(.+\)': process_set_environment
}


def interpret_lines(lines):
    r = {
        'env': {}
    }
    for line in lines:
        line = line.replace('\\', '')
        for k, v in SCRIPTS_MAPPING.items():
            is_match = re.search(k, line)
            if is_match:
                process_type, key_value = v(line)
                r[process_type].update({ key_value[0]: key_value[1] })

    return r


def parse_using_response(key_value_dict, jsonResponse):
    d = {}
    for etype, evalue in key_value_dict.items():
        d[etype] = {}
        for k, v in evalue.items():
            if v.startswith('jsonResponse'):
                v = v.replace('jsonResponse.', '')
                d[etype][k] = jsonResponse[v]
            else:
                d[etype][k] = v
    return d