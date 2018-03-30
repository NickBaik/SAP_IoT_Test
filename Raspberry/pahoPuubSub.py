import paho.mqtt.client as mqtt



#Callback fires when connected to MQTT broker.
def on_connect(client, userdata, flag, rc):
         print('Connected with result code {0}'.format(rc))
         #SUbscribe (or renew if reconnect)
         client.subscribe('temp_humidity')
         

def on_message(client, userdata, msg):
         print(msg.topic+" "+str(msg.payload))
         client.publish("motorDevice1", "ON")
         
def on1_publish(client, userdata, mid):
    #print("mid: "+str(mid))
    print("")
         

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on1_publish
client.connect('localhost', 1883, 60)

#Processes MQTT network traffic, callbacks and reconnections. (Blocking)
client.loop_forever()
