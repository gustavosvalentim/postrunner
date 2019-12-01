from postrunner.collection import Collection


with open('tests/mocks/TestCollection.postman_collection.json') as c:
    str_collection = c.read()


class TestCollection:
    def test_load_collection(self):
        c = Collection(str_collection)
        assert type(c) == Collection
