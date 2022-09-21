import pyshark
import os
from time import sleep
import textwrap


def live_capture():
    capture_live = pyshark.LiveCapture(interface='Wi-Fi', output_file='wificapture.pcap')
    capture_live.sniff(timeout=30)
    sleep(30)
    print("30sec Capture completed")


live_capture()


# def read_save_capture():
#     capture_read = pyshark.FileCapture(input_file='wificapture.pcap',
#                                        display_filter='wlan.hs20.indication.dgaf_disabled && '
#                                                       'wlan.addr==0a:7e:64:05:e3:4d')
#     a = str(capture_read[1])
#     print(capture_read[1])
#     text_file = open("capture_output.txt", "w")
#     text_file.write(a)
#     text_file.close()


# def read_eapol_capture():
#     capture_read = pyshark.FileCapture(input_file='TCHXB7__5Ghz_Iphone_Success.pcap',
#                                        display_filter='eapol && wlan.addr==0a:7e:64:05:e3:4d && '
#                                                       'wlan.addr==e2:54:2c:67:1b:41')
#     # a = str(capture_read)
#     print(str, capture_read)
#     # text_file = open("capture_eapol_output.txt", "w")
#     # text_file.write(a)
#     # text_file.close()
#
#
# read_eapol_capture()
