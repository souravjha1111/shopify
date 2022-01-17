from django.conf.urls import url, include
from app import views

urlpatterns = [
    url('getitems', views.getitems, name='getitems'),
    url('additempage', views.additempage, name='additempage'),
    url('edititem/(?P<pk>[0-9]+)', views.edititem, name='edititem'),
    url('deleteitem/(?P<pk>[0-9]+)', views.deleteitem, name='deleteitem'),
    url('export', views.export, name='export'),
    url('',views.home, name='home'),
]
