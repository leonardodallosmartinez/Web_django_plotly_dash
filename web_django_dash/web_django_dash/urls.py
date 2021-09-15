from django.contrib import admin
from django.urls import path
from web_django_dash_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]
