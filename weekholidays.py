from lunarcalendar import Converter, Solar, Lunar
from datetime import date, datetime
from config import holidays
import requests
import hashlib
import base64
import time
import json
import sys


# 获取当前年份
current_year = date.today().year

# 计算春节日期（农历正月初一）
lunar_new_year = Lunar(current_year, 1, 1)
solar_new_year = Converter.Lunar2Solar(lunar_new_year)
# 计算距离春节的天数
days_until_spring_festival = (solar_new_year.to_date() - date.today()).days
print(f"距离春节还有 {days_until_spring_festival} 天")

message1 = "大扫除"
message2 = "不是大扫除日"
filepath = "C:/Users/wuzheng3/Pictures/dsc.jpeg"
data = holidays.data1(message1)
data1 = holidays.data2(message2)
data2 = holidays.data_image(filepath)


if __name__ == "__main__":
    current_week = holidays.is_weekday()
    if current_week != 1:
        print(requests.post(url=holidays.url, headers=holidays.headers, data=data))
        if days_until_spring_festival <= 7:
            print(requests.post(url=holidays.url, headers=holidays.headers, data=data2))
    else:
        print(requests.post(url=holidays.SELF, headers=holidays.headers, data=data1))
        if days_until_spring_festival <= 7:
            print(
                requests.post(url=holidays.SELF, headers=holidays.headers, data=data2)
            )
