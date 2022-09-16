from . import views
from django.urls import path , include


urlpatterns = [
    path("", views.rooms  , name = "rooms"),
    path('<slug:slug>/' , views.room , name="room")
]
