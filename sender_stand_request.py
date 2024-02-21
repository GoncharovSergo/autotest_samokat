import configuration
import requests
import data



#Создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())
auth_token = response.json().get("authToken")


#Создание нового набора
def post_new_client_kit(kit_body, auth_token):
    kit_headers = data.headers.copy()
    kit_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
                         json=kit_body,
                         headers=kit_headers)


response = post_new_client_kit(data.kit_body, auth_token)
print(response.status_code)
print(response.json())
