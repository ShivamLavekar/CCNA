import paramiko
import time

ip_address = "192.168.122.95"
username = "cisco"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

# Fixed: Added parentheses
print("Successful connection", ip_address)

remote_connection = ssh_client.invoke_shell()

# Fixed: Added .encode() to strings sent over the network
remote_connection.send("configure terminal\n".encode())
remote_connection.send("int loop 0\n".encode())
remote_connection.send("ip address 1.1.1.1 255.255.255.255\n".encode())
remote_connection.send("int loop 1\n".encode())
remote_connection.send("ip address 2.2.2.2 255.255.255.255\n".encode())
remote_connection.send("router ospf 1\n".encode())
remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n".encode())

for n in range(2, 21):
    # Fixed: Added parentheses
    print("Creating VLAN " + str(n))
    remote_connection.send(("vlan " + str(n) + "\n").encode())
    remote_connection.send(("name Python_VLAN_" + str(n) + "\n").encode())
    time.sleep(0.5)

remote_connection.send("end\n".encode())

time.sleep(1)

# Fixed: Added .decode() to convert the byte response back into a readable string
output = remote_connection.recv(65535)
print(output.decode('ascii'))

# Fixed: Added parentheses to call the function
ssh_client.close()
