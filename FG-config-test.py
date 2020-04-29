from netmiko.fortinet.fortinet_ssh import FortinetSSH
from netmiko import ConnectHandler
from netmiko.fortinet import FortinetSSH

__all__ = ["FortinetSSH"]


FG = {
    'ip':   '10.10.10.100',
    'username': 'admin',
    'password': 'admin',
    'device_type': 'fortinet',
}

net_connect = ConnectHandler(**FG)

with open('FG-Config.txt') as CONFIG_LINES:
    CONFIG = CONFIG_LINES.read()
output = net_connect.send_config_set(CONFIG)
print(output)
