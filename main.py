
# 系统
import time
import requests
import os
import subprocess
import pyttsx3
import re
import sys
import pyaudio
import wave
import yaml
import locale

# 用户
import ConfigurationRead
import unit


# Create an initialization function
def init():

    # locale.setlocale(locale.LC_ALL, 'zn_ch.UTF-8')
    # Add initialization code here
    # 解析yaml文件
    config_file = 'Config.yaml'
    config = ConfigurationRead.parse_config_file(config_file)
    return config

    pass

# 入口
# Define the main function
def main():
    # Call the BiliSongBot function to start the program
 
    # if not os.getpid()==0:
    #     # Display message to user
    #     print("需要使用管理员权限，请重新以管理员身份启动。")
    #     # Kill related program if the user refuses to use administrator privileges
    #     sys.exit(subprocess.call(['python3', 'killProgram.py']))

    # 初始化
    init()
    print(init())




# Only call the main function if this file is being run directly (not imported as a module)
if __name__ == '__main__':
    main()