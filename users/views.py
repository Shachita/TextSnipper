from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class LoginDetails(View):
    def post(request):
        print(request.POST.get('username'))

