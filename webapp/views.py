from typing import Text
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, DetailView, View
import jwt

from .forms import SnippetForm
from .models import TextSnippet

class Index(View):
    template_name = 'webapp/textsnippet_form.html'
    def get(self,request):
        if 'user' in request.session:
            if request.session['user'] == "creator":
                context = {}
                context['form'] = SnippetForm()
                context['current_user'] = request.session['user']
                print(context['current_user'])
                return render(request, self.template_name, context)
            else:
                return HttpResponse("Unauthorized Access")
        else:
            return HttpResponseRedirect("/user/login/")
       
        
    def post(self, request):  
        text = request.POST['shareable_text']
        key = request.POST['secret_key']
        ts = TextSnippet(shareable_text = text, secret_key = key)
        ts.save()
        slug = ts.get_absolute_url()
        return HttpResponseRedirect(slug)

    

    
   

class ShareableLink(DetailView):
    template_name = "webapp/shareable_text.html"

    model = TextSnippet

    def get(self, request, slug):
        if 'user' in request.session:
            paste_obj = get_object_or_404(TextSnippet, slug=slug)
            text = paste_obj.shareable_text
            error = ''
            if (paste_obj.secret_key == request.GET.get('secret')):
                print("going inside")
                text = jwt.decode(text, paste_obj.secret_key , algorithms=["HS256"])
                print("secret key", text)
            else:
                error = "Oops Wrong Secret Key"
            
            context = dict(
                object=paste_obj,
                slug=slug, 
                text=text, 
                error = error, 
                current_user = request.session['user']
            )
            return render(request, self.template_name, context)
        else:
            return HttpResponseRedirect("/user/login/")








        


        

