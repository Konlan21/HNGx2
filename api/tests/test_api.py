from rest_framework.test import APIClient
from rest_framework import status


class TestCreatePerson:
    def test_create_person_object_returns_201(self):


        client = APIClient()

        response = client.post('/api/ ', { 'title': 'Mark Essien' })
        
        assert response.status_code == status.HTTP_201_CREATED