import time
import keyboard
from pywinauto import Desktop, findwindows
from pywinauto.controls.uia_controls import ButtonWrapper
from pywinauto import Application


def auto_confirm_edge_popup():
    target_texts = ["保存", "确认", "允许", "是", "系统提示", "确定"]
    timeout = 6000
    check_interval = 25
    print(f"监控 Edge 弹窗中（关键词：{target_texts}），按 ESC 终止...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        if keyboard.is_pressed("esc"):
            print("监控已手动终止")
            return
        try:
            windows = Desktop(backend="uia").windows()
            print("已发送回车确认0")
            for win in windows:
                if (
                    "Chrome_WidgetWin" not in win.class_name()
                    and "Microsoft Edge" not in win.window_text()
                ):
                    print("已发送回车确认1")
                    continue
                win_text = win.window_text().lower()
                has_target = any(txt.lower() in win_text for txt in target_texts)
                print("已发送回车确认2")
                if not has_target:
                    try:
                        confirm_btn = win.child_window(
                            control_type="Button",
                            title=lambda t: any(
                                keyword in t.lower() for keyword in target_texts
                            ),
                        )
                        if confirm_btn.exists():
                            has_target = True
                    except findwindows.ElementNotFoundError:
                        pass
                if has_target:
                    print(f"发现 Edge 弹窗: {win.window_text()}")
                    win.set_focus()
                    keyboard.send("enter")
                    print("已发送回车确认")
                    return
        except Exception as e:
            print(f"监控出错: {str(e)}")
        time.sleep(check_interval)
    print("超时，未检测到目标弹窗")


if __name__ == "__main__":
    auto_confirm_edge_popup()
