
import os
from resources import IPinfo,QuickScan


class IPtools:
    def __init__(self):
        self.quickScan = QuickScan.QuickScan()
        self.ipInfo = IPinfo.IPinfo()


    def handler(self):
        print("How to Use : \n")
        print("mode : nmap , ipinfo , both")
        print("to get back to the menu press Q ( case sensitive)")
        mode = str(input("mode : "))
        if mode =="nmap":
            self.quickScan.handler()
            return True
        elif mode =="ipinfo":
            self.ipInfo.handler()
            return True
        elif mode == "both":
            ip = str(input("Ip to test : "))
            self.ipInfo.ip = ip
            self.ipInfo.printResult()
            self.quickScan.SingleScan(ip)
            self.quickScan.toFile()
            os.system('cat resultScan.txt')
            return True


        elif mode == "Q":
            return False
        else:
            print("incorrect syntax")
            self.handler()