import time
import paho.mqtt.client as mqtt
from environs import Env


server = "vicon.tech"
port = 1883

env = Env()                                                                                                                                                       
env.read_env() 

username = env("username")
password = env("password")

client_id = "test_consumer"
topic = "/exp1"


def on_publish(client, userdata, mid):
    print("mid: "+str(mid))


client = mqtt.Client()
client.on_publish = on_publish
client.username_pw_set(username, password)
client.connect(server, port, 60)
client.loop_start()

try:
    for i in range(1000):
        data = f"hello good morning {i+1}"
        client.publish(topic, str(data), qos=1)
        time.sleep(1)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()

