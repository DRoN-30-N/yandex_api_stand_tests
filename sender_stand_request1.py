import configuration2
import requests
import data


def post_products_kits(product_ids):
    return requests.post(configuration2.URL_SERVICE + configuration2.PRODUCTS_KITS_PATH,
                         headers=data.headers)
response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())
