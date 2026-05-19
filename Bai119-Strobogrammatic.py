def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def get_strobogrammatic(n, expanded=False):
    mapping = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
    if expanded:
        mapping.update({'2':'5', '5':'2'})
    
    s = str(n)
    res = ""
    for char in reversed(s):
        if char not in mapping:
            return None
        res += mapping[char]
    return int(res)

strob_list = []
strob_prime_list = []
strob_ext_list = []
strob_ext_prime_list = []
special_list = []

for i in range(1000000):
    val = get_strobogrammatic(i, expanded=False)
    is_strob = (val == i)
    if is_strob:
        strob_list.append(i)
        if is_prime(i):
            strob_prime_list.append(i)
            
    val_ext = get_strobogrammatic(i, expanded=True)
    is_strob_ext = (val_ext == i)
    if is_strob_ext:
        strob_ext_list.append(i)
        if is_prime(i):
            strob_ext_prime_list.append(i)

    if not is_strob and not is_prime(i):
        if val is not None and is_prime(val):
            special_list.append(i)

# In kết quả
print("a. Các số strobogrammatic nhỏ hơn 1 triệu:")
print(strob_list)

print("\nb. Các số nguyên tố strobogrammatic nhỏ hơn 1 triệu:")
print(strob_prime_list)

print("\nc. Các số strobogrammatic mở rộng nhỏ hơn 1 triệu:")
print(strob_ext_list)

print("\nd. Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu:")
print(strob_ext_prime_list)

print("\ne. Các số không phải strob, không phải nguyên tố, nhưng xoay lại là số nguyên tố:")
print(special_list)