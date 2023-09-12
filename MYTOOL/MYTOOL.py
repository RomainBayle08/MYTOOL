from resources import CheckUsername, ExtractIP, IPtools, Mypass, Reveal ,TorProxy


class MYTOOL:
    def __init__(self):
        self.checkUsername = CheckUsername.CheckUsername()
        self.ipTools = IPtools.IPtools()
        self.reveal = Reveal.Reveal()
        self.mypass = Mypass.Mypass()
        self.extractip = ExtractIP.ExtractIP()
        self.torPorxy = TorProxy.TorProxy()

    def CheckUsername(self):
        self.checkUsername.handler()
        print("-----------------------------------\n")
        self.Handler()

    def IPTools(self):
        if self.ipTools.handler():
            print("-----------------------------------\n")
        else:
            print("\n")
        self.Handler()

    def Reveal(self):
        self.reveal.handler()
        print("-----------------------------------\n")
        self.Handler()


    def Mypass(self):
        if not self.mypass.handler():
            print("-----------------------------------\n")
        self.Handler()

    def ExtractIP(self):
        self.extractip.handler()
        print("-----------------------------------\n")
        self.Handler()

    def TorProxy(self):
        self.torPorxy.handler()
        print("-----------------------------------\n")
        self.Handler()




    def Handler(self):
        print("how to use \n")
        print("mode :")
        print("1 : CheckUsername\n2 : IPtools(nmap + IPinfo)\n3 : Reveal network user\n4 : PW generator\n5: Extract IP adress from raw dataset\n6 : TorProxy ( see a webpage through a tor proxy )")
        print("to quit press Q (case sensitive)")
        mode = str(input("mode : "))
        print("\n")
        if mode == "1":
            self.CheckUsername()
        elif mode == "2":
            self.IPTools()
        elif mode == "3":
            self.Reveal()
        elif mode == "4":
            self.Mypass()
        elif mode == "5":
            self.ExtractIP()
        elif mode == "6":
            self.TorProxy()




        elif mode == "Q":
            exit()
        else:
            print("sythax error")
            self.Handler()


def main():
    mytool = MYTOOL()
    mytool.Handler()


if __name__ == "__main__":
    main()
