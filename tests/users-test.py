import constants
import requests
import json
import pytest


def test_create_user(supply_url):
    url = supply_url["url"] + constants.USER
    data = {
        "name": "morpheus",
        "job": "leader",
    }
    response = requests.post(url, data=data)
    assert response.status_code == constants.STATUS_CREATED


def test_update_user(supply_url):
    user_id = 2
    url = supply_url["url"] + constants.USER + str(user_id)
    data = {
        "name": "morpheus",
        "job": "Zior resident",
    }
    response = requests.put(url, data=data)
    assert response.status_code == constants.STATUS_OK


@pytest.mark.parametrize("userid, firstname", [(7, "Michael"), (8, "Lindsay")])
def test_list_valid_user(supply_url, userid, firstname):
    url = supply_url['url'] + "users/" + str(userid)
    resp = requests.get(url)
    j = json.loads(resp.text)
    assert resp.status_code == constants.STATUS_OK
    assert j['data']['id'] == userid, resp.text
    assert j['data']['first_name'] == firstname, resp.text


def test_list_unexisting_user(supply_url):
    userid = 23
    url = supply_url['url'] + "users/" + str(userid)
    resp = requests.get(url)
    assert resp.status_code == constants.STATUS_NOT_FOUND


def test_delete_user(supply_url):
    userid = 2
    url = supply_url['url'] + "users/" + str(userid)
    resp = requests.delete(url)
    assert resp.status_code == constants.STATUS_NO_CONTENT


