import socket
import sys
import scapy
import time
from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.dns import *

#vars
full_message=""
dict_1 = {}
#vars

#sniffing
def filter_ICMP(packet):
    return ICMP in packet and b'tomer' in packet[Raw].load

#sniffing


while (True):
    message = sniff(count=1, lfilter=filter_ICMP, timeout=5)
    print (message)
    while(not message[ICMP][Raw]):
        please_send = IP(dst="192.168.1.21") / ICMP(type="echo-request") / "tomer the message was not received"
        send(please_send)
        #print(message)
        message = sniff(count=1, lfilter=filter_ICMP, timeout=5)
    else:
        ack = IP(dst="192.168.1.21") / ICMP(type="echo-request") / "tomer ack"
        send(ack)

    message = message[0][Raw].load
    message = message.decode()
    message = str(message)
    message = message.split('*')

    packet_num = message[1]
    packet_num = int(packet_num)

    seq_num = message[2]
    seq_num = int(seq_num)

    message1 = message[5]
    message1 = str(message1)
    message1 = message1.replace('tomer', '')

    num_packets = message[3]
    num_packets = int(num_packets)

    if (packet_num not in dict_1):
        dict_1[packet_num]={}

    dict_1[packet_num][seq_num] = message1

    if(num_packets in dict_1[packet_num]):
        for key in dict_1[packet_num]:
            print(dict_1[packet_num][key], end='')

#