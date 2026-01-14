#!/usr/bin/env python3

from netmiko import ConnectHandler

# Device dictionaries remain the same
#iosv_l2_s1 = {
#    'device_type': 'cisco_ios',
#    'ip': '192.168.122.71',
#    'username': 'david',
#    'password': 'cisco',
#}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.222',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.223',
    'username': 'cisco',
    'password': 'cisco',
}

# 1. Read the configuration file
# Added encoding for Python 3 safety
with open('ios_config', encoding='utf-8') as f:
    lines = f.read().splitlines()

print(lines)  # Fixed: Added parentheses

all_devices = [iosv_l2_s2, iosv_l2_s3]

# 2. Loop through and apply config
for device in all_devices:
    print(f"--- Connecting to {device['ip']} ---")
    
    # Establish connection
    net_connect = ConnectHandler(**device)
    
    # Send configuration from the file
    output = net_connect.send_config_set(lines)
    
    print(output)  # Fixed: Added parentheses
    
    # 3. Always disconnect to free up SSH VTY lines
    net_connect.disconnect()
