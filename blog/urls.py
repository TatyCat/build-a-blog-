from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list_base, name='post_list_base'),
]
