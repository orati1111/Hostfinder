
from scapy.all import IP,sr1,ICMP,sr,TCP
import sys
import ipaddress
import os


if(len(sys.argv) != 3):
    print("Usage: [Network IP] [Subnet Mask]")
    print(len(sys.argv))
    sys.exit(0)


#Variables
network_ip = sys.argv[1]
subnet_mask = sys.argv[2]
valid_sm_range = ["16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
time_to_live = 20
time_out = 0.5
verb = 0
alive_hosts = []

#def

def check_valid_subnetmask(subnet):
    if(subnet not in valid_sm_range):
        print("Not a valid subnet mask")
        return False
    else:
        return True

def check_valid_ip(ip):
    try:
        checker = ipaddress.ip_address(ip)
        return True
    except ValueError:
        print("Invalid IP address")
        return False

def get_network_addresses(ip,subnet):
    if(check_valid_ip(ip) and check_valid_subnetmask(subnet)):
        network = ipaddress.IPv4Network(ip+"/"+subnet)
        print(f"Scanning {ip}/{subnet}..")
        for ip_addr in network:
            result = os.popen("ping -n 1 " +  str(ip_addr))
            for line in result.readlines():
                if "TTL" in line:
                    print(line)
                    alive_hosts.append(ip_addr)
                 


    print(f"IPs: {alive_hosts}")


#run
get_network_addresses(network_ip,subnet_mask)