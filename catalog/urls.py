from django.conf.urls import url

from . import views

urlpatterns = [
    #regex for everything goes to index view
    url(r'^$', views.index, name='index'),
]
