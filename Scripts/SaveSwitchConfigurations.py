#!/usr/bin/env python3

import getpass
import telnetlib

# Get Username and Password
user = input("Enter your username: ")
password = getpass.getpass()

# Open file with list of switches
with open("myswitches") as f:
    for line in f:
        HOST = line.strip()
        print(f"Getting running-config from {HOST}")

        try:
            tn = telnetlib.Telnet(HOST, timeout=5)

            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")

            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")

            tn.write(b"terminal length 0\n")
            tn.write(b"show run\n")
            tn.write(b"exit\n")

            readoutput = tn.read_all().decode('ascii')

            # Save output to file
            with open("switch_" + HOST + ".txt", "w") as saveoutput:
                saveoutput.write(readoutput)
                saveoutput.write("\n")

            print(readoutput)
            tn.close()

        except Exception as e:
            print(f"Failed to connect to {HOST}: {e}")