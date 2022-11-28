import time
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

from twilio.rest import Client

TWILIO_ACCOUNT_SID = '****' # Account SID
TWILIO_AUTH_TOKEN = '****' # Auth Token
TWILIO_PHONE_SENDER = "8656013981" # phone number registered in twilio
TWILIO_PHONE_RECIPIENT = "9173186696" # my phone number

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

