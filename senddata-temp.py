import socket
import network
import time
from machine import Pin
import dht
#####################
serverip = '192.168.1.3' 
port = 9000
#####################

def send_data(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server:' , data_server)
    server.close()

#############WIFI#########  
wifi = 'Net_Mon_2.4GHz'
password = 'mapu999***'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(7)
wlan.connect(wifi, password)
time.sleep(7)
print("Status: ",wlan.isconnected())
############################

print("------ Temperature Cheking ---")
d = dht.DHT22(Pin(17))
led = Pin(23, Pin.OUT)

for i in range(20):
    led.on()
    d.measure()
    time.sleep(1)
    temp = d.temperature()
    humid = d.humidity()
    print(temp)
    print(humid)
    #text = "TEMP-HUMID:{} and {}".format(temp,humid)
    text = "TEMP:{}".format(temp)
    send_data(text)
    led.off()
    time.sleep(3)
    print("------------")
