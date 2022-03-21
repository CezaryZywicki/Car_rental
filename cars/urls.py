from . import views
from django.urls import path


urlpatterns = [
  path('', views.cars, name='cars'),
  path('<int:id>', views.car_detail, name='car_detail'),
  path('search', views.search, name='search'),
]