import requests
import unittest


token_ya = 'Место для вашего токена'
api_base_url = 'https://cloud-api.yandex.net/'
headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {token_ya}'
        }


class TestDocuments(unittest.TestCase):

    def test_create_folder1(self):
        response = requests.put(api_base_url + 'v1/disk/resources', params={'path': 'Test'}, headers=headers)
        assert response.status_code == 201

    def test_create_folder2(self):
        response = requests.put(api_base_url + 'v1/disk/resources', params={'path': 'Test'}, headers=headers)
        assert response.status_code == 409

    def test_get_folder(self):
        response = requests.get(api_base_url + 'v1/disk/resources', params={'path': 'Test'}, headers=headers)
        assert response.status_code == 200

    def test_get_folder2(self):
        response = requests.get(api_base_url + 'v1/disk/resources', params={'path': 'Нет такой папки'}, headers=headers)
        assert response.status_code == 404


if __name__ == '__main__':
    unittest.main()

