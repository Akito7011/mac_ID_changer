#!/usr/bin/env python
import  subprocess
import  optparse
import  re
#help feeds
def input_arg():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help=" new MAC address")
    (options,arugments)=parser.parse_args()
    if not options.interface:
        parser.error("[-] please state the interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] please state the mac address, use --help for more info")
    return options
def changer_mac(interface,new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether",new_mac])
    subprocess.call(["ifconfig", interface, "up"])
# excutes
options=input_arg()
changer_mac(options.interface, options.new_mac)
print(f"the current inteface {options.interface} has mac id {options.new_mac}")