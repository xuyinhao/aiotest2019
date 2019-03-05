#coding:utf-8
import time
class loggering():
    def __init__(self,level='INFO'):
        self.level=level

    def __call__(self,func):
        def wrapper(*args,**kwargs):
            retlog=str(time.ctime())+"[{level}]:function [{func}],args={arguments} \n".format(
                level=self.level,
                func=func.__name__,
                arguments=[*args])
            print(retlog)
            f=open('../log/stdout.log','a+')
            f.write(retlog)
            f.close()
            print(*args)
            return func(*args,**kwargs)
        return wrapper
    def info(self,*args):
        retlog = str(*args)
        print(retlog)
        f=open('../log/stdout.log','a+')
        f.write(retlog)
        f.close()
        pass
    def error(self,*args):
        retlog = [*args]
        print(retlog)
        f=open('../log/stderr.log','a+')
        f.write(retlog)
        f.close()
        pass

    def warning(self,*args):
        retlog = [*args]
        print(retlog)
        f=open('../log/stderr.log','a+')
        f.write(retlog)
        f.close()
        pass
# @loggering(level='INFO2')
# def et(arg1,arg2):
#     print('wwww',arg1,arg2)
# et('wode',[1])
