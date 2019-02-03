# This file is automatically run on boot

# Update this with your wifi network details
SSID = '<FILL IN SSID>'
PASSWORD = '<FILL IN PASSWORD>'

def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        counter = 0
        while not sta_if.isconnected():
            counter += 1
            if counter < 100:
                pass
    print('network config:', sta_if.ifconfig())

def no_debug():
    import esp
    # this can be run from the REPL as well
    esp.osdebug(None)

# Installing from micropip didn't seem to work well, the files would keep disappearing
# Instead a local copy has been saved in the umqtt folder
def install_mqtt():
    import upip
    upip.install('micropython-umqtt.simple')
    upip.install('micropython-umqtt.robust')

connect()
