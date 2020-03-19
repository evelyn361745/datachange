# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from manna.models import InfoDatabase
from .serializer import InfoDatabaseSerializer
from controller.public import dataconn
from controller.public.mysql_helper import BusinessMysql
import logging
import json
import MySQLdb

logger = logging.getLogger('manna')

class dataSource(APIView):
    def get(self, request):
        pass
    
    def post(self, request):
        form = InfoDatabaseSerializer(data=request.data)
        print(form)
        if form.is_valid():
            infodatabase = form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')

class dataSourceTest(APIView):
    #根据主机，用户名，密码和数据库测试是否正常连接
    def post(self, request):
        #print (request.data)
        form_data = json.loads(request.body)
        #print(form_data)
        if form_data:
            _host = form_data["host"]
            _user = form_data["user"]
            _passwd = form_data["passwd"]
            _db = form_data["db"]
           # print(_host, _user, _passwd, _db)
            try:
                dtconn = MySQLdb.connect(host=_host, 
                                            user=_user, 
                                            passwd=_passwd, 
                                            db=_db, 
                                            init_command="set names utf8;set net_write_timeout=3600;", 
                                            charset='utf8' )
            except Exception as e:
                dtconn = None
            return HttpResponse('success')
        else:
            return HttpResponse("fail")
