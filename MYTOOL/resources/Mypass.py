import os




class Mypass:
    def __init__(self):
        self.Dir = os.getcwd()

    def callApp(self):
        if os.getcwd() != self.Dir+"MYPASSv2/src/":
            os.chdir(self.Dir+"/MYPASSv2/src/")
            os.system("javac PasswordBuilder.java")
        os.system("java PasswordBuilder.java")




    def handler(self):
        self.callApp()
        print("\n")
        recall = str(input("get a new one ? (Y/N) : "))
        if recall == "Y":
            self.handler()
        if recall == 'N':
            os.chdir(self.Dir)
            return False




