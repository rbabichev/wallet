import requests


class Request(object):

    def __init__(self):
        self.request = requests

    def get(self, endpoint):
        result = self.request.get(endpoint, verify=False)
        return result

    def post(self, endpoint, data, header):
        result = self.request.post(endpoint, data, header, verify=False)
        return result
