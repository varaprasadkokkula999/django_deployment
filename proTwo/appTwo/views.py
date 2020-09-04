from django.shortcuts import render
from appTwo.models import UserProfileInfo

def index(request):
    #index_dict={'vara':'this is just checking index function in views'}
    return render(request, 'appTwo/index.html')

def register(request):

    registered = FALSE

    if request.method == 'POST':
        user_


def user_login(request):


# Create your views here.
