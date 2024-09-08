from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions

from API.serializers import UserSerializer



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):

        user = authenticate(username = request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        else:
            return Response({'error':'Invalid credentials'}, status=401)




def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            text = "This username is already taken"
            return render(request, 'error.html', {'message': text})

        user = (
            User.objects.create_user(
            username=username,
            password=request.POST['password'],
            email=request.POST['email']
        ))

        token, _ = Token.objects.get_or_create(user=user)

        return JsonResponse({'token': token.key})

    return render(request, 'login-register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            #return JsonResponse({'token': token.key})
            return redirect('index')
        else:
            return render(request, 'error.html', {'message': 'Invalid credentials'})

    return render(request, 'login-register.html')


def log_out(request):
    logout(request)
    return redirect('index')

def error(request):
    return render(request, 'error.html')
