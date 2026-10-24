def test_api_status():
    response = get_api_response()
    assert response.status_code == 999
