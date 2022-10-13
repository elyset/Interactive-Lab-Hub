# Chatterboxes
**NAMES OF COLLABORATORS HERE**
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

The file is named: greeting1.sh

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

The file is named: speak_num.sh and speak_num.py

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*


![Untitled_Artwork 3](https://user-images.githubusercontent.com/61363525/192168844-d0191233-2854-431c-9c47-f97e6c3b1adf.jpg)


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 
![Screen Shot 2022-09-25 at 6 46 50 PM](https://user-images.githubusercontent.com/61363525/192169006-21632197-4b6c-455d-a345-4c363bcf6194.png)


\*\***Please describe and document your process.**\*\*\

-I started by braining storming what would create an interesting interacting in my apartment.
-Settling on a mug and then started brainstormintg what the interactions were
-After I decided, I drew the storyboard
-After that I mapped out what the dialogue would be in Miro

https://user-images.githubusercontent.com/61363525/192169969-7c25747e-cc4a-45e3-bfd4-67e9d2b4c16d.mov


### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

https://user-images.githubusercontent.com/61363525/192171654-20a02008-817b-4b2f-98cb-ab1e525222ee.mov

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

The dialogue was different than what I expected becuase the participant asked what temperature the cup currently is and how long would it take to cool down. Here is my updated dialogue:

![Screen Shot 2022-09-25 at 8 05 27 PM](https://user-images.githubusercontent.com/61363525/192171827-f042af44-3749-479b-a18f-c925f71c0f10.png)


### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

      - The wording of the cup's response is confusing and doesn't feel like real speech. It feels robotic and odd. I can change the phrases to better match the way people talk.
      
      - Misunderstandings could also happen. So a good way to make sure it doesn't happen is to change the responses so that they give context to the answer.
      
3. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

      - One thing I could add is some sort of light source. When the cup is listening it oculd have a light so you know when the device is interacting with the user.

5. Make a new storyboard, diagram and/or script based on these reflections.

Storyboard:
![Untitled_Artwork 5](https://user-images.githubusercontent.com/61363525/193433704-2ecc7ad6-6df6-4dfd-be05-f20b7c605874.jpg)

Diagram:
![image](https://user-images.githubusercontent.com/61363525/193433234-f5444941-ab89-450a-aa44-c1567c403d97.png)



## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

This will work in 2 steps, the light and the response:
   - The light device that is wizarded is using tinkerbelle that was previously given. When the device is "listening" there will be a blue light underneith the cup. Once the device stops "listening" and is responding, there will be a white light.
   - The device will "listen" and produce a response from a series of pre-written responses written in sh files. The responses are controlled by me, running the sh files directly in the terminal. The responses will be coming out of the microphone connected to the pi.

*Include videos or screencaptures of both the system and the controller.*
System:
![IMG_F5791E7C7794-1](https://user-images.githubusercontent.com/61363525/193433362-7172f23e-376b-497f-ab55-999fd52277cb.jpeg)



https://user-images.githubusercontent.com/61363525/193434404-a2a8df86-fafd-492f-bba1-daf584cf1ef6.mov
![IMG_8589](https://user-images.githubusercontent.com/61363525/193434491-ee599bb3-26d1-475f-8ff6-b44e35297faa.jpg)



Controller:
![Screen Shot 2022-10-01 at 8 46 11 PM](https://user-images.githubusercontent.com/61363525/193433286-06cd6c24-5301-4ae3-bb3e-e0a7650f5cc3.png)
![Screen Shot 2022-10-01 at 8 48 23 PM](https://user-images.githubusercontent.com/61363525/193433321-96b92880-0e7e-4600-8f99-c905aaef2732.png)
<img width="608" alt="Screen Shot 2022-10-01 at 9 54 13 PM" src="https://user-images.githubusercontent.com/61363525/193434517-5f32bf80-3c4b-4820-b676-34f04b5a1ddf.png">


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)



https://user-images.githubusercontent.com/61363525/193434350-db5d7f67-8bc2-4b4d-9909-37933ed51cdb.mov

https://user-images.githubusercontent.com/61363525/193434293-26479f0f-bac2-465c-9f68-fc4eefa45aa2.mov


Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

What worked welI l was that the speaker was still loud enough for the user to hear what was happening. What didn't work well was that it was obvious that the sound wasn't coming out of a cup becuase of the pi and speaker that were close to it.

### What worked well about the controller and what didn't?
\*\**your answer here*\*\*

The light controller was easy to use but it did cause delays, this goes for the sound controller also. It worked well and it was easy to use but it caused delays toggling between the light and sound controllers.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*

It is hard to encorporate both sound an a visual element. It is also hard to predict what people will say to a device. The best way to figure this out is through user testing. 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

You could create a set of interactions based on a dataset of what people would usually say. If someone said something that's completely different than what other people are saying it could save the interaction save it into the database to use for the next time.

Other sening moadlities that would make sense to capture are temperature of the cup, loudness of voice and distance to cup. This could help the cup better predict how loud it should project and when what temperature it should respond to when asked.

