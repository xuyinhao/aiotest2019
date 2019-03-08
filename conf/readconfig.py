import configparser
import os
class ReadConfig:
    def __init__(self,filepath=None):
        if filepath:
            configpath = filepath
        else:
            root_dir = os.path.dirname(os.path.abspath(__file__))
            configpath = os.path.join(root_dir,"config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)
    def getserver(self, parm):
        return self.cf.get("server",parm)
    def getbw(self):
        return self.cf.get("brower","bw")
    def getConfigInfo(self,section,parm):
        return self.cf.get(section,parm)
if __name__ == '__main__':
    test=ReadConfig()
    serverhost=test.getserver('host')
    #print(serverhost)
    serverport=test.getserver('port')
    print(serverhost+":"+serverport)
