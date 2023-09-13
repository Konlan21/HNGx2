from rest_framework.test import APIClient
from rest_framework import status
import pytest
from api.models import Person
import json


@pytest.mark.django_db
class TestCreatePerson:
    def test_create_person_object_returns_201(self):
        client = APIClient()
        response = client.post('/api/', { 'name': 'Mark Essien' })
        assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
class TestRetrievePerson:
    def test_retrieve_person_object_return_200(self):
        new_person = Person.objects.create(name='Mark Essien')
        client = APIClient()
        response = client.get(f'/api/{new_person.id}/')
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestUpdatePerson:
    def test_update_person_object_returns_200(self):
        new_person = Person.objects.create(name='Mark Essien')
        client = APIClient()
        updated_data = {'name': 'Updated Name'}

        response = client.put(
            f'/api/{new_person.id}/',
            data=json.dumps(updated_data),
            content_type='application/json',
        )

        assert response.status_code == status.HTTP_200_OK

        new_person.refresh_from_db()

        assert new_person.name == updated_data['name']


@pytest.mark.django_db
class TestDeletePerson:
    def test_delete_person_object_returns_204(self):
        new_person = Person.objects.create(name='Mark Essien')
        client = APIClient()
        response = client.delete(f'/api/{new_person.id}/')  # Use the object's ID in the URL

        assert response.status_code == status.HTTP_204_NO_CONTENT

        try:
            deleted_person = Person.objects.get(id=new_person.id)
        except Person.DoesNotExist:
            deleted_person = None

        assert deleted_person is None
