from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import win32gui, win32process, psutil, pyautogui, subprocess, time, sys

chrome_driver_path = "D:\deepseek\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
url = "http://172.24.215.211:3000/d/ady80rsrqrz0gf/zabbix-servers-status?orgId=1&refresh=1m&kiosk"
subprocess.Popen([chrome_path, url])
time.sleep(5)
driver.fullscreen_window()


def open_chrome_fullscreen():
    while True:
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(15)
        pyautogui.press("f5")


if __name__ == "__main__":
    open_chrome_fullscreen()
