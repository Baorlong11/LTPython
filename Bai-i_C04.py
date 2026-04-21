from datetime import datetime
now = datetime.now()

print("Năm hiện tại:", now.year)
print("Tháng hiện tại bằng chữ:", now.strftime("%B"))
print("Tuần hiện tại là tuần thứ mấy trong năm:", now.isocalendar()[1])

week_of_month = (now.day - 1) // 7 + 1
print("Tuần hiện tại là tuần thứ mấy trong tháng:", week_of_month)
print("Ngày hiện tại là ngày thứ mấy trong năm:", now.timetuple().tm_yday)
print("Ngày dương lịch hiện tại là ngày:", now.day)
print("Thứ của ngày hiện tại:", now.strftime("%A"))
print("Giờ phút giây hiện tại:", now.strftime("%H:%M:%S"))
