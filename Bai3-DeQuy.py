def tinh_luy_thua(a, b):
    if b == 0:
        return 1
    return a * tinh_luy_thua(a, b - 1)

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
if a > 0 and b >= 0:
    ket_qua = tinh_luy_thua(a, b)
    print(f"{a}^{b} = {ket_qua}")

    