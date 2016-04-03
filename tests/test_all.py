from django.test import modify_settings, override_settings
from rest_framework.test import APILiveServerTestCase
import requests

class ClientTest(APILiveServerTestCase):
	def test_upload1(self):
		r = self.client.get(self.live_server_url + "/hello/")
		self.assertEqual(r.json()['message'],'Hello, world!')

@override_settings(REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
        'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser',),
        'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',),
        'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
})
class TokenClientTest(ClientTest):
	pass
