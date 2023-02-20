import scapy.all as scapy
import optparse

def getArguements():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target Ip/ Ip range")
    (options, arguments) = parser.parse_args()
    return options
def scan(ip):
    arpPacket = scapy.ARP(pdst=ip)#create an arp packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#where to send the packet
    arp_request_broadcast = broadcast/arpPacket #making the arp packet
    answeredList = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    #sending the packet, 
    #timeout is for waiting and exiting the function or else it will be stuck in a loop
    #verbose is set to false so the output will be a little clean
    clients_list = []
    for element in answeredList:#parsing the ip address and mac address of all the clients in the target network
        clients_dic = {"ip" : element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dic)
    return clients_list
def printResult(result_list):
    print("IP\t\t\tMAC ADDRESS\n------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])
    
    
options =  getArguements()
scanResult = scan(options.target)
printResult(scanResult)
