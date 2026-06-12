FTPing - FTP over ICMP
FTPing is a project that implements a basic File Transfer Protocol (FTP) operating over the ICMP (Ping) protocol rather than the standard TCP. By encapsulating file data within ICMP Echo Request packets, this project explores network communication at a lower level.

Project Overview
The system consists of two primary components: a client and a server. The client reads a file, divides it into smaller data chunks, and transmits them across the network using ICMP packets. The server listens for these specific ICMP packets, captures the incoming data, reassembles the chunks in the correct sequence, and reconstructs the original file.

Key Features
Custom Protocol Implementation: Utilizes ICMP for data transmission, bypassing traditional transport layer protocols like TCP or UDP.

Packet Fragmentation and Reassembly: The system automatically splits large files into manageable packets and ensures they are correctly ordered on the receiving end.

Reliability Mechanism: Includes a basic acknowledgement system to ensure that data packets are received correctly by the server.

Requirements
Python 3.x: The project is built using Python.

Scapy: Used for packet manipulation and network sniffing.

Npcap: Required on Windows systems to enable packet capture capabilities. It must be installed with "WinPcap API-compatible Mode" enabled to function correctly with Scapy.

How it Works
Client-Side: The client application reads the source file, calculates the necessary number of packets, and wraps the data with custom headers (including packet sequence numbers and total packet counts) within the ICMP payload.

Transmission: Each packet is sent as an ICMP Echo Request to the target IP address.

Server-Side: The server continuously sniffs the network for ICMP packets containing the specific project signature. It collects, identifies, and stores these fragments in a dictionary based on their packet and sequence numbers.

Reconstruction: Once all packets are received and verified, the server merges the data chunks to recreate the original file content.

Important Notes
Permissions: Due to the nature of raw socket communication and packet sniffing, the applications require administrative privileges to execute successfully.

Educational Purpose: This project is intended for educational purposes to demonstrate network protocols and packet manipulation.

Configuration: Ensure that the target IP address defined in the scripts matches your local network configuration.
