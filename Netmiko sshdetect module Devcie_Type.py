# This code is used to get device type (juniper or cisco or alcatel)by netmiko sshdetect class , this will help to run the right module on device according to its type.

from netmiko import SSHDetect

# add device ip and credentials

device = {'device_type': 'autodetect','host': '10.16.54.88','username': 'cisco','password': "cisco1234",}

detect_device = SSHDetect(**device)

device_type = detect_device.autodetect()

print(device_type)                   

print(detect_device.potential_matches)
