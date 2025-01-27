import pytest
from unittest.mock import Mock
from put_delete import JSONPlaceholder

@pytest.fixture
def json_placeholder():
    """Fixture to create a JSONPlaceholder instance"""
    base_url = "https://jsonplaceholder.typicode.com/posts"
    return JSONPlaceholder(base_url)

def test_class_initialization(json_placeholder):
    """Test if the class is initialized correctly with the base URL"""
    assert isinstance(json_placeholder, JSONPlaceholder)
    assert json_placeholder.base_url == "https://jsonplaceholder.typicode.com/posts"

def test_update_user_success(json_placeholder, mocker):
    """Test successful PUT request to update a user"""
    # Mock the PUT response
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.headers = {"Content-Type": "application/json"}
    mock_resp.content = b'{"userId": 3, "id": 3, "title": "My test", "body": "Testing for user 3"}'
    mocker.patch('requests.put', return_value=mock_resp)
    
    result = json_placeholder.update_user(3, "My test", "Testing for user 3")
    
    # Verify response structure and content
    assert isinstance(result, dict)
    assert all(key in result for key in ['status_code', 'headers', 'content'])
    assert result['status_code'] == 200
    assert result['headers'] == {"Content-Type": "application/json"}
    assert result['content'] == b'{"userId": 3, "id": 3, "title": "My test", "body": "Testing for user 3"}'

def test_update_user_correct_url_and_data(json_placeholder, mocker):
    """Test if update_user makes PUT request with correct URL and data"""
    mock_put = mocker.patch('requests.put')
    user_id = 3
    title = "My test"
    body = "Testing for user 3"
    expected_data = {"title": title, "body": body}
    
    json_placeholder.update_user(user_id, title, body)
    
    # Verify the PUT request was made with correct URL and data
    expected_url = f"{json_placeholder.base_url}/{user_id}"
    mock_put.assert_called_once_with(expected_url, expected_data)

def test_delete_user_success(json_placeholder, mocker):
    """Test successful DELETE request"""
    # Mock the DELETE response
    mock_resp = Mock()
    mock_resp.status_code = 200
    mocker.patch('requests.delete', return_value=mock_resp)
    
    result = json_placeholder.delete_user(3)
    
    # Verify response structure and content
    assert isinstance(result, dict)
    assert 'status_code' in result
    assert result['status_code'] == 200

def test_delete_user_correct_url(json_placeholder, mocker):
    """Test if delete_user makes DELETE request with correct URL"""
    mock_delete = mocker.patch('requests.delete')
    user_id = 3
    
    json_placeholder.delete_user(user_id)
    
    # Verify the DELETE request was made with correct URL
    expected_url = f"{json_placeholder.base_url}/{user_id}"
    mock_delete.assert_called_once_with(expected_url)