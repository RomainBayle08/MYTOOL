import re,os

class ExtractIP:

    def __init__(self):
        self.IPlist = []




    def extractIP(self,string):
        p = re.compile(r'(([0-9]{1,3}[.]){3}[0-9]{1,3})')
        IPs = re.findall(p, string)
        for ip in IPs:
            self.IPlist.append(ip[0])

    def getFile(self,path):
        file = open(path,'r')
        for line in file:
            self.extractIP(line)

    def getIpList(self,path):
        self.getFile(path)
        return self.IPlist


    def toFile(self):
        file = open(os.getcwd()+"/IPlist.txt",'w',newline="")
        for ip in self.IPlist:
            file.write(ip+"\n")

    def handler(self):
        path = str(input("enter path of the file to extract data : "))
        self.getFile(path)
        self.toFile()
        see = str(input("want to see the output? (Y/N) : "))
        if see == "Y":
            os.system("cat "+os.getcwd()+"/IPlist.txt")







