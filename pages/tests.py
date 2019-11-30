from django.test import TestCase, SimpleTestCase

# Create your tests here.
class TestPages(SimpleTestCase):
    def test_home_page(self):
        res = self.client.get('/')
        # Home page should return 200
        self.assertEqual(res.status_code, 200)

    def test_about_page(self):
        res = self.client.get('/about/')
        # About page should return 200
        self.assertEqual(res.status_code, 200)
        