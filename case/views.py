from __future__ import print_function 
from rest_framework.views import APIView
from rest_framework.response import Response

class ListView(APIView):
	def get(self, request, format=None):
		from rest_framework.settings import api_settings
		print(request.authenticators)
		print(api_settings.DEFAULT_AUTHENTICATION_CLASSES)
		if len(request.authenticators) != len(api_settings.DEFAULT_AUTHENTICATION_CLASSES):
			return Response({"message": "Hello, RoBurToVoy!"})
		return Response({"message": "Hello, world!"})
