import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "D:\deepseek\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

url = "http://172.24.215.211:3000/d/ady80rsrqrz0gf/zabbix-servers-status?orgId=1&refresh=1m&kiosk"
driver.get(url)
time.sleep(5)


# 检查当前窗口是否处于全屏模式
def is_fullscreen(driver):
    # 获取当前窗口的尺寸和屏幕的尺寸
    window_size = driver.get_window_size()
    screen_width = driver.execute_script("return window.screen.width;")
    screen_height = driver.execute_script("return window.screen.height;")

    # 判断窗口尺寸是否等于屏幕尺寸
    return (
        window_size["width"] == screen_width and window_size["height"] == screen_height
    )


def is_edge_fullscreen(driver):
    while True:
        # 如果未处于全屏模式，则设置为全屏模式
        if not is_fullscreen(driver):
            print("当前未处于全屏模式，正在设置为全屏模式...")
            driver.fullscreen_window()  # 进入全屏模式
        else:
            print("当前已处于全屏模式。")
        time.sleep(15)


# def is_edge_fullscreen():
#     while True:
#         driver.maximize_window()  # 最大化窗口（非全屏）
#         driver.fullscreen_window()  # 进入全屏模式
#         time.sleep(52600)


if __name__ == "__main__":
    is_edge_fullscreen(driver)
