from datetime import datetime

S = input("Nhập chuỗi ngày (ví dụ Sep 18 2019 2:43PM): ")

d = datetime.strptime(S, "%b %d %Y %I:%M%p")

print(f"Dữ liệu sau khi chuyển: {type(d)}")
print(f"Giá trị ngày tháng: {d}")