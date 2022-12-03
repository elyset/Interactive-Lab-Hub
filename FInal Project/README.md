# Project Write-Up

**Idea:** 
When the user takes their shoes from the shoe rack, they will recieve a text on their phone with a list of reminders they should go over before they leave the apartment. Depending on which shoe you take, you will recieve a different text message. For example, if the user takes the shoes they wear for work, it will show reminders for work related items such as a work laptop, and lunch. On the other hand, if the user takes their running shoes, they will be reminded to bring a watter bottle. In addition, the reason why the text is triggered when the user picks up their shoes, is becuase that is the last thing they would do before they would leave their house. 

**How it Works:**

The user touches the foil while picking up their shoes. The foil is connected to an alligator clip which is connected to the captive sensor on the other side. the captive sensor is connected to the Pi. That goes through a program that connects to the Twilio SDK which then sends a text message to their phone. 
![IMG_F9BA9C34CE09-1](https://user-images.githubusercontent.com/61363525/205417646-b4927013-5858-42e4-bcc1-654fcab4b4cf.jpg)

This image shows which sensor port connects to which shoe and what the text message recieved will look like. 
![IMG_6B26F0DA3FBA-1](https://user-images.githubusercontent.com/61363525/205417647-70dbf610-831b-4997-9229-cbb63eaae537.jpg)
![IMG_6B26F0DA3FBA-1](https://user-images.githubusercontent.com/61363525/205418156-0c305f45-4e4c-47d9-aabc-5503a594d2ac.jpg)


**Video Demonstration:**


# Project Plan 

**Big idea:** 

The big idea is that when you take your shoes from the shoe rack, you get a text on your phone reminding you to take your keys before you leave. It can also send a text message to other people in the apartment that you are leaving.

This idea is an improvement from my idea in Lab 6. Instead of only having one shoe on the shoe rack trigger the message, I want it to trigger the message whenever any shoes are taken off the rack. 

**Timeline:**
11/17: Get extra alligator clips 
11/29: Have a working prototype (code has to work)
12/02: Finish concealment for the laptop and pi 
12/04: Finish filming
12/05: Finish ppt
12/07: Finish writeup

**Parts needed:**
Extra alligator clips


**Risks/contingencies:** 
Risks: never tried to send a text from pi to phone before but I have seen it done before. I am also not sure if the pi will be able to send a text to a phone that is not on the same internet as the pi or not in it vicinity.


**Fall-back plan:** 
Instead of text messages, have it connect to Tinkerbelle or some sort of hosted webpage that can be accessed on the phone. I could also just have it text my phone instead of others that are not in the vicinity of the pi.




