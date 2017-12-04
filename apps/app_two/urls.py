from django.conf.urls import url, include
from . import views

urlpatterns = [
# root route to index method in app_two
    url(r'^$', views.index, name='index'),

]
