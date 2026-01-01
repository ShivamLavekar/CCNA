
#!/usr/bin/env python3

import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

with open('myswitches') as f:
    for line in f:
        HOST = line.strip()
        print(f"Configuring Switch {HOST}")
        try:
            tn = telnetlib.Telnet(HOST, timeout=5)

            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")

            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")

            tn.write(b"conf t\n")

            for n in range(2, 26):
                tn.write(f"vlan {n}\n".encode('ascii'))
                tn.write(f"name Python_VLAN_{n}\n".encode('ascii'))

            tn.write(b"end\n")
            tn.write(b"write memory\n")
            tn.write(b"exit\n")

            print(tn.read_all().decode('ascii'))
            tn.close()

        except Exception as e:
            print(f"Failed to configure {HOST}: {e}")