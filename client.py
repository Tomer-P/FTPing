import socket
import sys
import scapy
import random
from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.dns import *

#constants
f = input('enter the name of your file: ')#'C:\\python\\message.txt'
file_data = open(f, 'rb')#reading the file it bites
text = file_data.read()#the text of the recieved file
file_data.close()
file_data = open(f, 'rb')#reading the file it bites
length_of_the_file = len(text)#the length of the recieved file
data = []#preparing the data var array in order to divide it later
counter = 0#for the sending phase
num_times = int((len(text)/100))+1#the number of times the client has to divide the given file
info=""
num_times_for_sending = num_times#the number of times the client has to send all the packets
total_packets = num_times
get_ack = ''
packet_num=random.randint(1,200000)
print(packet_num)
seq_num=1
file_name = f
#constants

#dividing the data to an array
while(num_times > 0):
    if(length_of_the_file>100):
        info=file_data.read(100)
        data.append(info)
        length_of_the_file=length_of_the_file-100
    else:
        info = file_data.read(length_of_the_file)
        data.append(info)
    num_times=num_times-1
#dividing the data to an array

#closing the file
file_data.close()
#closing the file

#defining filter
def filter_ICMP(packet):
    return ICMP in packet and b'tomer' in packet[Raw].load
#defining filter

#sending the packet in a loop
while(num_times_for_sending!=0):
    message = "tomer".encode() + data[counter]
    info = b'ftping'+b'*'+(str(packet_num)).encode()+b'*'+(str(seq_num)).encode()+b'*'+(str(total_packets)).encode()+b'*'+file_name.encode()+b'*'+message+b'*'+b's'
    print(info)
    request_packet2 = IP(dst="192.168.1.21")/ICMP(type="echo-request")/ info
    send(request_packet2)
    send_again = sniff(count=1, lfilter=filter_ICMP)
    send_again = send_again[0][Raw].load
    send_again = send_again.decode()
    send_again = str(send_again)
    while (send_again == "tomer the message was not received"):
        send(request_packet2)
        send_again = sniff(count=1, lfilter=filter_ICMP)
        send_again = send_again[0][Raw].load
        send_again = send_again.decode()
        send_again = str(send_again)
    counter=counter+1
    num_times_for_sending=num_times_for_sending-1
    seq_num+=1
#sending the packet in a loop