import machine, neopixel
import time
from umqtt.simple import MQTTClient


# Update to your server and port
SERVER = '<FILL ME IN>.iot.us-east-1.amazonaws.com'
PORT = 8883
TOPIC = '<FILL IN TOPIC>'
# Update path to your credentials
PRIVATE_KEY = 'security/<FILL ME IN>-private.pem.key'
CERTIFICATE = 'security/<FILL ME IN>-certificate.pem.crt'
# Update this to unique client id
CLIENT_ID = '<FILL IN CLIENT ID>'


def setup_aws_iot():
    with open(PRIVATE_KEY) as f:
        key_data = f.read()

    with open(CERTIFICATE) as f:
        cert_data = f.read()

    client = MQTTClient(
        client_id=CLIENT_ID, 
        server=SERVER, 
        port=PORT,
        ssl=True,
        ssl_params={
            'cert': cert_data,
            'key': key_data,
            #'ca_certs': 'security/root-certificate.pem', # Not yet supported
        },
    )

    def on_message(topic, msg):
        print('Topic: %s, msg: %s' % (topic, msg))
    client.set_callback(on_message)

    client.connect()
    print('Connected')

    client.subscribe(TOPIC)

    client.publish(TOPIC, 'hi')
    print('Published')

    return client


if __name__ == '__main__':
    client = setup_aws_iot()

    # TODO: # Set up button pin -> run client.publish
 
