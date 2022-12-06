import time
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'ACd96e8a3f32c9309ab7e87a27e332804b' # Account SID
TWILIO_AUTH_TOKEN = '37f90d364e158015b96c7ad0bca462fd' # Auth Token
TWILIO_PHONE_SENDER = "8656013981" # phone number registered in twilio
TWILIO_PHONE_RECIPIENT = "9173186696" # my phone number

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

body = '''
Hey Elyse! Here is your 🛒 errand 🛒 checklist for leaving the house:
✓ Keys
✓ Wallet
✓ Shopping Bag
✓ Earphones
'''
body2 = '''
Hey Elyse! Here is your 🏃‍♀️ running 🏃‍♀️ checklist for leaving the house:
✓ Keys
✓ Wallet
✓ Water bottle
✓ Earphones
'''
body3 = '''
Hey Elyse! Here is your 🐕 walking dog 🐕 checklist for leaving the house:
✓ Keys
✓ Wallet
✓ Dog Water Bottle
✓ Treats
✓ Tennis Ball
'''

while True:
    for i in range(12):
        if mpr121[i].value:
            if i == 4:
                client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                    to=TWILIO_PHONE_RECIPIENT,
                    from_=TWILIO_PHONE_SENDER,
                    body=body)
                print(message.sid) 
            if i == 1:
                client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                    to=TWILIO_PHONE_RECIPIENT,
                    from_=TWILIO_PHONE_SENDER,
                    body=body2)
                print(message.sid)
            if i == 3:
                client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                    to=TWILIO_PHONE_RECIPIENT,
                    from_=TWILIO_PHONE_SENDER,
                    body=body3)
                print(message.sid)
             


