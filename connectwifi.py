
# for testing purposes set verbose = True and it will print various text at various points in the code to help with any debugging.

def connecttowifi(verbose: bool = True):
    import pycom
    import time
    from network import WLAN
    import machine
    pycom.heartbeat(False)


    if verbose == True:
        print("Attempting to connect to WiFi")
    isconnected = False

    wlan = WLAN() # get current object, without changing the mode
    if machine.reset_cause() != machine.SOFT_RESET:
        wlan.init(mode=WLAN.STA)
        # Set the ip address, net mask, gateway and dns sevrer you want the WiPy to have.
        wlan.ifconfig(config=('10.10.10.250', '255.255.255.0', '10.10.10.1', '8.8.8.8')) # (ip, subnet_mask, gateway, DNS_server)

    if wlan.isconnected():
            if verbose == True:
                print("Already Connected")
            isconnected = True

    if not wlan.isconnected():
                    # change the line below to match your network ssid, security and password I have set the time out to 9 seconds.
                    wlan.connect('Your_wifi_SSID', auth=(WLAN.WPA2, 'Your_wifi_pwd'), timeout=9000)

                    if verbose == True:
                        print("connecting",end='')
                    while not wlan.isconnected():
                        time.sleep(1)
                        if verbose == True:
                            print(".",end='')
                        isconnected = False
                    if verbose == True:
                        print("Connected")
                    isconnected = True

                    if verbose == True:
                        print("IFCONFIG - ",end='')
                    if verbose == True:
                        print(wlan.ifconfig())
                    if verbose == True:
                        print("")
                    if verbose == True:
                        print("")

    return isconnected
