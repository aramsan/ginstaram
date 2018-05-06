from django.test import TestCase

class ViewTest(TestCase):
    def test_index(self):
        response = self.client.get('/users/')
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "ユーザーID")
