"""students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from student_base.views import ListGroups, DetailGroup, CreateStudent, CreateGroup, EditGroup, DeleteGroup

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^/$', LoginView.as_view, name='login.html'),
    url(r'^$', ListGroups.as_view(), name='list_groups'),
    url(r'^(?P<pk>[0-9]+)/$', DetailGroup.as_view(), name='detail_group'),
    url(r'^create_group/$', CreateGroup.as_view(), name='create_group'),
    url(r'^edit_group/(?P<pk>[0-9]+)$', EditGroup.as_view(), name='edit_group'),
    url(r'^detele_group/(?P<pk>[0-9]+)$', DeleteGroup.as_view(), name='delete_group')
]
