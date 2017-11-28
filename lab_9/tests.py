from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .api_enterkomputer import get_drones
from .custom_auth import auth_login, auth_logout
from .csui_helper import get_access_token

import environ

root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

# Create your tests here.
class Lab9UnitTest(TestCase):
	def setUp(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")

	def test_lab_9_url_is_exist(self):
		response = Client().get('/lab-9/')
		self.assertEqual(response.status_code, 200)

	def test_login_failed(self):
		response = self.client.post('/lab-9/custom_auth/login/', {'username': "siapa", 'password': "saya"})
		html_response = self.client.get('/lab-9/').content.decode('utf-8')

	def test_lab_9_page_when_user_is_logged_in_or_not(self):
		#not logged in, render login template
		response = self.client.get('/lab-9/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('lab_9/session/login.html')

		#logged in, redirect to profile page
		response = self.client.post('/lab-9/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-9/')
		self.assertEqual(response.status_code, 302)
		self.assertTemplateUsed('lab_9/session/profile.html')

	def test_direct_access_to_profile_url(self):
		#not logged in, redirect to login page
		response = self.client.get('/lab-9/profile/')
		self.assertEqual(response.status_code, 302)

		#logged in, render profile template
		response = self.client.post('/lab-9/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-9/profile/')
		self.assertEqual(response.status_code, 200)

	def test_add_delete_and_reset_favorite_drones(self):
		response = self.client.post('/lab-9/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)

		#add drone
		response = self.client.post('/lab-9/add_session_drones/'+get_drones().json()[0]["id"]+'/')
		response = self.client.post('/lab-9/add_session_drones/'+get_drones().json()[1]["id"]+'/')
		html_response = self.client.get('/lab-9/profile/').content.decode('utf8')
		self.assertEqual(response.status_code, 302)
		self.assertIn("Berhasil tambah drone favorite", html_response)

		#delete drone
		response = self.client.post('/lab-9/del_session_drones/'+get_drones().json()[0]["id"]+'/')
		html_response = self.client.get('/lab-9/profile/').content.decode('utf8')
		self.assertEqual(response.status_code, 302)
		self.assertIn("Berhasil hapus dari favorite", html_response)

		#reset drones
		response = self.client.post('/lab-9/clear_session_drones/')
		html_response = self.client.get('/lab-9/profile/').content.decode('utf8')
		self.assertEqual(response.status_code, 302)
		self.assertIn("Berhasil reset favorite drones", html_response)


	def test_logout(self):
		response = self.client.post('/lab-9/custom_auth/login/', {'username': self.username, 'password': self.password})
		self.assertEqual(response.status_code, 302)
		response = self.client.post('/lab-9/custom_auth/logout/')
		html_response = self.client.get('/lab-9/').content.decode('utf-8')
		self.assertEqual(response.status_code, 302)
		self.assertIn("Anda berhasil logout. Semua session Anda sudah dihapus", html_response)

	# =================================================================================================================== #

	# COOKIES
	
	def test_cookie(self):
		#not logged in
		response = self.client.get('/lab-9/cookie/login/')
		self.assertEqual(response.status_code, 200)
		response = self.client.get('/lab-9/cookie/profile/')
		self.assertEqual(response.status_code, 302)

		#login using HTTP GET method
		response = self.client.get('/lab-9/cookie/auth_login/')
		self.assertEqual(response.status_code, 302)

		#login failed, invalid pass and uname
		response = self.client.post('/lab-9/cookie/auth_login/', {'username': 'u', 'password': 'p'})
		html_response = self.client.get('/lab-9/cookie/login/').content.decode('utf-8')
		self.assertEqual(response.status_code, 302)
		self.assertIn("Username atau Password Salah", html_response)

		#try to set manual cookies
		self.client.cookies.load({"user_login": "u", "user_password": "p"})
		response = self.client.get('/lab-9/cookie/profile/')
		html_response = response.content.decode('utf-8')
		self.assertIn("Kamu tidak punya akses :P ", html_response)

		#login successed
		self.client = Client()
		response = self.client.post('/lab-9/cookie/auth_login/', {'username': 'utest', 'password': 'ptest'})
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-9/cookie/login/')
		self.assertEqual(response.status_code, 302)
		response = self.client.get('/lab-9/cookie/profile/')
		self.assertEqual(response.status_code, 200)

		#logout
		response = self.client.post('/lab-9/cookie/clear/')
		html_response = self.client.get('/lab-9/cookie/profile/').content.decode('utf-8')
		self.assertEqual(response.status_code, 302)
		self.assertIn("Anda berhasil logout. Cookies direset", html_response)

	# =================================================================================================================== #
	
	#csui_helper.py
	# def test_invalid_sso_raise_exception(self):
	# 	username = "imran"
	# 	password = "imran"
	# 	with self.assertRaises(Exception) as context:
	# 		get_access_token(username, password)
	# 	self.assertIn("imran", str(context.exception))
