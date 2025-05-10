<<<<<<< HEAD
import requests
from app.config import PINATA_JWT

class IPFSClient:
    def __init__(self):
        self.api_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
        self.json_url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
        self.headers = {
            "Authorization": f"Bearer {PINATA_JWT}"
        }

    def upload_file(self, file):
        files = {'file': file}
        response = requests.post(
            self.api_url,
            files=files,
            headers=self.headers
        )
        if response.status_code == 200:
            return response.json()['IpfsHash']
        else:
            raise Exception(f"IPFS upload failed: {response.text}")

    def upload_json(self, data):
        response = requests.post(
            self.json_url,
            json={'pinataContent': data},
            headers=self.headers
        )
        if response.status_code == 200:
            return response.json()['IpfsHash']
        else:
            raise Exception(f"IPFS upload failed: {response.text}")

def upload_to_ipfs(file_or_data, is_file=True):
    client = IPFSClient()
    if is_file:
        return client.upload_file(file_or_data)
    else:
=======
import requests
from app.config import PINATA_JWT

class IPFSClient:
    def __init__(self):
        self.api_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
        self.json_url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
        self.headers = {
            "Authorization": f"Bearer {PINATA_JWT}"
        }

    def upload_file(self, file):
        files = {'file': file}
        response = requests.post(
            self.api_url,
            files=files,
            headers=self.headers
        )
        if response.status_code == 200:
            return response.json()['IpfsHash']
        else:
            raise Exception(f"IPFS upload failed: {response.text}")

    def upload_json(self, data):
        response = requests.post(
            self.json_url,
            json={'pinataContent': data},
            headers=self.headers
        )
        if response.status_code == 200:
            return response.json()['IpfsHash']
        else:
            raise Exception(f"IPFS upload failed: {response.text}")

def upload_to_ipfs(file_or_data, is_file=True):
    client = IPFSClient()
    if is_file:
        return client.upload_file(file_or_data)
    else:
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
        return client.upload_json(file_or_data)