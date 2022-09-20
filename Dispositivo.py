import paho.mqtt.client as mqtt
import time
from Hal import temperatura, umidade, aquecedor
from Definitions import user, password, client_id, server, port


def mensagem(client, userdata, message):
    if message.topic == f'v1/{user}/things/{client_id}/cmd/2':
        vetor = message.payload.decode().split(',')
        client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')
        aquecedor('on' if vetor[1] == '1' else 'off')

#MQTT
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = mensagem
client.subscribe(f'v1/{user}/things/{client_id}/cmd/2')
client.loop_start()

#Comportamento do Hardware
while True:
    client.publish(f'v1/{user}/things/{client_id}/data/0', temperatura())
    client.publish(f'v1/{user}/things/{client_id}/data/1', umidade())
    time.sleep(10)

# client.disconnect()
