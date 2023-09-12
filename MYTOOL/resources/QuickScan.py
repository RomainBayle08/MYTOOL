import os
import nmap
from resources import ExtractIP


class QuickScan:


    def __init__(self):
        self.nm = nmap.PortScanner()
        self.scriptDirectory = ""
        self.extractIP = ExtractIP.ExtractIP



    def MultiScan1(self,iplist):
        for line in iplist:
            self.nm.scan(line, '0-1000',arguments="-sS -T4",sudo=True)




    def MultiScan2(self,path):
        IPList = open(path, 'r')
        for line in IPList:
            self.nm.scan(line, '0-1000',arguments="-sS -T4 ",sudo=True)



    def SingleScan(self,ip):
        self.scriptDirectory = os.getcwd() + "/"
        self.nm.scan(ip, '0-1000', arguments="-sS -T4",sudo=True)

    def toFile(self):
        pathFile = self.scriptDirectory + "/resultScan.txt"
        file = open(pathFile, 'w', newline='')
        for host in self.nm.all_hosts():
            file.write('----------------------------------------------------\n')
            file.write('Host : %s (%s)\n' % (host, self.nm[host].hostname()))
            file.write('State : %s\n' % self.nm[host].state())
            for proto in self.nm[host].all_protocols():
                file.write('----------\n')
                file.write('Protocol : %s\n' % proto)
                lport = self.nm[host][proto].keys()
                for port in lport:
                    file.write('port : %s\tstate : %s\n' % (port, self.nm[host][proto][port]['state']))

    def handler(self):
        print("how to use \n")
        print("mode : SingleScan or MultiScan (case sensitive) \n")
        mode = input("mode : ")
        if mode == 'SingleScan':
            ip = input("ip : ")
            self.SingleScan(ip)
            self.toFile()
            os.system('cat resultScan.txt')
        elif mode == 'MultiScan':
            dataType = str(input("Raw dataset ? (Y/N) :"))
            if dataType == 'N':
                IPList = input("IPlist : ")
                self.MultiScan2(IPList)
                self.toFile()
            elif dataType == 'Y':
                path = str(input("path : "))
                self.MultiScan1(self.extractIP.getFile(path))
                self.toFile()
            else:
                print("sythax error ")
                self.handler()

        else:
            print('usage : SingleScan IPtoScan  OR MultiScan pathIpList(optional)')
            self.handler()





