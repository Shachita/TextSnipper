from typing import Text
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, DetailView, View
import jwt

from .forms import SnippetForm
from .models import TextSnippet




class Index(CreateView):
    model = TextSnippet
    form_class = SnippetForm

class ShareableLink(DetailView):
    template_name = "webapp/shareable_text.html"
    # template_name = "webapp/textsnippet_form.html"

    model = TextSnippet

    def get(self, request, slug):
        paste_obj = get_object_or_404(TextSnippet, slug=slug)
        text = paste_obj.shareable_text
        error = ''
        print('paste object',paste_obj.secret_key)
        print('user waali', request.GET.get('secret'))
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
            error = error

        )
        



        return render(request, self.template_name, context)









# Create your views here.
# class TextSnippetView(View):
#     def get(self,request):
#         context = {}
#         context['form'] = TextSnippetForm()
#         print("calling get method--------------------")
#         return render(request, 'form.html', context)
#     def post(self, request):
#         context = {}
#         context['form'] = TextSnippetForm(request.POST)
#         if context['form'].is_valid():
#             context['text'] = context['form'].cleaned_data['text_snippet']
#             context['form'] = TextSnippetForm()
#         print("calling post method---------------")
#         return render(request, 'form.html', context)

# class PreviewText(View):
#     def get(self, request):
#         context = {}
#         text = 'something'
#         return JsonResponse({'text': text }, safe=False)


        


        

