
import pytest
import requests
import source.service as service
import unittest.mock as mock

# mock, skip, fail test cases addressed
@pytest.mark.skip(reason ='temporarily disabled')
@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Alice"

@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400  # to fail & see on console "FAILED tests/test_service.py::test_get_users - requests.exceptions.HTTPError"
    mock_response.json.return_value = {"id": 1, "name": "john Doe"}
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "name": "john Doe"}

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_response.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
