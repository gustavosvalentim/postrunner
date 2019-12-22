from postrunner.collection import Collection

from tests.fixtures import collection_as_string_fixture, collection_fixture, COLLECTION_NAME


class TestCollection:
    def test_load_collection(self, collection_as_string_fixture):
        c = Collection(collection_as_string_fixture)
        assert type(c) == Collection

    def test_collection_name(self, collection_fixture):
        assert collection_fixture.info['name'] == COLLECTION_NAME

    def test_get_collection_requests(self, collection_fixture):
        collection_requests = collection_fixture.get_requests()
        assert type(collection_requests) == list

