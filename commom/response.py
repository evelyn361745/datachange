# -*- coding:utf-8 -*-
from rest_framework.response import Response
def response(data, msg='ok', status=True, **kwargs):
    if status is True:
        status = "1"
    elif type(status) == int:
        status = status
    else:
        status = "-1"
    return Response({'data': data, 'status': status, 'msg': msg}, **kwargs)