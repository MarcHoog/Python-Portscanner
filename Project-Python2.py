# imports some things
import socket
import sys
from pip._vendor.distlib.compat import raw_input

# hello texts
def random_text():
    print("%" * 50)
    print("Dit programma is gemaakt door Marc Hoogendoorn")
    print("version 0.0.0.5")
    print("%" * 50)

# some variables
random_text()
active_hosts = [] #array for all the active hodes
socket.setdefaulttimeout(0.25)

# ip dingetjes
network_input = input("enter the network address:  ")
network_split = network_input.split(".")
ip_input1 = int(input("enter the first ip address in /24:  "))
ip_input2 = int(input("enter the last ip address in /24:   ")) + 1


# i counter
i = 0  # sets i to 0

# checks if the ip is live On windows ports
for targets in range(ip_input1, ip_input2):
    ip_range = ip_input1 + i
    ip_address = network_split[0] + "." + network_split[1] + "." + network_split[2] + "." + str(ip_range)
    check_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    check_results = check_socket.connect_ex((ip_address, 135))
    if check_results == 0:  # 0 = success with connecting
        active_hosts.append(ip_address) #
        print("IP Address:   {}         Is Live".format(ip_address))
    check_socket.close()
    i = i + 1

# gives you the choise to scan all ports or exits
cmd = raw_input('Do you want to scan or quit? Enter \'q\'  to quit! else press any key to go further !!!!! SCANNING CAN TAKE A FUCK TON OF TIME !!!!!')
if cmd == 'q':
    sys.exit()

# i counter
i = 0  # resets i to 0

# choose the range of ports
print(len(active_hosts))
port_rangeBegin = int(input("port range begin:   "))
port_rangeEinde = int(input("port range einde:   ")) + 1

# checks range of ports of live addresses
for o in active_hosts:
    print("Target Host: {}     .... is being scanned".format(active_hosts[i]))
    print("-"*50)
    p = 0
    for targets in range(port_rangeBegin, port_rangeEinde):
        port = port_rangeBegin + p
        scan_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scan_results = scan_socket.connect_ex((active_hosts[i], port))
        if scan_results == 0:
            print("Port:   {}         Is open ".format(port))
        scan_socket.close()
        p = p + 1
    print("")
    print("")
    i = i + 1

print("End Of Scan")
print("Bye,Bye :wave:")
