
import requests
import urllib3

class BaseClient:

    def __init__(self, url):
        self.url = url

    def get(self):
        pass


class FetchData(BaseClient):

    def get(self):
        session = requests.Session()
        response = session.get(self.url)
        return response

if __name__ == '__main__':
    ancients = FetchData("https://api.opendota.com/api/constants/ancients").get()
    print(ancients.text)

