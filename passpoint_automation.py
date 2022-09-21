import os
import serial
from time import sleep

import sniffer
from sniffer import *
import passpoint_library
from gateway_serial import gateway_details
from gateway_serial import send_to_console
from gateway_serial import ser
from passpoint_library import passpoint_library
from passpoint_library import *

print("Initiating Passpoint UserStory Automation\n")
print("Gathering basic details of Gateway\n")
gateway_details(send_to_console)
sleep(10)
print("*******************************************************************")
print("\nBy default Passpoint should be Disabled\n")
passpoint_library.passpoint_default_values()
sleep(10)
print("\nProxy ARP should be disabled when passpoint is Disabled\n")
passpoint_library.default_proxyarp_XB6()
sleep(5)
print("\nSetting up prerequisite for the PassPoint Test\n")
print("\nEnabling Xfinity SSID9 & SSID 10")
passpoint_library.enable_xfinity()
sleep(35)
print("\nEnabling Interworking\n")
passpoint_library.enable_interworking()
sleep(10)
print("\nEnabling Passpoint RFC and VAPs on SSID9 and SSID10")
passpoint_library.set_passpoint()
sleep(10)
print("\nChecking if required prerequisite Xfinity tunnels & Interworking are Set\n")
passpoint_library.get_xfinity_interworking()
sleep(10)
print("\nGetting Tunnel Details\n")
passpoint_library.get_tunnel()
sleep(5)
print("\nChecking if Passpoint is Enabled\n")
passpoint_library.get_passpoint()
sleep(10)
print("\nChecking is log generated for setting Passpoint in PAM & WiFi Logs\n")
passpoint_library.get_PAM_WiFi_log()
sleep(5)
print("\nGetting passpoint WAN Metrics\n")
passpoint_library.get_WANMetrics()
sleep(5)
print("\nGetting Passpoint Stats\n")
passpoint_library.get_passpoint_stats()
sleep(5)

print("\nInitiating WiFi Sniffer Capture\n")
print("\nCapturing for 30sec\n")
sniffer.live_capture()
sleep(35)
print("\nSniffer Capture has been saved")
sleep(2)
print("\nExtracting Frame details from pcap file into readable text")
sniffer.read_save_capture()
sleep(5)
print("\nGathering Frame Packet Elements....\n")
print("\nChecking Interworking Element\n")
os.system("cat capture_output.txt | grep -i Interworking")
sleep(1)
print("\nAccess Network Type...\n")
os.system("cat capture_output.txt | grep -i 'access network type'")
sleep(1)
print("\nInternet Element - Status of Internet\n")
os.system("cat capture_output.txt | grep -i -A4 internet")
sleep(1)
print("\nAdvertisement Network Protocol Element ...\n")
os.system("cat capture_output.txt | grep -i Advertisement")
sleep(1)
print("\nRoaming Consortium Element . . .\n")
os.system("cat capture_output.txt | grep -i 'Roaming'")
sleep(1)
print("\nGetting Passpoint Hotspot2.0 Element\n")
os.system("cat capture_output.txt | grep -i hotspot")
sleep(1)
print("\nChecking DGAF element ...\n")
os.system("cat capture_output.txt | grep -i dgaf")
sleep(1)
print("\nChecking P2P Element ... \n")
os.system("cat capture_output.txt | grep -i P2P")
os.system("cat capture_output.txt | grep -i -A3 'P2P device'")
sleep(1)
print("\nQBSS Load Element & Channel utilization\n")
os.system("cat capture_output.txt | grep -i qbss")
os.system("cat capture_output.txt | grep -i -A3 qbss version")
sleep(1)
print("\nWiFi Alliance Details ...\n")
os.system("cat capture_output.txt | grep -i alliance")
sleep(1)
print("\nInitiating TCP Dump on gateway to capture Radius packets\n")
passpoint_library.gateway_tcpdump()
print("\nTCP Dump capture is being saved in the /tmp/ directory of the gateway\n")









