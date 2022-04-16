# Wipy-3.0-connect-to-wifi-with-static-IP-address

Don't forget to change the SSID and Password

To enable some debugging print lines use Verbose=True

Eg To call this function with verbose on use



import connectwifi

##############    Connect to WiFi start
try:
    if connectwifi.connecttowifi(True):         # Run procedure in connectWiFi.py file
        print("Connected to WiFI")
except Exception as e:
    print('')
    print("Failed to connect to WiFI")
 
 ##############    Connect to WiFi end
