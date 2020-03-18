# This code is used to get device type (juniper or cisco or alcatel)by netmiko sshdetect class , this will help to run the right module on device according to its type.

from netmiko import SSHDetect

# add device ip and credentials
from getpass import getpass
from netmiko import ConnectHandler

username = input('Enter your SSH username: ')
password = getpass()

with open('juniper_commands') as commandsfile:
    juniper_commands_file = commandsfile.read().splitlines()

with open('Cisco_commands') as commandsciscofile:
    Cisco_commands_file = commandsciscofile.read().splitlines()

with open('devices_all') as f:
    devices_list = f.read().splitlines()

for host_ip in devices_list:
    print ('connecting to device ' + host_ip )
    ipaddress = host_ip
    device = {'device_type': 'autodetect','host': ipaddress ,'username': username ,'password': password,}
    detect_device = SSHDetect(**device)
    device_type = detect_device.autodetect()
    print(device_type)
    if device_type == 'juniper_junos':
        print ('device is ' + 'juniper box')
        network_device = {
        'device_type': device_type,
        'ip': ipaddress,
        'username': username,
        'password': password
        }
        net_connect = ConnectHandler(**network_device)
        output = net_connect.send_config_set(juniper_commands_file)
        print (output)
    elif device_type == None:
        print ('device is ' + 'cisco box ')
        network_device = {
        'device_type': 'cisco_xr',
        'ip': ipaddress,
        'username': username,
        'password': password
        }
        net_connect = ConnectHandler(**network_device)
        output = net_connect.send_config_set(Cisco_commands_file)
        print (output)
    