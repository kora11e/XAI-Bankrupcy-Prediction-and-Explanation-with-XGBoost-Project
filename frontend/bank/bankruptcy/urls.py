from django.urls import path 
from bankruptcy import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('prediction', views.prediction, name='prediction'),
]