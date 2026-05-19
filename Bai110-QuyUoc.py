def khoi_phuc_chuoi(cipher_text):
    plain_text = ""
    i = 0
    n = len(cipher_text)
    
    while i < n:
        if cipher_text[i] == '#':
            so_luong = int(cipher_text[i+1])
            ky_tu = cipher_text[i+2]
            plain_text += ky_tu * so_luong
            i += 3
        else:
            plain_text += cipher_text[i]
            i += 1
            
    return plain_text

test1 = "XY#6Z1#4023"
print(khoi_phuc_chuoi(test1)) 

test2 = "#39+1=1#30"
print(khoi_phuc_chuoi(test2))