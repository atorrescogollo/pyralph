import requests

class Ralph:
    def __init__(self, username, password, base_url="http://localhost"):
        self.base_url = base_url
        self.credentials = dict(username=username, password=password)

    def _get_token(self):
        url = '{0}/api-token-auth/'.format(self.base_url)
        data = self.credentials
        response = requests.post(url, json=data)
        return response.json()
