from json import JSONDecodeError

import jsonpath_rw


def find_jsonpath_response(response, jsonpath):
    try:
        json_response = response.json()
    
    except JSONDecodeError as err:
        print('Error decoding response: %s' % response.content.decode('utf-8'))
        print(err)
    
    jsonpath_expr = jsonpath_rw.parse(jsonpath)
    jsonpath_matches = [x.value for x in jsonpath_expr.find(json_response)]

    return jsonpath_matches
