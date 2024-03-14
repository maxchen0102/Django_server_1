import requests
import json
from requests import ConnectionError, HTTPError, Timeout

try:
    url = "http://localhost:8000/api"
    url_get_product = "http://localhost:8000/api/product"
    url_post_product = "http://localhost:8000/api/product_add"
    url_prodcut_delete = "http://localhost:8000/api/prodcut_delete"
    url_update_product = "http://localhost:8000/api/update_product"

    params = {
        'id': 12,
        "name": "chris",
        "flag": 2
    }
    json = {
        "title": "moto",
        "conttne": "cool but not cool ",
        "price": 2500
    }
    password = {
        "account": "kingcall",
        "password": "1111"
    }
    json_update = {
        "id": 2,
        "title": "motoxxxxxxxxxx",
        "conttne": "cool but not cool ",
        "price": 2500999
    }

    # res = requests.post(url_post,json=json)
    res = requests.post(url_update_product, params={"id": 2}, json=json_update)
    print(res),
    data = res.json()
    print(data)

except ConnectionError:
    print('找不到伺服器')
    print('沒有發生問題')