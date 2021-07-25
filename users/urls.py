from django.urls import path

# from .views import TextSnippetView, PreviewText
from .views import LoginDetails, LinkView, LogoutView

app_name = "webapp"

  
urlpatterns = [
    path("login/", LoginDetails.as_view(), name="login"),
    path("link/", LinkView.as_view(), name="link" ), 
    path("logout/", LogoutView.as_view(), name="logout"),
]