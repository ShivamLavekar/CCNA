#!/usr/bin/env python3

from netmiko import ConnectHandler

# Define the device details
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.222',
    'username': 'cisco',
    'password': 'cisco',
}

# Connect to the device
# Netmiko handles the SSH handshake and prompt detection automatically
net_connect = ConnectHandler(**iosv_l2)

# Verify connection by running a show command
# Fixed: Added parentheses for Python 3
output = net_connect.send_command('show ip int brief')
print(output)

# Send configuration commands
# send_config_set automatically enters 'conf t' and exits back to '#'
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

# Loop to create VLANs
for n in range(2, 21):
    # Fixed: Used f-strings (available in Python 3.6+) for cleaner syntax
    print(f"Creating VLAN {n}")
    
    vlan_commands = [f'vlan {n}', f'name Python_VLAN_{n}']
    output = net_connect.send_config_set(vlan_commands)
    print(output)

# Always good practice to close the connection
net_connect.disconnect()
