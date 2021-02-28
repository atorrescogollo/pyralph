import requests

class DataCenterAssetRaw:
    def __init__(self, ralph):
        self.ralph = ralph

    def getAll(self):
        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/data-center-assets/")
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
        url = self.ralph.get_resource_url("/data-center-assets/")
        response = requests.get(url, headers=headers, params=filters)
        return response.json()

    def create(self, hostname, model_id, rack_id, position, orientation, sn=None, barcode=None, status="new", extra_fields={}):
        assert sn or barcode

        extra_fields['hostname']=hostname
        extra_fields['model']=model_id
        extra_fields['rack']=rack_id
        extra_fields['orientation']=orientation
        extra_fields['position']=position
        extra_fields['status']=status
        if sn: extra_fields['sn']=sn
        if barcode: extra_fields['barcode']=barcode

        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/data-center-assets/")
        response = requests.post(url, headers=headers, data=extra_fields)
        return response.json()

    def delete(self, id):
        headers = self.ralph.get_auth_headers()
        url = self.ralph.get_resource_url("/data-center-assets/{0}/".format(id))
        response = requests.delete(url, headers=headers)
        return dict(ok=response.ok, reason=response.reason, text=response.text)

    def edit(self):
        raise NotImplementedError()
