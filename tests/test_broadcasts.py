import pytest
import requests
from websocket import create_connection


def test_retrieve_messages(endpoint, reader_token):
    url = endpoint + "v1/broadcasts"
    headers = {"Authorization": "Bearer {}".format(reader_token)}
    resp = requests.get(url=url, headers=headers)
    assert "broadcasts" in resp.text


def test_broadcast_validation(endpoint, broadcaster_token, broadcaster_id):
    url = endpoint + "v1/broadcasts/" + broadcaster_id + "/validation"
    headers = {"Authorization": "Bearer {}".format(broadcaster_token)}
    resp = requests.put(url=url, data="2018-10-16_01", headers=headers)

    """

    We're expecting one of two values:
    200 - Validated an existing broadcast
    201 - Created a new broadcast
    """
    assert resp.status_code in (200, 201)


def test_sending_messages(ws_endpoint):
    ws = create_connection(ws_endpoint)
    ws.send(
        '{"messageType": "hello", "use_webpush": true, "broadcasts": {"test/validation": "v0"}}'
    )
    result = ws.recv()
    ws.close()

    """
    Sample response in JSON
    
    {
        "messageType":"hello",
        "uaid":"92a21288d67b43dea22644a6096430e0",
        "status":200,
        "use_webpush":true,
        "broadcasts":{"test/validation":"2018-10-16_01"}
    }
    """

    expected_fields = ["messageType", "uaid", "status", "use_webpush", "broadcasts"]
    for field in expected_fields:
        assert field in result
