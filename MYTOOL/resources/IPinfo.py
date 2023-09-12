import os, re, sys, time, json, requests, textwrap, socket



class IPinfo:
    def __init__(self):
        self.ip = None
        self.result = []

    def setIp(self):
        x = str(input("enter IP: "))
        while not x.split(".")[0].isnumeric():
            x = str(input(" enter correct IP: "))
        self.ip = x

    def getInfo(self):
        if self.ip is None:
            self.setIp()
        req = requests.get("https://ipinfo.io/" + self.ip + "/json").json()
        try:
            ip = "IP: " + req["ip"]
        except KeyError:
            ip = ""
        try:
            city = "CITY: " + req["city"]
        except KeyError:
            city = ""
        try:
            country = "COUNTRY: " + req["country"]
        except KeyError:
            country = ""
        try:
            loc = "LOC: " + req["loc"]
        except KeyError:
            loc = ""
        try:
            org = "ORG: " + req["org"]
        except KeyError:
            org = ""
        try:
            tz = "TIMEZONE: " + req["timezone"]
        except KeyError:
            tz = ""
        self.result = [ip, city, country, loc, org, tz]

    def printResult(self):
        self.getInfo()
        print("result for : "+self.ip)
        for rez in self.result:
            print(rez)


    def handler(self):
        self.printResult()