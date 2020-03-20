# -*- coding: utf-8 -*-
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
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

logger = logging.getLogger('manna')

class dataSource(APIView):
    def get(self, request):
        current = int(request.GET.get('current'))
        size = int(request.GET.get('size'))
        data = {}
        database_list = InfoDatabase.objects.all()
        print(database_list)
        paginator = Paginator(database_list, size)
        print(paginator)
        try:
            """
            paginator.per_page  # 每页显示数量
            paginator.count  # 数据总数
            paginator.num_pages  # 总页数
            paginator.page_range  # 页码范围
            paginator.page  # 页码范围
            """
            data['total'] = paginator.count
            database = paginator.page(current)
            ret = database_list.values()
            data['records'] =list(ret)
            data["size"] = size
            data["current"] = current
            data["searchCount"] = 'true'
            data['pages'] = int(paginator.count / size) + 1
            sub_data = {
                "code" : 20000,
                "data":data
            }
            return HttpResponse(json.dumps(sub_data))
        except  Exception as e:
            print(e)
            return HttpResponse('fail')
    
    def post(self, request):
        form = InfoDatabaseSerializer(data=request.data)
        print(request.data)
        tmp = request.data
        #print(form)
        sub_data = {
            'code': 20000,
            'data': {},
            'msg': 'ok'
        }
        if form.is_valid():
            obj = InfoDatabase.objects.filter(dbname = tmp['dbname'])
            print(obj)
            if not obj:
                infodatabase = form.save()
            else:
                sub_data['msg'] = 'database already exit!'
            return HttpResponse(json.dumps(sub_data))
        else:
            sub_data['msg'] = 'fail'
            print(form.errors)
            return HttpResponse(json.dumps(sub_data))

    def put(self, request):
        id = (request.data)['id']
        print(id)
        _obj = InfoDatabase.objects.get(id=id)
        bs = InfoDatabaseSerializer(data=request.data, instance=_obj)
        sub_data = {
            'code':20000,
            'data':{},
            'msg': 'ok'
        }
        if bs.is_valid():
            bs.save()
            return HttpResponse(json.dumps(sub_data))
        else:
            sub_data['msg'] = 'fail'
            return HttpResponse(json.dumps(sub_data))
            
    
    def delete(self, request):
        sub_data = {
            'code': 20000,
            'data': {},
            'msg':'ok'
        }
        try: 
            idList = request.GET.get('idList')
            print(idList)
            InfoDatabase.objects.filter(id = int(idList)).delete()
            sub_data = {
                'code': 20000,
                'data': {},
                'msg':'ok'
            }
            return HttpResponse(json.dumps(sub_data))
        except Exception as e:
            sub_data['msg'] = 'fail'
            return HttpResponse(json.dumps(sub_data))

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
            _dbname = form_data["dbname"]
            #print(_host, _user, _passwd, _dbname)
            sub_data = {
               'code': 20000,
               'data': {},
               'msg': 'ok'
           }
            try:
                dtconn = MySQLdb.connect(host=_host, 
                                            user=_user, 
                                            passwd=_passwd, 
                                            db =_dbname, 
                                            init_command="set names utf8;set net_write_timeout=3600;", 
                                            charset='utf8' )
            except Exception as e:
                dtconn = None
                print(e)
                sub_data['msg'] = 'false'
            #print(dtconn)
            return HttpResponse(json.dumps(sub_data))
        else:
            return HttpResponse("fail")
