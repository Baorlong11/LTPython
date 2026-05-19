import math

def get_reverse(n):
    return int(str(n)[::-1])

a = int(input())
b = int(input())

friendly_list = []
for i in range(a, b + 1):
    if math.gcd(i, get_reverse(i)) == 1:
        friendly_list.append(i)

print(*(friendly_list))
print(len(friendly_list))