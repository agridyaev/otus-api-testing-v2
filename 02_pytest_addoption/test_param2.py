import pytest


@pytest.mark.parametrize("code", [200, 300, 400, 404, 500, 502])
def test_url_status(base_url, request_method, code):
    target = base_url + f"/status/{code}"
    response = request_method(target)
    assert response.status_code == code