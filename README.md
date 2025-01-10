# holidays
> 声明：本项目仅用于学习和研究PYTHON，中国法定假期。
from datetime import date, datetime


holidays = [
    "2025-01-01",  # 元旦
    "2025-01-28",  # 春节
    "2025-01-29",  # 春节
    "2025-01-30",  # 春节
    "2025-01-31",  # 春节
    "2025-02-01",  # 春节
    "2025-02-02",  # 春节
    "2025-02-03",  # 春节
    "2025-02-04",  # 春节
    "2025-04-04",  # 清明节
    "2025-04-05",  # 清明节
    "2025-04-06",  # 清明节
    "2025-05-01",  # 五一
    "2025-05-02",  # 五一
    "2025-05-03",  # 五一
    "2025-05-04",  # 五一
    "2025-05-05",  # 五一
    "2025-05-31",  # 端午
    "2025-06-01",  # 端午
    "2025-06-02",  # 端午
    "2025-10-01",  # 国庆
    "2025-10-02",  # 国庆
    "2025-10-03",  # 国庆
    "2025-10-04",  # 国庆
    "2025-10-05",  # 国庆
    "2025-10-06",  # 国庆
    "2025-10-07",  # 国庆
    "2025-10-08",  # 国庆
]


def is_weekday():
    # 获取当前日期
    today = datetime.today().date()
    # 检查是否是周末
    if today.weekday() == 4:
        if today.strftime("%Y-%m-%d") not in holidays:
            return 1
    return 2


if __name__ == "__main__":
    current_week = is_weekday()
    if current_week == 1:
        print(f"ok!")
    else:
        print(f"not ok!")

from config import public_holidays


if __name__ == "__main__":
    current_week = public_holidays.is_weekday()
    # print(f"{current_week}")
    if current_week == 1:
        print(f"It's not the holidays and is the Friday!")
    else:
        print(f"It's not the holidays and is the Friday!")

