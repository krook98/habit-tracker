import requests
import os
from datetime import datetime

USERNAME = os.environ.get('USERNAME')
TOKEN = os.environ.get('TOKEN')
GRAPH_ID = 'graph1'


pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(pixela_endpoint, json=user_params)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    'id': GRAPH_ID,
    'name': 'My Coding Graph',
    'unit': 'hours',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

today = datetime.now()

pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': "22"
}

# POST
post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
# post_pixel_response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=headers)

# PUT
new_pixel_data = {
    'quantity': '2'
}

put_pixel_endpoint = f"{post_pixel_endpoint}/{pixel_data['date']}"
# put_pixel_response = requests.put(url=put_pixel_endpoint, json=new_pixel_data, headers=headers)

# DELETE
delete_pixel_data = {
    'quantity': '10'
}

delete_pixel_endpoint = put_pixel_endpoint
# delete_pixel_response = requests.delete(url=delete_pixel_endpoint, json=delete_pixel_data, headers=headers)
