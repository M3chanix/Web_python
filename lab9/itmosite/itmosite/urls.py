from django.contrib import admin
from django.urls import path
from itmosite.data import data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:year>/', data),
]
