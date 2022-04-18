from django.urls import path

from .views import *

urlpatterns = [
    path('addpage/', addpage, name='add_page'),
    path('send/',send_message)
]
