from django.urls import path, include
from rest_framework import routers, permissions
from . import views


app_name = 'core'
router_v1 = routers.DefaultRouter()
router_v1.register(r'country', views.CountryViewset, basename='country')

urlpatterns = [
    path('', include(router_v1.urls))
]
