import constants
import requests


def test_successful_login(supply_url):
    url = supply_url['url'] + constants.LOGIN
    data = {
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka',
    }
    response = requests.post(url, data=data)
    assert response.status_code == constants.STATUS_OK


def test_unsuccessful_login(supply_url):
    url = supply_url['url'] + constants.LOGIN
    data = {
        'email' : 'peter@klaven'
    }
    response = requests.post(url, data=data)
    assert response.status_code == constants.STATUS_BAD_REQUEST
