import requests


def test_root():
    req = requests.get('http://127.0.0.1:8000/api/get')
    assert req.status_code == 200


def test_root_with_params():
    req = requests.get('http://127.0.0.1:8000/api/get?id=1&id=2')
    assert req.status_code == 200


# Here we can write other tests to out methods...
