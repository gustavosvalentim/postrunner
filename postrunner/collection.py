import json

from postrunner.request import Request


class Collection:
	info = dict()
	__requests = list()

	def __init__(self, collection_as_string, cert=None, verify=True):
		collection_obj = json.loads(collection_as_string)
		self.__load(collection_obj)

	def __getattr__(self, attr):
		for r in self.__requests:
			if r.name == attr:
				return r
		
		else:
			raise KeyError()

	def __load(self, collection_obj):
		self.info = collection_obj['info']
		for item in collection_obj['item']:
			self.__requests.append(Request(item))

	def get_requests(self):
		return self.__requests
