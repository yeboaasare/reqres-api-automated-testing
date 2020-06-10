import constants
import requests
import json


def test_successful_registration(supply_url):
    url = supply_url["url"] + constants.REGISTER
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol",
    }
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == constants.STATUS_OK
    assert token["token"] == "QpwL5tke4Pnpja7X4"


def test_unsuccessful_registration(supply_url):
    url = supply_url["url"] + constants.REGISTER
    data = {
        "email": "sydney@fife",
    }
    response = requests.post(url, data=data)
    assert response.status_code == constants.STATUS_BAD_REQUEST
