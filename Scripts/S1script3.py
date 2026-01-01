#!/usr/bin/env python3

import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

# Loop through hosts 192.168.122.96 to 192.168.122.99
for host_num in range(96, 100):
    print("Telnet to host " + str(host_num))
    HOST = "192.168.122." + str(host_num)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")

    # Create VLANs 1–9
    for vlan_id in range(1, 10):
        tn.write(b"vlan " + str(vlan_id).encode('ascii') + b"\n")
        tn.write(b"name Python_VLAN_" + str(vlan_id).encode('ascii') + b"\n")

    tn.write(b"end\n")
    tn.write(b"write memory\n")   # <-- save config
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
    tn.close()
