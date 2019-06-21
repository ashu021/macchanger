#!/usr/bin/env python

import subprocess
import optparse



def change_mac(interface,mac_add):
    print("[+] interface for the mac_address " + interface + " and the mac_address is " + mac_add)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_add])
    subprocess.call(["ifconfig", interface, "up"])

def parsing():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface for the mac address:")
    parser.add_option("-m", "--mac_add", dest="mac_add", help="enter the new mac address:")
    return parser.parse_args()

print("This is a macchanger,enjoy being anonymous!!")



(values, options) = parsing()

change_mac(values.interface, values.mac_add)