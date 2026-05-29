import math

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def bang_cuu_chuong(a, b):
    bat_dau = min(a, b)
    ket_thuc = max(a, b)
    for i in range(bat_dau, ket_thuc + 1):
        print(f"--- Bảng cửu chương {i} ---")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print()

def liet_ke_snt_nho_hon_n(n):
    ds_snt = [str(i) for i in range(2, n) if la_so_nguyen_to(i)]
    print(f"Các số nguyên tố < {n}: {', '.join(ds_snt)}")

def liet_ke_uoc_snt(n):
    uoc_snt = [str(i) for i in range(2, n + 1) if n % i == 0 and la_so_nguyen_to(i)]
    print(f"Các số vừa là ước của {n}, vừa là số nguyên tố: {', '.join(uoc_snt)}")

def main():
    try:
        nhap_ab = input("Nhập a, b: ")
        a, b = map(int, nhap_ab.split(','))
        bang_cuu_chuong(a, b)
        n = int(input("Nhập số nguyên dương n: "))
        liet_ke_snt_nho_hon_n(n)
        liet_ke_uoc_snt(n)
        
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số!")

if __name__ == "__main__":
    main()