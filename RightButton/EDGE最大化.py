import win32gui
import win32con
import win32process
import psutil


def get_edge_windows():
    edge_windows = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                process = psutil.Process(pid)
                if process.name().lower() == "msedge.exe":
                    if not win32gui.IsIconic(hwnd):  # 排除最小化的窗口
                        edge_windows.append(hwnd)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return True

    win32gui.EnumWindows(enum_handler, None)
    return edge_windows


edge_hwnds = get_edge_windows()

if not edge_hwnds:
    print("未找到Microsoft Edge窗口。")
else:
    for hwnd in edge_hwnds:
        placement = win32gui.GetWindowPlacement(hwnd)
        if placement[1] != win32con.SW_MAXIMIZE:
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
            print("已将Microsoft Edge窗口最大化。")
        else:
            print("Microsoft Edge窗口已处于最大化状态。")
