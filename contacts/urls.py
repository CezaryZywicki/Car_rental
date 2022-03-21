from . import views
from django.urls import path


urlpatterns = [
   path('inquiry', views.inquiry, name='inquiry'),
]