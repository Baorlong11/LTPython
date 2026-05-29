kiem_tra_boi_so = lambda n: n % 13 == 0 or n % 19 == 0
kiem_tra_tam_giac = lambda a, b, c: (
    "Tam giác đều" if a == b == c else
    "Tam giác vuông cân" if (a == b or b == c or a == c) and (round(a**2+b**2, 2) == round(c**2, 2) or round(a**2+c**2, 2) == round(b**2, 2) or round(b**2+c**2, 2) == round(a**2, 2)) else
    "Tam giác vuông" if round(a**2+b**2, 2) == round(c**2, 2) or round(a**2+c**2, 2) == round(b**2, 2) or round(b**2+c**2, 2) == round(a**2, 2) else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác thường"
)

n = int(input("Nhập số nguyên n: "))
if kiem_tra_boi_so(n):
    print(f"{n} là bội số của 13 hoặc 19.")
else:
    print(f"{n} không phải bội số của 13 hay 19.")
print("-" * 30)

print("Nhập 3 cạnh tam giác:")
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if (a + b > c) and (a + c > b) and (b + c > a):
        loai = kiem_tra_tam_giac(a, b, c)
        print(f"3 cạnh hợp lệ. Đây là: {loai}")
    else:
        print("Kết quả: Không phải 3 cạnh tam giác (không thỏa mãn bất đẳng thức tam giác).")
except ValueError:
    print("Vui lòng chỉ nhập số!")
