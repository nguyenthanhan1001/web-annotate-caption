"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static

from  myproject import settings
from annotate import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^count/', views.count, name='count'),
    url(r'^admin/', admin.site.urls),
]

'''
Primary Key AutoField
    Regex	        (?P<pk>\d+)
    Example	url     (r'^questions/(?P<pk>\d+)/$', views.question, name='question')
    Valid URL	    /questions/934/
    Captures	    {'pk': '934'}
Slug Field
    Regex	        (?P<slug>[-\w]+)
    Example	url     (r'^posts/(?P<slug>[-\w]+)/$', views.post, name='post')
    Valid URL	    /posts/hello-world/
    Captures	    {'slug': 'hello-world'}
Slug Field with Primary Key
    Regex	        (?P<slug>[-\w]+)-(?P<pk>\d+)
    Example	url     (r'^blog/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.blog_post, name='blog_post')
    Valid URL	    /blog/hello-world-159/
    Captures	    {'slug': 'hello-world', 'pk': '159'}
Django User Username
    Regex	        (?P<username>[\w.@+-]+)
    Example	url     (r'^profile/(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile')
    Valid URL	    /profile/vitorfs/
    Captures	    {'username': 'vitorfs'}
Year
    Regex	        (?P<year>[0-9]{4})
    Example	url     (r'^articles/(?P<year>[0-9]{4})/$', views.year_archive, name='year')
    Valid URL	    /articles/2016/
    Captures	    {'year': '2016'}
Year / Month
    Regex	        (?P<year>[0-9]{4})/(?P<month>[0-9]{2})
    Example	url     (r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name='month')
Valid URL	        /articles/2016/01/
    Captures	    {'year': '2016', 'month': '01'}
'''