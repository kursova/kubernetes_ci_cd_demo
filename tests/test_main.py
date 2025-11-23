import pytest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Test the root route returns 200 and expected content."""
    rv = client.get('/')
    assert rv.status_code == 200
    
    assert b"Hello from version" in rv.data
