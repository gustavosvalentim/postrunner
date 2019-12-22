import pytest

from postrunner.collection import Collection


mock_collection_path = 'tests/mocks/TestCollection.postman_collection.json'
COLLECTION_NAME = 'TestCollection'


@pytest.fixture
def collection_as_string_fixture():
    with open(mock_collection_path) as c:
        str_collection = c.read()

    return str_collection


@pytest.fixture
def collection_fixture():
    with open(mock_collection_path) as c:
        str_collection = c.read()

    return Collection(str_collection)
