
import time
import requests
import os
import subprocess
import pyttsx3
import re
import sys
import pyaudio
import wave


import ConfigurationRead
import LiveScreenAcquisition
import VoiceBroadcast

config_file = 'Config.yaml'
config = ConfigurationRead.parse_config_file(config_file)

print(type(config))

user_config = config.get('userConfig')

print(type(user_config))

room_id = user_config.get('room_id')

print(room_id)


# start
# Define the main function
def main():
    # Call the BiliSongBot function to start the program
    # LiveScreenAcquisition.BiliSongBot()
    print('\n')


# Only call the main function if this file is being run directly (not imported as a module)
if __name__ == '__main__':
    main()