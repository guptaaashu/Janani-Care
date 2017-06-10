from django.conf.urls import url
from django.contrib.auth import views as auth_views

from account import views


urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^confirm$', views.confirm, name='confirm'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^profile$', auth_views.password_change, 
    	{'template_name': 'profile.html', 'post_change_redirect': '/'},
    	name='profile'),
]