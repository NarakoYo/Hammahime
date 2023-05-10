
# 系统
import time
import os
import sys
import locale

# 用户
import ConfigurationSetup
import unit


# Create an initialization function
def init():

    # locale.setlocale(locale.LC_ALL, 'zn_ch.UTF-8')
    # Add initialization code here

    ConfigurationSetup()

    pass

# 入口
# Define the main function
def main():

    # 初始化
    init()




# Only call the main function if this file is being run directly (not imported as a module)
if __name__ == '__main__':
    main()