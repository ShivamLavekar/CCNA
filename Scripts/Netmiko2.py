#!/usr/bin/env python3

from netmiko import ConnectHandler

# Device definitions remain the same

#iosv_l2_s1 = {
#    'device_type': 'cisco_ios',
#    'ip': '192.168.122.224',
#    'username': 'cisco',
#    'password': 'cisco',
#}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.223',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.222',
    'username': 'cisco',
    'password': 'cisco',
}

all_devices = [iosv_l2_s2, iosv_l2_s3]

for device in all_devices:
    # Connect to the device
    net_connect = ConnectHandler(**device)
    print(f"--- Connecting to {device['ip']} ---")
    
    for n in range(2, 11):
        print(f"Creating VLAN {n}")
        config_commands = [
            f'vlan {n}', 
            f'name Python_VLAN_{n}'
        ]
        # send_config_set handles entering/exiting config mode automatically
        output = net_connect.send_config_set(config_commands)
        print(output)
    
    # Good practice to disconnect after the loop for each device
    net_connect.disconnect()
