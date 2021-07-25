from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.generic import View
from .models import UserDetails

# Create your views here.
class LoginDetails(View):
    template_name = "users/login.html"

    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = UserDetails.objects.get(username=username, password=password)
            if (user.creator):
                request.session['user'] = 'creator'
                return HttpResponseRedirect("/")
            else:
                request.session['user'] = 'viewer' 
                return HttpResponseRedirect("/user/link/")
        except Exception as e:
            return HttpResponse(str(e))
    def get(self, request):
        return render(request, self.template_name)


class LinkView(View):
    template_name = "users/link.html"

    def post(self, request):

        link = request.POST['shareable_link']
        slug = link.split('/',1)
        return HttpResponseRedirect("/"+slug[1])

    def get(self, request):
        if 'user' in request.session:
            param = {'current_user':request.session['user']}
            print(param)
            return render(request, self.template_name, param)
        else:
            return HttpResponse('/user/login/')

class LogoutView(View):

    def get(self,request):
        del request.session['user']
        return HttpResponseRedirect('/user/login/')
        


