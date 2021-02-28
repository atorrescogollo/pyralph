import requests

class VirtualServerRaw:
    def __init__(self, ralph):
        self.ralph = ralph

    def getAll(self):
        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/virtual-servers/")
        response = requests.get(url, headers=headers)
        return response.json()

    def get(self, id=None, hostname=None, status=None, filters={}):
        """
        filters={
            "hostname__endswith": "01"
        }
        """
        if hostname: filters['hostname']=hostname
        if id: filters['id']=id
        if status: filters['status']=status

        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/virtual-servers/")
        response = requests.get(url, headers=headers, params=filters)
        return response.json()

    def create(self, hostname, hypervisor_id, type_id, status="new", extra_fields={}):
        extra_fields['type']=type_id
        extra_fields['hypervisor']=hypervisor_id
        extra_fields['hostname']=hostname
        extra_fields['status']=status

        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/virtual-servers/")
        response = requests.post(url, headers=headers, data=extra_fields)
        return response.json()

    def delete(self, id):
        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/virtual-servers/{0}/".format(id))
        response = requests.delete(url, headers=headers)
        return dict(ok=response.ok, reason=response.reason, text=response.text)

    def edit(self, id, hostname=None, hypervisor_id=None, type_id=None, status=None, extra_fields={}):
        if type_id: extra_fields['type']=type_id
        if hypervisor_id: extra_fields['hypervisor']=hypervisor_id
        if hostname: extra_fields['hostname']=hostname
        if status: extra_fields['status']=status

        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/virtual-servers/{0}/".format(id))
        response = requests.patch(url, headers=headers, data=extra_fields)
        return response.json()


class VirtualServerTypeRaw:
    def __init__(self, ralph):
        self.ralph = ralph

    def getAll(self):
        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/virtual-server-types/")
        response = requests.get(url, headers=headers)
        return response.json()

    def get(self, id=None, name=None, filters={}):
        """
        filters={
            "name__contains": "vm"
        }
        """
        if name: filters['name']=name
        if id: filters['id']=id

        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/virtual-server-types/")
        response = requests.get(url, headers=headers, params=filters)
        return response.json()

    def create(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()

    def edit(self):
        raise NotImplementedError()
