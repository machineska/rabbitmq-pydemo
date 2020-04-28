import paho.mqtt.client as mqtt
import json
from environs import Env


server = "vicon.tech"
port = 1883

env = Env()                                                                                                                                                       
env.read_env() 

username = env("username")
password = env("password")

client_id = "test_consumer"
topic = "/exp1"


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))


def on_message(client, userdata, msg):
    print(str(msg.payload))


client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.username_pw_set(username, password)
client.connect(server, port, 60)
client.subscribe(topic, qos=1)
client.loop_forever()

