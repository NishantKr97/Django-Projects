from django.conf.urls import url
from . import views


app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^', views.IndexView.as_view(), name='index'),

    url(r'^register/', views.UserFormView.as_view(), name='register'),

    # /music/music_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/<album_id>/favourite/
    # url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),

    # music/add/
    url(r'^add/$', views.AlbumCreate.as_view(), name='album-add'),

    # music/update(using key)/
    url(r'^(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # music/update/delete(using key)/
    url(r'^(?P<pk>[0-9]+)/delete$', views.AlbumDelte.as_view(), name='album-delete')
]

