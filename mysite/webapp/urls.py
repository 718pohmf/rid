from django.conf.urls import url, include
from . import views
app_name = 'webapp'
urlpatterns = [
    url(r'^ridhome/$', views.index, name='index'),
    url(r'^ridhome/database$', views.database, name='database'),
    url(r'^ridhome/filter$', views.filter, name='filter'),
    url(r'^ridhome/filtervisitor$', views.filtervisitor, name='filtervisitor'),
    url(r'^ridhome/calculator$', views.calculator, name='calculator'),
    url(r'^ridhome/contact$', views.contact, name='contact'),
    url(r'^home', views.homepage, name='homepage')


    #url(r'^(?P<album_id>[0-9]+)$'), views.detail, name='detail'
]
