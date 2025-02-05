import pyautogui, time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
scheduler = BlockingScheduler()


def auto_refresh():
    # time.sleep(5)
    print(f"当前刷新: ({formatted_now})")
    pyautogui.press("f5")  # 发送 F5 刷新
    time.sleep(5)


if __name__ == "__main__":
    auto_refresh()
