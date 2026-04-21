from datetime import date

d1_input = input("Nhập ngày 1 (ngày/tháng/năm): ")
d2_input = input("Nhập ngày 2 (ngày/tháng/năm): ")

ngay1, thang1, nam1 = map(int, d1_input.split('/'))
ngay2, thang2, nam2 = map(int, d2_input.split('/'))

d1 = date(nam1, thang1, ngay1)
d2 = date(nam2, thang2, ngay2)

delta = abs((d2 - d1).days)

print(f"Số ngày cách nhau giữa 2 ngày là: {delta} ngày")