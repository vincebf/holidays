from datetime import date, datetime
from config import holidays
import requests
import hashlib
import base64
import time
import json
import sys


message1 = "大扫除"
message2 = "不是大扫除日"
filepath = "C:/Users/wuzheng3/Pictures/dsc.jpeg"
data = holidays.data1(message1)
data1 = holidays.data2(message2)
data2 = holidays.data_image(filepath)


if __name__ == "__main__":
    current_week = holidays.is_weekday()
    if current_week == 1:
        print(requests.post(url=holidays.url, headers=holidays.headers, data=data))
        print(requests.post(url=holidays.url, headers=holidays.headers, data=data2))
    else:
        print(requests.post(url=holidays.SELF, headers=holidays.headers, data=data1))
        print(requests.post(url=holidays.SELF, headers=holidays.headers, data=data2))
