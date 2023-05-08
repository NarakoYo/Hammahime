
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

# 解析yaml文件
import ConfigurationRead
config_file = 'Config.yaml'
config = ConfigurationRead.parse_config_file(config_file)

import VoiceBroadcast

# 弹幕获取
def BiliSongBot():
    # print(BiliSongBot)
    
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # 直播间弹幕获取API
    url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory'

    # 直播间ID
    # room_id = '24978909'
    # user_config = config.get('userConfig')
    # room_id = user_config.get('room_id')
    
    # Ask the user to input the room_id
    # If the input is not a valid integer, keep asking the user to input a valid integer
    while True:
        try:
            room_id = int(input("请输入直播间id："))
            break
        except ValueError:
            print("请输入一个有效的整数。")

    # Send a request to check if the room_id is valid
    response = requests.get(f'https://api.live.bilibili.com/room/v1/Room/room_init?id={room_id}')

    # If the room_id is not valid, keep asking the user to input a valid room_id
    MAX_TRIES = 5
    try_count = 0
    while response.json()['code'] != 0 and try_count < MAX_TRIES:
        try_count += 1
        print("该直播间id无效，请重新输入。")
        while True:
            try:
                room_id = int(input("请输入直播间id："))
                break
            except ValueError:
                print("请输入一个有效的整数。")
        response = requests.get(f'https://api.live.bilibili.com/room/v1/Room/room_init?id={room_id}')

    if try_count >= MAX_TRIES:
        # 如果达到最大尝试次数，打印错误信息并退出程序
        print("已达到最大尝试次数，请稍后重试。")
        exit()

    # If the room_id is valid, print a message to inform the user
    print("直播间id有效，可以获取弹幕。")

    # 请求参数
    params = {
        'roomid': room_id,
        'csrf_token': '',
        'csrf': ''
    }

    # Define the existing_danmus list
    existing_danmus = []


    # Format the filename as "年+月+日+小时+直播间id.txt"
    BarrageRecording =time.strftime('%Y%m%d%H', time.localtime()) + "-" + str(room_id) + '.txt'

    # Check if the file 'danmu.txt' exists
    if os.path.exists(BarrageRecording):
        # If the file exists, delete it
        os.remove(BarrageRecording)

    # Continuously loop to get the danmus in real-time
    while True:
        # Send the request to get the danmus
        response = requests.get(url, headers=headers, params=params)

        # Get the danmu content
        danmu_list = response.json()['data']['room']

        # 连接直播间时判断直播时候结束
        if not danmu_list:
            # Print a message to inform the user that the live stream has ended
            print("直播已结束，程序即将退出。")
            # Exit the program
            exit()

        # Iterate through each danmu in the danmu_list
        for danmu in danmu_list:
            # Extract the time, user, and text content from the danmu
            time_str = danmu['timeline']
            user = danmu['nickname']
            text = danmu['text']

            # Check if the danmu's time is already in the existing_danmus list
            if time_str not in existing_danmus:
                # If the danmu's time is not already in the existing_danmus list,
                # format the danmu as "时间+用户+弹幕内容"
                formatted_danmu = f"<--{time_str} - {user}--> + {text}"

                # Print the formatted danmu
                print(formatted_danmu)

                # Call the voice_player function to play the danmu content
                VoiceBroadcast.voice_player(formatted_danmu)

                # Open the 'danmu.txt' file in append mode and add the new danmu to the end
                with open('Temp/' + BarrageRecording, 'a', encoding='utf-8') as f:
                    f.write("<--" + time_str + '-' + user + "-->  " + text + '\n')

                # Add the danmu's time to the existing_danmus list
                existing_danmus.append(time_str)

        # Wait for 1 second before sending the next request
        time.sleep(1)