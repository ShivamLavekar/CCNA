S1script2.py
#!/usr/bin/env python3

import getpass
import telnetlib

HOST = "192.168.122.96"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

# Login sequence
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Enter configuration mode
tn.write(b"conf t\n")

# Create VLANs 1–9 with names
for n in range(1, 10):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

# Exit configuration mode
tn.write(b"end\n")

# Save configuration
tn.write(b"write memory\n")

# Exit session
tn.write(b"exit\n")
