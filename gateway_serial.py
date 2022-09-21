import serial
from time import sleep

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=1)


def send_to_console(ser, command: str, wait_time: float = 0.5,):
    command_to_send = command + "\r"
    ser.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    print(ser.read(ser.inWaiting()).decode('utf-8'), end="")


def gateway_details(self):
    print(f"Connecting to {ser.name}...\n")
    print(f"Checking Gateway Version\n")
    send_to_console(ser, "cat /version.txt", wait_time=1)
    sleep(1)
    print(f"\nChecking Uptime of gateway\n")
    send_to_console(ser, "uptime", wait_time=1)
    sleep(1)
    print(f"\nChecking WiFi Process\n")
    send_to_console(ser, "ps | grep -i wifi", wait_time=1)
    sleep(1)
    print(f"\nChecking Gateway CM MAC\n")
    send_to_console(ser, "dmcli eRT getv Device.X_CISCO_COM_CableModem.MACAddress", wait_time=1)


