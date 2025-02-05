import time
import keyboard
from pywinauto import Desktop, findwindows


def auto_confirm_popup(target_title="系统提示", timeout=20000, check_interval=0.5):
    """
    监控并自动确认指定标题的弹窗
    :param target_title: 弹窗标题（支持模糊匹配，如“确认”或“另存为”）
    :param timeout: 超时时间（秒）
    :param check_interval: 检查间隔（秒）
    """
    print(f"开始监控弹窗（标题包含'{target_title}'），按 ESC 键终止...")
    start_time = time.time()

    while time.time() - start_time < timeout:
        # 检测 ESC 键终止
        if keyboard.is_pressed("esc"):
            print("监控已手动终止")
            return

        try:
            # 查找所有顶层窗口
            windows = Desktop(backend="uia").windows()
            for win in windows:
                if target_title.lower() in win.window_text().lower():
                    print(f"发现弹窗: {win.window_text()}")
                    # 激活窗口并发送回车键
                    win.set_focus()
                    keyboard.send("enter")
                    print("已发送回车确认")
                    return
        except findwindows.ElementNotFoundError:
            pass

        time.sleep(check_interval)

    print("超时，未检测到目标弹窗")


if __name__ == "__main__":
    # 示例：监控标题包含“确认”的弹窗，超时60秒
    auto_confirm_popup(target_title="系统提示")
