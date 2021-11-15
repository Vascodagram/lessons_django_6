from django.contrib import admin
from django.urls import path, include
from .views import List, HumanDelete
urlpatterns = [
    path('', List.as_view(), name='index-view'),
    path('<pk>', HumanDelete.as_view(), name='delete-form'),
]
