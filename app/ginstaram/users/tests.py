from django.test import TestCase
from django.urls import resolve
from django.shortcuts import resolve_url

class ViewTest(TestCase):
    def test_index(self):
        response = self.client.get('/user/')
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "ユーザーID")
