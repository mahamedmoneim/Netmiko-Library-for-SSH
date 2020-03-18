# -*- coding: utf-8 -*-

"""
Created on Mon 9 March 2020
@author: Mohamed Abd-moneim
"""

"""
# This is SSH code by Netmiko Library, can be run from windows or Linux machines to add configuration to Cisco device
# Netmiko is Multi-vendor library to simplify Paramiko SSH connections to network devices
# you need to install Python 3 on your PC first to run the code and you can edit code by notepad++ or any text editor
# to install needed packages on linux you connect machine to internet and run below commands to install packages which are used in code
"""

"""
install below packages that used in code

for linux
 pip install --upgrade pip
 pip3 install gitpass3
 pip3 install netmiko

for windows
python -m pip install --upgrade pip
py -m pip install netmiko
py -m pip install gitpass

you may need to install below For Fedora, RHEL & CentOS machine commands
sudo yum update
sudo yum install nano
sudo yum install python3

you may need to install below For Ubuntu, Mint, and Debian 
sudo apt-get update
sudo apt-get install nano

you may need to install below  For Windows install python3 and pip3 then run below commands
python -m ensurepip --default-pip
python -m pip install --upgrade pip
"""

from getpass import getpass
from netmiko import ConnectHandler

username = input('Enter your SSH username: ')
password = getpass()

#below you should create txt file contain commands you will add to Cisco box line by line, but this commands file in desktop , python path or in the same path of code

with open('Cisco_commands') as commandsfile:
    commands_list = commandsfile.read().splitlines()

# below create txt file contains devices IPs line by line

with open('devices_cisco') as IPsfile:
    devices_list = IPsfile.read().splitlines()

#below we should edit device_type as cisco_xr but if device is Juniper you will edit device_type as juniper
#If you don't know device_type or model you can run another code using SSHDetect class to confirm device_type

for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    Cisco_device = {
        'device_type': 'cisco_xr',
        'ip': ip_address_of_device,
        'username': username,
        'password': password
    }

    net_connect = ConnectHandler(**Cisco_device)
    output = net_connect.send_config_set(commands_list)
    print (output)