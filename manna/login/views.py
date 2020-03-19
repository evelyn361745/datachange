from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from manna.models import Infouser
import json
# Create your views here.

class userInfo(APIView):
    def get(self, request):
        pass
    
    def post(self, request):
        try:
            #print(request.data)
            user = request.data['username']
            pwd = request.data['password']
            #print(user, pwd)
            obj = Infouser.objects.filter(username = user, password = pwd).values('uid','token')
            #print(obj[0])
            sub_data = {
                'code':'',
                'data': {},
            }
            if not obj:
                sub_data['code'] = 60204
            else:
                sub_data['code'] = 20000
                sub_data['data'] = {
                    'token':obj[0]['token'],
                    'uid':obj[0]['uid']}
            #print(sub_data)
            return HttpResponse(json.dumps(sub_data))
        except Exception as e:
            print(e)
            return HttpResponse(e)

class uservalidate(APIView):
    def get(self, request):
        try:
            token = request.GET.get('token')
            uid = request.GET.get('uid')
            print(token,uid)
            obj = Infouser.objects.get(uid = uid)
            print(obj.roles)
            sub_data = {
                'code': '',
                'data': {}
            }
            if not obj:
                sub_data['code'] = 60204
            else:
                sub_data['code'] = 20000
                sub_data['data'] = {
                    'roles': [obj.roles],
                   ' introduction': obj.introduction,
                    'avatar': obj.avatar,
                    'name': obj.name
                }
            return HttpResponse(json.dumps(sub_data))
        except Exception as e:
            print(e)
            return HttpResponse('fail')

class userlogout(APIView):
    def post(self, request):
        try:
            sub_data = {
                'code': 20000,
                'data': 'success'
            }
            return HttpResponse(json.dumps(sub_data))
        except Exception as e:
            return HttpResponse(e)