from lunarcalendar import Converter, Solar, Lunar
from datetime import date

# 获取当前年份
current_year = date.today().year

# 计算春节日期（农历正月初一）
lunar_new_year = Lunar(current_year, 1, 1)
solar_new_year = Converter.Lunar2Solar(lunar_new_year)

# 打印春节日期
print(f"春节日期: {solar_new_year}")

# 计算距离春节的天数
days_until_spring_festival = (solar_new_year.to_date() - date.today()).days
print(f"距离春节还有 {days_until_spring_festival} 天")
