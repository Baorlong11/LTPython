import math

# a) Số thân thiện: gcd(n, số đảo ngược của n) = 1
so_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# b) Số chính phương
so_chinh_phuong = lambda n: int(math.sqrt(n)) ** 2 == n

# c) Số đồng nhất: các chữ số đều giống nhau
so_dong_nhat_all = lambda n: all(ch == str(n)[0] for ch in str(n))
so_dong_nhat_any = lambda n: not any(ch != str(n)[0] for ch in str(n))

# d) Số hoàn thiện: tổng ước không kể chính nó bằng n
so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

# e) Số phong phú: tổng ước không kể chính nó lớn hơn n
so_phong_phu = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) > n

# f) Số tăng dần: chữ số từ trái sang phải không giảm
so_tang_dan = lambda n: all(str(n)[i] <= str(n)[i + 1] for i in range(len(str(n)) - 1))

# g) Số Armstrong
so_armstrong = lambda n: sum(int(ch) ** len(str(n)) for ch in str(n)) == n

# h) Số nguyên tố
so_nguyen_to = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))

# i) Số Palindrome
so_palindrome = lambda n: str(n) == str(n)[::-1]

# j) Số nguyên tố Palindrome
so_nguyen_to_palindrome = lambda n: so_nguyen_to(n) and so_palindrome(n)

# k) Số lộc phát: chỉ chứa số 6 hoặc 8
so_loc_phat_all = lambda n: all(ch in "68" for ch in str(n))
so_loc_phat_dem = lambda n: str(n).count("6") + str(n).count("8") == len(str(n))

# l) Số lộc phát Palindrome
so_loc_phat_palindrome = lambda n: so_loc_phat_all(n) and so_palindrome(n)


# ==========================
# IN KẾT QUẢ TỪ 1 ĐẾN 1 TRIỆU
# ==========================

print("Nhập một số nguyên dương N (1 <= N <= 1,000,000): ")
N = int(input())

print("a) Số thân thiện:")
print([i for i in range(1, N + 1) if so_than_thien(i)])

print("\nb) Số chính phương:")
print([i for i in range(1, N + 1) if so_chinh_phuong(i)])

print("\nc) Số đồng nhất:")
print([i for i in range(1, N + 1) if so_dong_nhat_all(i)])

print("\nd) Số hoàn thiện:")
print([i for i in range(1, N + 1) if so_hoan_thien(i)])

print("\ne) Số phong phú:")
print([i for i in range(1, N + 1) if so_phong_phu(i)])

print("\nf) Số tăng dần:")
print([i for i in range(1, N + 1) if so_tang_dan(i)])

print("\ng) Số Armstrong:")
print([i for i in range(1, N + 1) if so_armstrong(i)])

print("\nh) Số nguyên tố:")
print([i for i in range(1, N + 1) if so_nguyen_to(i)])

print("\ni) Số Palindrome:")
print([i for i in range(1, N + 1) if so_palindrome(i)])

print("\nj) Số nguyên tố Palindrome:")
print([i for i in range(1, N + 1) if so_nguyen_to_palindrome(i)])

print("\nk) Số lộc phát:")
print([i for i in range(1, N + 1) if so_loc_phat_all(i)])

print("\nl) Số lộc phát Palindrome:")
print([i for i in range(1, N + 1) if so_loc_phat_palindrome(i)])