import configuration2
import requests
import data


def post_new_user(body):
    return requests.post(configuration2.URL_SERVICE + configuration2.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)