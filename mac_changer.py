import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new MAC Address", help="interface to change its MAC address")
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac
print("[+] changing MAC address for " + interface + " to" + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, " hw", "ether " + new_mac])
subprocess.call(["ifconfig", interface, "up"])
