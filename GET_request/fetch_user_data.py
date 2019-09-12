import requests

url_get_list_users = "https://reqres.in/api/users?page=2"
response = requests(url_get_list_users)
print (response.headers)