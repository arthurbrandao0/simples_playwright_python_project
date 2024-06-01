import requests
import pytest

def test_retrieve_available_pets():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus'
    params = {
        'status': 'available'
    }
    headers = {
        'accept': 'application/json'
    }
    
    response = requests.get(url, params=params, headers=headers)
    
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body[0]['id'], int)
