import requests

class Ralph:

    def __init__(self, username, password, base_url="http://localhost"):
        self.base_url = base_url
        self.credentials = dict(username=username, password=password)

    def _get_token(self):
        url = '{0}/api-token-auth/'.format(self.base_url)
        data = self.credentials
        response = requests.post(url, json=data)
        return response.json()['token']

    def get_auth_headers(self):
        token = self._get_token()
        headers = {}
        headers['Authorization'] = "Token {0}".format(token)
        return headers

    def get_resource_url(self, resource_path):
        return "{0}{1}".format(self.base_url, "/api"+resource_path)
