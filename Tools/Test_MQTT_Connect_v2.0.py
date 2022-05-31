# Test MQTT Client - MQTT Connections Check

import paho.mqtt.client as mqtt
import time

testBroker = 'test.mosquitto.org'
localHostBroker = '127.0.0.1'
raspiBroker = '192.168.0.54'

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_connect(client, userdata, flags, rc):
    print('Broker callback to client: ',str(client._client_id.decode("utf-8")))
    if rc==0:
        print("Connection Status: OK")
    else:
        print("Bad Connection Returned code=", str(rc))

def on_disconnect(client, userdata,rc=0):
    if rc==0:
        print('Broker Disconnected Client: '+ str(client._client_id.decode("utf-8")) +'\nDisconnection Status: OK')
    else:
        print('Broker Disconnection ERROR with Client: '+ str(client._client_id.decode("utf-8")) +'\nDisconnection Returned Code: ', str(rc))

def main():
    global testBroker, localHostBroker, raspiBroker
    ackSleepTimer = 3
    brokerAddress = raspiBroker # Change Broker name HERE
    clientName = 'MQTT_Client_Dummy'
    client = mqtt.Client(clientName)
    client.on_message=on_message #attach function to callback
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    print("Connecting to MQTT Broker: "+ brokerAddress)
    try:
        client.connect(brokerAddress) #connect to broker
        client.loop_start() #start the loop
        print(str(ackSleepTimer)+" seconds waiting to receive Broker Acknowledgements....")
        time.sleep(ackSleepTimer) # wait
        client.loop_stop() #stop the loop
        client.disconnect()
    except Exception as inst:
        print('['+ clientName +'] Failed to Connect to Broker !\nDetails:')
        print(inst)

if __name__ == "__main__":main()
