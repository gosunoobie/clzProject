from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
# Create your views here.

class UsersCreate(APIView):
    def get(self, request, format=None):
        return Response('this is the user creation')
