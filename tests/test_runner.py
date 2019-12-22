from postrunner.runner import runner

from tests.fixtures import collection_fixture, COLLECTION_NAME


class TestRunner:
    def test_success_run(self, collection_fixture):
        runner.use_collection(collection_fixture)
        runner.run()
        assert hasattr(runner, COLLECTION_NAME)
