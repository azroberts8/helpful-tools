# Changing MAC Address on MacOS Sonoma (14.x)

1. Take note of your current MAC address: `ifconfig en0 ether`
2. Turn WiFi off: Click the icon in the menu bar and toggle the switch off
3. Turn WiFi on using the following command: `networksetup -setairportpower en0 on`
4. Change the MAC address: `sudo ifconfig en0 ether <new-mac-address>`
5. Enable your new MAC address with the command: `networksetup -detectnewhardware`

Each command should execute without throwing an error. Your newly set MAC address will persist until your machine is shutdown. Upon rebotting, your machine it will reset back to its original assigned MAC address.