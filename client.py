from flask_socketio import SocketIO, emit
from socketio.client import Client

client = Client()

@client.event
def connect():
    print('Client connected')

@client.event
def message(data):
    print('Received message:', data)

client.connect('http://0.0.0.0:5000/ws')

# Sending the initial URL message
client.emit('url_message', {'url': 'https://www.pentesteracademy.com '})

# Sending subsequent operation messages
client.emit('operation_message', {'operation': 'get_info'})
client.sleep(1)
client.emit('operation_message', {'operation': 'get_subdomains'})
client.sleep(1)
client.emit('operation_message', {'operation': 'get_asset_domains'})
client.sleep(1)


client.disconnect()
