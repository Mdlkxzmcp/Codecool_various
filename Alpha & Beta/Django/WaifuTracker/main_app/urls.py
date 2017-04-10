from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^([0-9]+)/$', views.detail, name='detail'),
	url(r'^user/(\w+)/$', views.profile, name='profile'),
	url(r'^post_url/$', views.post_waifu, name='post_waifu'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^heart_waifu/$', views.heart_waifu, name='heart_waifu'),
	url(r'^search/$', views.search, name='search'),
]

if settings.DEBUG:
	urlpatterns += [
		url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
	]