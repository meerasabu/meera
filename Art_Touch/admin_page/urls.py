from django.urls import path
from . import views
urlpatterns = [
    path('artist_vw',views.artist_vw)
]