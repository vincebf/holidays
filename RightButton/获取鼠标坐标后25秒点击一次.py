import pyautogui
import time
import keyboard
import sys, datetime
from datetime import datetime

# 设置安全措施：将鼠标移动到屏幕左上角(0,0)时触发失败安全，终止程序
pyautogui.FAILSAFE = True


def auto_click(interval_seconds, x=None, y=None, click_times=1):
    """定时点击函数    :param interval_seconds: 点击间隔时间（秒）    :param x: 目标X坐标（None表示当前位置）    :param y: 目标Y坐标（None表示当前位置）    :param click_times: 点击次数（默认1次）"""
    try:
        print("程序已启动，按 ESC 键终止...")
        while True:
            now = datetime.now()
            formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
            # 检测是否按下 ESC 键
            if keyboard.is_pressed("esc"):
                print("\n程序已手动终止")
                break

            # 获取目标坐标（如果未指定则使用当前位置）
            target_x, target_y = (
                pyautogui.position() if (x is None or y is None) else (x, y)
            )

            print(f"当前坐标: ({formatted_now},{target_x}, {target_y})")
            # 执行点击操作
            pyautogui.click(x=target_x, y=target_y, clicks=click_times)
            # print(
            #     f"已在坐标 ({target_x}, {target_y}) 点击 {click_times} 次 - {time.strftime('%Y-%m-%d %H:%M:%S')}"
            # )

            # 等待指定间隔
            time.sleep(interval_seconds)

    except Exception as e:
        print(f"发生错误: {str(e)}")
    finally:
        print("程序结束")


if __name__ == "__main__":
    # 自定义参数（示例：每5秒点击一次坐标(100, 200)）
    CLICK_INTERVAL = 25  # 点击间隔（秒）
    TARGET_X = None  # 目标X坐标（None表示当前鼠标位置）
    TARGET_Y = None  # 目标Y坐标（None表示当前鼠标位置）
    CLICK_TIMES = 1  # 每次点击次数

    # 获取当前坐标的提示
    if TARGET_X is None or TARGET_Y is None:
        input("请将鼠标移动到目标位置，按回车获取坐标...")
        current_x, current_y = pyautogui.position()
        print(f"当前坐标: ({current_x}, {current_y})")
        # confirm = input("是否使用当前坐标？(y/n): ").lower()
        # if confirm == "y":
        TARGET_X, TARGET_Y = current_x, current_y
        # else:
        #     exit()

    auto_click(
        interval_seconds=CLICK_INTERVAL, x=TARGET_X, y=TARGET_Y, click_times=CLICK_TIMES
    )
