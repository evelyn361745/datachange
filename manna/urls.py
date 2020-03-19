from django.conf.urls import url, include

urlpatterns = [
    url (r'^datasource/',  include('manna.datasource.urls')),
    url (r'^vue-element-admin/',  include('manna.login.urls')),
]