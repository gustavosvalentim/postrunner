# Postrunner
Run Postman collections using Python.

# How to use
First, import the requirements
```python
from postrunner.collection import Collection
from postrunner.runner import runner
```

Now open your collection and create an instance of `Collection`
```python
with open(path_to_your_collection) as c:
    str_collection = c.read()

collection = Collection(str_collection)
```

Add your collection to runner object and run it
```python
runner.use_collection(collection)
runner.run()
```

To access the response of your requests use `runner.CollectionName`