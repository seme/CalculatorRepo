from app import app


def test_api(self):
    with app.test_client() as c:
        response = c.get('/')
        assert response.data == b'please give a number in the URL'
        assert response.status_code == 200
