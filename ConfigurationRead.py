
import yaml

import os

def parse_config_file(filename):
    if not os.path.isfile(filename):
        return filename + " is not file"
    try:
        with open(filename, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        return config
    except:
        return filename + "内容存在错误，解析异常，请修正文件内容！"

