from postrunner.collection import Collection
from postrunner.runner import runner
from postrunner.utils import find_jsonpath_response


with open('TestCollection.postman_collection.json') as c:
    collection = Collection(c.read())

runner.use_collection(collection)
runner.run()

test_collection_responses = runner.TestCollection
test_request_response = test_collection_responses['TestRequest']
test_request_status_code = test_request_response.status_code

jsonpath = 'headers.host'
test_request_response_jsonpath = find_jsonpath_response(test_request_response, jsonpath)
print(test_request_response_jsonpath)
