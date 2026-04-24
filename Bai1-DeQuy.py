def tinh_tong_chu_so(n):
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + tinh_tong_chu_so(n // 10)

n = int(input("Nhap so nguyen n: "))
print("Tong chu so cua", n, "la:", tinh_tong_chu_so(n))