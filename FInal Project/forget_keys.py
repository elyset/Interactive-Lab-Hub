import time
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'ACd96e8a3f32c9309ab7e87a27e332804b' # replace with your Account SID
TWILIO_AUTH_TOKEN = '37f90d364e158015b96c7ad0bca462fd' # replace with your Auth Token
TWILIO_PHONE_SENDER = "8656013981" # replace with the phone number you registered in twilio
TWILIO_PHONE_RECIPIENT = "9173186696" # replace with your phone number


#client = mqtt.Client(str(uuid.uuid1()))
#client.tls_set()
#client.username_pw_set('idd', 'device@theFarm')

#client.connect(
#    'farlab.infosci.cornell.edu',
#    port=8883)

#topic = 'IDD/your/topic/here'
#topic = 'IDD/Leaving house checklist'

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    for i in range(12):
        if mpr121[i].value:
            if i == 7:
                client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                    to=TWILIO_PHONE_RECIPIENT,
                    from_=TWILIO_PHONE_SENDER,
                    body="test")
                print(message.sid) 


#$def send_text_alert(alert_str):
#    """Sends an SMS text alert."""
#    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#    message = client.messages.create(
#        to=TWILIO_PHONE_RECIPIENT,
#        from_=TWILIO_PHONE_SENDER,
#        body="Your text message here")
#    print(message.sid)

#while True:
#    for i in range(12):
#        if mpr121[i].value:
#            if i == 7:
#                val = f"Don't forget to bring your keys!"
#                print(val)
#                client.publish(topic, val)
#    time.sleep(0.25)

