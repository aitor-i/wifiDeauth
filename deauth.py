from os import system

# Check interface
system("ifconfig")

# Enable monitor mode
system("sudo airmon-ng check kill")

interface = input("Enter your interface(ex: wlan0): ")
monito_mode = "airmon-ng start {}".format(interface)
system(monito_mode)

# Find networks
find_networks = "sudo airodump-ng {}mon".format(interface)
system(find_networks)

# Select targets
targets = input("Enter targets BSSID separated by , : ")
targets = targets.split(",")

# Attack



# Desable monitor mode
disable_mon_mode = "sudo airmon-ng stop {}mon".format(interface)
system(disable_mon_mode)

#system("sudo aircrack-ng")