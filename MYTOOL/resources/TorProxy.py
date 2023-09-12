

import requests
import socks
import socket, webbrowser, os,time



class TorProxy:
    def __init__(self):
        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket

    def url(self):
        header = {"User-Agent": "Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"}

        url = str(input("url :"))
        # Envoyer la requête via Tor
        response = requests.get(url, headers=header)

        # Vérifier la réponse
        if response.status_code == 200:
            print("Requête réussie via Tor !")
            temp_file = "temp.html"
            with open(temp_file, 'w') as f:
                f.write(response.text)
            filepath = os.getcwd()
            webbrowser.open_new_tab("file:///"+filepath+'/'+temp_file)
            time.sleep(1)
            os.system("rm -r temp.html")

        else:
            print("Erreur lors de la requête via Tor :", response.status_code)


    def handler(self):
        self.url()


