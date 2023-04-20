import pytest


@pytest.mark.parametrize("code", [200, 300, 400, 404, 500, 502])
def test_url_status(request, code):
    base_url = request.config.getoption("--url")
    request_method = getattr(requests, request.config.getoption("--method"))
    target = base_url + f"/status/{code}"
    response = request_method(target)
    assert response.status_code == code
