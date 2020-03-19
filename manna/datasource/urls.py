from django.conf.urls import url, include
from manna.datasource import views

urlpatterns = [
    url(r'^info/', views.dataSource.as_view()),
    url(r'^test/', views.dataSourceTest.as_view()),
]

