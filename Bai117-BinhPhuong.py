n_str = input()
length = len(n_str)
total_s = 0

for i in range(length):
    for j in range(i + 1, length + 1):
        sub_val = int(n_str[i:j])
        total_s += sub_val**2

print(total_s)