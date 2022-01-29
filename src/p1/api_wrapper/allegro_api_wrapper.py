import requests
import base64
from pprint import pprint


class AllegroAPIWrapper:
    headers: dict
    app_id: str
    app_secret: str

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

        token = self.get_access_token()

        self.headers = {
            'authorization': f'Bearer {token}',
            'accept': 'application/vnd.allegro.public.v1+json',
            'content-type': 'application/vnd.allegro.public.v1+json'
        }

    def get_access_token(self):
        auth = base64.b64encode(f'{self.client_id}:{self.client_secret}'.encode()).decode()

        response = requests.post('https://allegro.pl.allegrosandbox.pl/auth/oauth/token', data={
            'grant_type': 'client_credentials'
        }, headers={
            'Authorization': f'Basic {auth}',
            'Content-Type': 'application/x-www-form-urlencoded'
        })

        return response.json().get('access_token')

    def get(self, path: str):
        return requests.get(f'https://api.allegro.pl.allegrosandbox.pl/{path}', headers=self.headers)


if __name__ == '__main__':
    app_id = '7bbda6ae73864eceb06b9d8cdc2f647b'
    app_secret = 'DbpVJ6rcMXojGOLYqrQNVwxBhe13qKjil54DpoxhnDCj2idWN1GEvqMp7ixIQ4PD'

    wrapper = AllegroAPIWrapper(app_id, app_secret)
    # pprint(wrapper.get('sale/categories').json())

    # docs
    # https://developer.allegro.pl/documentation/#operation/getListing
    pprint(wrapper.get('offers/listing?phrase=laptop&sort=+price').json().get('items'))
