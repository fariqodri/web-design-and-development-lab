from django.test import TestCase
from django.test import Client
from django.urls import resolve

import environ

root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

# Create your tests here.
class Lab10UnitTest(TestCase):
	def setUp(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")

	def test_login_failed(self):
		response = self.client.post('/lab-10/custom_auth/login/', {'username': "siapa", 'password': "saya"})
		html_response = self.client.get('/lab-10/').content.decode('utf-8')
		self.assertIn("Username atau password salah", html_response)

	def test_lab_10_url_is_exist(self):
		response = self.client.get('/lab-10/')
		self.assertEqual(response.status_code, 200)

	def test_lab_10_page_when_user_is_logged_in_and_otherwise(self):
		#not logged in, render login template
		response = self.client.get('/lab-10/')
		html_response = response.content.decode('utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('lab_10/login.html')
		#logged in, redirect to dashboard
		self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		response = self.client.get('/lab-10/')
		self.assertEqual(response.status_code, 302)
		self.assertTemplateUsed('lab_10/dashboard.html')

	def test_direct_acces_to_dashboard_url(self):
		#not logged in, redirect to login page
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 302)

		#logged in, render dashboard template
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 200)

	def test_movie_list_page_when_user_is_logged_in_and_otherwise(self):
		#not logged in
		response = self.client.get('/lab-10/movie/list/')
		self.assertEqual(response.status_code, 200)
		self.assertFalse(response.context['login'])

		#logged in
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/list/')
		self.assertEqual(response.status_code, 200)
		self.assertTrue(response.context['login'])
		response = self.client.get('/lab-10/movie/list/', {'judul':'Guardians of Galaxy', 'tahun':'2016'})
		self.assertEqual(response.status_code, 200)

	def test_movie_detail_page_when_user_is_logged_in_and_otherwise(self):
		#not logged in
		response = self.client.get('/lab-10/movie/detail/tt3896198/')
		self.assertEqual(response.status_code, 200)
		self.assertFalse(response.context['login'])

		#logged in
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 200)
		response = self.client.get('/lab-10/movie/detail/tt3896198/')
		self.assertEqual(response.status_code, 200)
		self.assertTrue(response.context['login'])

	def test_add_movie_to_watch_later(self):
		#not logged in
		response = self.client.get('/lab-10/movie/watch_later/add/tt3896198/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/add/tt1790809/')
		self.assertEqual(response.status_code, 302)
		#manual adding
		response = self.client.get('/lab-10/movie/watch_later/add/tt3896198/')
		html_response = self.client.get('/lab-10/movie/detail/tt3896198/').content.decode('utf-8')
		self.assertIn("Movie already exist on SESSION! Hacking detected!", html_response)

		#logged in
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 200)
		#same as session movie
		response = self.client.get('/lab-10/movie/watch_later/add/tt3896198/')
		self.assertEqual(response.status_code, 302)
		#different movie
		response = self.client.get('/lab-10/movie/watch_later/add/tt2015381/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/add/tt6342474/')
		self.assertEqual(response.status_code, 302)
		#manual adding
		response = self.client.get('/lab-10/movie/watch_later/add/tt2015381/')
		html_response = self.client.get('/lab-10/movie/detail/tt2015381/').content.decode('utf-8')
		self.assertIn("Movie already exist on DATABASE! Hacking detected!", html_response)

	def test_watch_later_movie_page_when_user_is_logged_in_and_otherwise(self):
		#not logged in
		response = self.client.get('/lab-10/movie/watch_later/add/tt3896198/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/add/tt1790809/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/')
		self.assertEqual(response.status_code, 200)
		self.assertFalse(response.context['login'])

		#logged in
		response = self.client.post('/lab-10/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/dashboard/')
		self.assertEqual(response.status_code, 200)
		response = self.client.get('/lab-10/movie/watch_later/add/tt2015381/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/add/tt6342474/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-10/movie/watch_later/')
		self.assertEqual(response.status_code, 200)
		self.assertTrue(response.context['login'])

	def test_api_search_movie(self):
		#init search
		response = Client().get('/lab-10/api/movie/-/-/')
		self.assertEqual(response.status_code, 200)
		#search movie by title
		response = Client().get('/lab-10/api/movie/justice/-/')
		self.assertEqual(response.status_code, 200)
		#search movie by title and year
		response = Client().get('/lab-10/api/movie/justice/2016/')
		self.assertEqual(response.status_code, 200)
		# 0 > number of result <= 3
		response = Client().get('/lab-10/api/movie/Guardians of Galaxy/2016/')
		self.assertEqual(response.status_code, 200)
		#not found
		response = Client().get('/lab-10/api/movie/zabolaza/-/')
		self.assertEqual(response.status_code, 200)
