import requests

class ClusterRaw:
    def __init__(self, ralph):
        self.ralph = ralph

    def getAll(self):
        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/clusters/")
        response = requests.get(url, headers=headers)
        return response.json()

    def get(self, id=None, name=None, hostname=None, status=None, filters={}):
        """
        filters={
            "hostname__endswith": "01"
        }
        """
        if name: filters['name']=name
        if hostname: filters['hostname']=hostname
        if id: filters['id']=id
        if status: filters['status']=status

        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/clusters/")
        response = requests.get(url, headers=headers, params=filters)
        return response.json()

    def create(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()

    def edit(self):
        raise NotImplementedError()
