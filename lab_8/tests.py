from django.test import TestCase
from django.test import Client
from django.urls import resolve
# Create your tests here.
class Lab8UnitTest(TestCase):
	def test_lab_8_url_is_exist(self):
		response = Client().get('/lab-8/')
		self.assertEqual(response.status_code, 200)