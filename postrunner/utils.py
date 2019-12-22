import jsonpath_rw


def find_jsonpath_response(response, jsonpath):
    if not response.is_json:
        raise TypeError('Response is not a json')

    json_response = response.json
    jsonpath_expr = jsonpath_rw.parse(jsonpath)

    jsonpath_matches = [x.value for x in jsonpath_expr.find(json_response)]

    return jsonpath_matches
