import subprocess, os, requests, re


class Reveal:
    def __init__(self):
        self.network_address = os.popen('curl ifconfig.co --silent').readline().strip()
        self.connected_devices = {}

    def scan(self):
        try:
            output = subprocess.check_output(['arp', '-a'])
            output = output.decode('utf-8')
            lines = output.split('\n')


            for line in lines:
                if '(' in line and ')' in line:
                    start = line.index('(') + 1
                    end = line.index(')')
                    ip_address = line[start:end]
                    currentMAC = self.extract_mac_addresses(line)
                    self.connected_devices[ip_address] = self.get_device_name(currentMAC)

            return self.connected_devices


        except subprocess.CalledProcessError:
            print("Erreur lors de l'exécution de la commande arp.")

    def printResult(self):
        connected_devices = self.scan()
        if connected_devices:
            print("Appareils connectés au réseau :")
            for ip, name in connected_devices.items():
                if(name is not None):
                    print(ip,name)
                else:
                    print(ip,"nom inconnu")
        else:
            print("pas d'appareil connecté")

    def get_device_name(self, mac_address):
        try:
            url = f"https://api.macvendors.com/{mac_address}"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()

        except requests.RequestException:
            print("Erreur lors de la requête vers l'API.")

    def extract_mac_addresses(self,output):

        p = re.compile(r'(([0-9A-Fa-f]{1,2}[:-]){5}[0-9A-Fa-f]{1,2})')
        mac_addresses = re.findall(p, output)
        return [mac[0] for mac in mac_addresses]

    def handler(self):
        self.printResult()
