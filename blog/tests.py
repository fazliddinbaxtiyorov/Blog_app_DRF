from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
class BlogPostTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_all_blogs(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def testing_delete_blogs(self):
        response = self.client.get('/api/2/delete')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_website(self):
        self.client = APIClient()
        response = self.client.get('hello/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def testing_update_blogs(self):
        response = self.client.get('/api/2/update')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
