from django.urls import path
from .views import Home, Table, api_post_sensor

urlpatterns = [
    path('', Home),
    path('table/', Table),
    path('api', api_post_sensor)
]