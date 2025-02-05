from datetime import date, datetime
import requests  # conda install requests
import json
import sys
import time
from config import holidays
import base64
import hashlib

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=5210cec9-4bc5-470e-b541-1dd20b88280a"
SELF = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=990a7ff5-6428-4b75-9afe-b995c150ca81"
headers = {"content-type": "application/json"}

holidays = [
    "2025-01-01",  # 元旦
    "2025-01-28",  # 春节
    "2025-01-29",  # 春节
    "2025-01-30",  # 春节
    "2025-01-31",  # 春节
    "2025-02-01",  # 春节
    "2025-02-02",  # 春节
    "2025-02-03",  # 春节
    "2025-02-04",  # 春节
    "2025-04-04",  # 清明节
    "2025-04-05",  # 清明节
    "2025-04-06",  # 清明节
    "2025-05-01",  # 五一
    "2025-05-02",  # 五一
    "2025-05-03",  # 五一
    "2025-05-04",  # 五一
    "2025-05-05",  # 五一
    "2025-05-31",  # 端午
    "2025-06-01",  # 端午
    "2025-06-02",  # 端午
    "2025-10-01",  # 国庆
    "2025-10-02",  # 国庆
    "2025-10-03",  # 国庆
    "2025-10-04",  # 国庆
    "2025-10-05",  # 国庆
    "2025-10-06",  # 国庆
    "2025-10-07",  # 国庆
    "2025-10-08",  # 国庆
]


def data_image(filepath):
    with open(filepath, "rb") as f:
        img_data = f.read()
        base64_image = base64.b64encode(img_data).decode("utf-8")
        md5_res = hashlib.md5(img_data).hexdigest()

    message_data = {
        "msgtype": "image",
        "image": {"base64": base64_image, "md5": md5_res},
    }
    data2 = json.dumps(message_data)
    return data2


def data1(message):
    data = {
        "msgtype": "text",
        "text": {
            "content": message,
            "mentioned_list": ["@all"],
        },
    }
    data = json.dumps(data)
    return data


def data2(message1):
    data = {
        "msgtype": "text",
        "text": {
            "content": message1,
            "mentioned_list": ["@all"],
        },
    }
    data = json.dumps(data)
    return data


def is_weekday():
    # 获取当前日期
    today = datetime.today().date()
    # 检查是否是周末
    if today.weekday() == 4:
        if today.strftime("%Y-%m-%d") not in holidays:
            return 1
    return 2


if __name__ == "__main__":
    current_week = is_weekday()
    if current_week == 1:
        print(f"ok!")
    else:
        print(f"not ok!")
