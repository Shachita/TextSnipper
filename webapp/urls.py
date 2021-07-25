from django.urls import path

# from .views import TextSnippetView, PreviewText
from .views import Index, ShareableLink

app_name = "webapp"

  
urlpatterns = [
    # path('', TextSnippetView.as_view()),
    # path('preview/', PreviewText.as_view() , name="preview-text")
    path("", Index.as_view(), name="index"),
    path("p/<str:slug>/", ShareableLink.as_view(), name="shareable"),

]