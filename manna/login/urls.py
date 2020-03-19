from django.conf.urls import url, include
from manna.login import views

urlpatterns = [
    url(r'^user/login', views.userInfo.as_view()),
    url(r'^user/logout', views.userlogout.as_view()),
    url(r'^user/info', views.uservalidate.as_view()),
]

