from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
]