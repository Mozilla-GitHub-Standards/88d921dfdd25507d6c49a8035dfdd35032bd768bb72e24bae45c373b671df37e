import requests


def test_broadcast_validation(endpoint, bearer_token):
    url = endpoint + "v1/broadcasts/test/validation"
    headers = {'Authorization': 'Bearer {}'.format(bearer_token)}
    resp = requests.put(
        url=url,
        data='2018-10-16_01',
        headers=headers
    )

    '''
    We're expecting one of two values:
    200 - Validated an existing broadcast
    201 - Created a new broadcast
    '''
    assert resp.status_code in (200, 201)
