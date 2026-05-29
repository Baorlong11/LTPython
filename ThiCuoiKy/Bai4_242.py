la_so_dong_nhat = lambda n: all(char == str(n)[0] for char in str(n))
la_so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

print("CÁC SỐ ĐỒNG NHẤT TỪ 1 ĐẾN 10000")
ds_dong_nhat = [i for i in range(1, 10001) if la_so_dong_nhat(i)]
print(ds_dong_nhat)

print("\n")

print("CÁC SỐ HOÀN THIỆN TỪ 1 ĐẾN 10000")
ds_hoan_thien = [i for i in range(1, 10001) if la_so_hoan_thien(i)]
print(ds_hoan_thien)

