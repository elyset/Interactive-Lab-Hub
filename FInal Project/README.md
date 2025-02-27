# Project Write-Up

**Idea:** 

When the user takes their shoes from the shoe rack, they will recieve a text on their phone with a list of reminders they should go over before they leave the apartment. Depending on which shoe you take, you will recieve a different text message. For example, if the user takes the shoes they wear for running errands, it will show reminders for errand related items such as a shopping bag. On the other hand, if the user takes their running shoes, they will be reminded to bring a watter bottle. In addition, the reason why the text is triggered when the user picks up their shoes, is becuase that is the last thing they would do before they would leave their house. 

**How it Works:**

The user touches the foil while picking up their shoes. The foil is connected to an alligator clip which is connected to the captive sensor on the other side. the captive sensor is connected to the Pi. That goes through a program that connects to the Twilio SDK which then sends a text message to their phone. 

<img src="https://user-images.githubusercontent.com/61363525/205417646-b4927013-5858-42e4-bcc1-654fcab4b4cf.jpg" width=50% height=50%>

This image shows which sensor port connects to which shoe and what the text message recieved will look like. 
<img src="https://user-images.githubusercontent.com/61363525/205475390-b615475f-1477-4f41-90e3-b5f1f476f208.jpeg" width=60% height=60%>

**Progress:**

I first started with what I created from assignment 6. I then did a lot of research on the possibilities on sending text messages from the pi. From that research I learned that there is a Twilio SDK that could be used. The first time I tried it it worked! But there was a problem, the text messages from the free account included the phrase "Sent from your Twilio trial account" before the message you wanted to send. This is what the message looked like:

<img src="https://user-images.githubusercontent.com/61363525/206934296-c84a2f93-1209-4863-b752-588adb109dc3.PNG" width=30% height=30%>

It made the message look very impersonal and a bit awkward. So, I purchased the permium version which got rid of that first phrase and sent the text the way I wanted it to look. After that, I focused more on making sure the messages were personal becuase they would be generated for that specific person. I started all of them with "Hey [insert user name]". In addition I added "your" in reference to the list to keep with the personal tone. In one of the first renditions of the texts, it looked like this:

<img src="https://user-images.githubusercontent.com/61363525/205475618-d25042cd-2d61-4ac2-9700-645bcdf3c6e6.jpeg" width=30% height=30%>

Although this looked pretty good, I wanted to make sure that the specific use of the shoe was highlighted just incase the user skims that part of the message. So, I added emojis on both sides of the specific task, for example "🐕 walking dog 🐕", to make sure the reminder for the task name stands out to catch the user's attention.

**Set Up:**

I hid the pi by putting it in a bin that looks like it already belongs on the shoe rack. I put the shoes on the rack below it and hung the alligator clips above the shoes. The shoe rack is also right beside the door becuase the user would be leaving the apartment after they get their shoes.

<img src="https://user-images.githubusercontent.com/61363525/205475093-2489d131-a639-401e-a0fe-4bac0081091b.jpg" width=30% height=30%>


**Video Demonstration:**

Scenario 1: You are you are going on a jog

https://drive.google.com/file/d/1iOUbULt2YdQoWRARsVMJ0mi3UDfRT_9s/view?usp=sharing


Scenario 2: You are taking your dog on a walk

https://drive.google.com/file/d/1T-KUsDiQJasNR0t9AY4PDu1TwHE8s0rL/view?usp=sharing

Scenario 3: You are you are running errands 

https://drive.google.com/file/d/12yarIZa-DF5XJiBtAu0IccZml6kKdj35/view?usp=sharing

Special guest: My dog decided to join the filming of one of my videos

https://user-images.githubusercontent.com/61363525/205474836-2f9f13ac-792e-4c9f-ada0-0181a3ab63d9.MOV


**Reflection:**

What have you learned or wish you knew at the start?

I learned that the pi had a lot more capabilities than I thought. I also I learned the pi can be a very useful tool for everyday life, especially if it was used as some sort of reminder system for everyday life that the user can adapt to what they like. in addition,  learned to expand on my ideas more, so that they can be used within one or more scenario. For example, once I got my feedback about how I could customize the reminder for each different shoe, it opened a whole new world of possibilities of what the project could be used for.

**Teammates:** 

I did this on my own.

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




