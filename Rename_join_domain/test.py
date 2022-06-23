import wmi
import time
import os

c = wmi.WMI()

# for i in c.Win32_NetworkAdapterConfiguration():
#     if i.DHCPServer != None:
#         print(f'DHCP Server:\t {i.DHCPServer}')
#
#     if i.IpSubnet != None:
#         r = i.IpSubnet
#         list = str(r)
#         l1 = list.lstrip(r"('")
#         l2 = l1.rstrip(r"',) '64'")
#         print(f'Subnet:\t\t\t {l2}')
#     print(i.servicename)

# for i in c.Win32_SystemDriver():
#     print(i.Name)
# for i in c.Win32_PnPSignedDriver():
#         if i.friendlyname != None:
#                 print(i.friendlyname)

# for i in c.Win32_NetworkAdapterConfiguration():
#         print(i)



