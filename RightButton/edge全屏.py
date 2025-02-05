import win32gui
import win32api
import win32process
import win32con
import psutil
import time
import pyautogui
from datetime import datetime


now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")


def is_edge_fullscreen():
    """检测是否存在全屏的 Edge 窗口"""
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    edge_hwnds = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                process = psutil.Process(pid)
                if process.name().lower() == "msedge.exe":
                    rect = win32gui.GetWindowRect(hwnd)
                    # 判断窗口是否覆盖整个主屏幕
                    if (
                        rect[0] <= 0
                        and rect[1] <= 0
                        and rect[2] >= screen_width
                        and rect[3] >= screen_height
                    ):
                        edge_hwnds.append(hwnd)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return True

    win32gui.EnumWindows(callback, None)
    return len(edge_hwnds) > 0


def activate_and_fullscreen_edge():
    """激活 Edge 窗口并发送 F11 按键"""
    edge_hwnds = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                process = psutil.Process(pid)
                if process.name().lower() == "msedge.exe":
                    edge_hwnds.append(hwnd)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return True

    win32gui.EnumWindows(enum_handler, None)

    if not edge_hwnds:
        print("未找到 Microsoft Edge 窗口")
        return False

    # 尝试激活第一个找到的窗口
    target_hwnd = edge_hwnds[0]

    while True:
        pyautogui.press("f5")
        if is_edge_fullscreen():
            print("Edge 已处于全屏模式")
        else:
            # print("Edge 未处于全屏模式，尝试全屏...")
            # 恢复窗口（如果最小化）
            if win32gui.IsIconic(target_hwnd):
                win32gui.ShowWindow(target_hwnd, win32con.SW_RESTORE)
            # 将窗口置顶
            win32gui.SetForegroundWindow(target_hwnd)
            time.sleep(0.5)  # 等待窗口激活
            # 发送 F11 按键
            pyautogui.press("f11")
            # print("已发送 F11 按键至 Edge 窗口")
        time.sleep(5)


if __name__ == "__main__":
    activate_and_fullscreen_edge()
    # if not is_edge_fullscreen():
    #     print("Edge 未处于全屏模式，尝试全屏...")
    #     if activate_and_fullscreen_edge():
    #         print("操作成功！等待 2 秒后重新检测...")
    #         time.sleep(2)
    #         print("当前全屏状态:", "是" if is_edge_fullscreen() else "否")
    #     else:
    #         print("未能成功全屏 Edge")
    # else:
    #     print("Edge 已处于全屏模式")
