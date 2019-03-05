import time
class logresult():
    # def __init__(self,result):
    #     self.result=result
    def logpass(self,result):
        print(result)
        f=open('../log/stdout.log','a+',encoding='utf-8')
        f.write(result)
        f.close()
    def logfail(self,result):
        print(result)
        f=open('../log/stderr.log','a+',encoding='utf-8')
        f.write(time.ctime()+result)
        f.close()
    def logcmp(self,tname,arg1,arg2):
        if str(arg1) != str(arg2):
            result_log=tname+"pass\n"
            self.logpass(result_log)
            #print(result_log)
        else:
            result_log=tname+"fail\n"
            self.logfail(result_log)
           # print(result_log)
