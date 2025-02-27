# Usage: tests API on:
# https://reqres.in/
# idea from yt tutorial on:
# https://www.youtube.com/watch?v=byaxg00Gf9I

import json

import pytest
import requests

# def main_url():
#     return "https://reqres.in"


@pytest.mark.skip(reason="no way of currently testing this")
def test_if_login_valid():
    url = "https://reqres.in/api/login/"
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.get(url, data=data)
    token = json.loads(response.text)

    assert response.status_code == 200
    assert token["token"] == "QpwL5tke4Pnpja7X4"
