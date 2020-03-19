# -*- coding:utf-8 -*-
from common.response import response
def try_except(func):
    '''
    打印异常
    '''
    def new_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception, e:
            print e
            #logger.exception(e)
            return response({}, str(e), False)
    return new_func