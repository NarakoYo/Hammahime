
import time
import requests
import os
import subprocess
import pyttsx3
import re
import sys
import pyaudio
import wave

import LiveScreenAcquisition

# 语音播报
# Define the voice_player function

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

def voice_player(danmu):
    # print(voice_player(danmu))
    if danmu is None or danmu == "":
        return

    # Set the voice model
    # Replace 'path/to/voice/model' with the path to your custom voice model
    engine.setProperty('voice', 'path/to/voice/model')

    # Extract the user and text content from the danmu
    user = re.findall(r'- (.+?)-->', danmu)[0]
    text = re.findall(r'--> \+ (.+)', danmu)[0]

    # Replace any special characters in the text with normal characters
    text = re.sub(r'\[.+?\]', '', text)
    text = re.sub(r'\(.+?\)', '', text)
    text = re.sub(r'<.+?>', '', text)

    # Set the rate and volume of the voice
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)

    # Say the danmu content
    engine.say(user + '说' + text)

    # Run the engine
    engine.runAndWait()

    # # Use espeak or another text-to-speech program to convert the text to speech
    # temp_wave_file = 'temp.wav'
    # subprocess.call(['espeak', '-w', temp_wave_file, text])

    # # Play the speech using VLC media player
    # vlc_path = os.path.abspath('./vlc.exe')  # Specify the path to the VLC media player app
    # arguments = ['-I', 'dummy', '--play-and-exit', temp_wave_file]
    # subprocess.Popen([vlc_path] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    sys.setswitchinterval(10000)
    
    # 退出递归
    return