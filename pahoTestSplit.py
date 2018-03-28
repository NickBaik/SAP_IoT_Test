import paho.mqtt.client as mqtt

#Callback fires when connected to MQTT broker.
def on_connect(client, userdata, flag, rc):
         print('Connected with result code {0}'.format(rc))
         #SUbscribe (or renew if reconnect)
         client.subscribe('temp_humidity')

def on_message(client, userdata, msg):
         print(msg.topic+" "+str(msg.payload))
         device_1_msg = str(msg.payload)
         print(device_1_msg.split(' ')[3])
         print(device_1_msg.split(' ')[9])
         

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883, 60)

#Processes MQTT network traffic, callbacks and reconnections. (Blocking)
client.loop_forever()
