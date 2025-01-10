from config import public_holidays


if __name__ == "__main__":
    current_week = public_holidays.is_weekday()
    # print(f"{current_week}")
    if current_week == 1:
        print(f"It's not the holidays and is the Friday!")
    else:
        print(f"It's not the holidays and is the Friday!")
