from app import app

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Jenkins Pipeline!" in response.data
