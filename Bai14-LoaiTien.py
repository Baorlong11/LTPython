def giai_bai_toan_doi_tien():
    try:
        x_input = int(input("Nhap so tien X: "))
    except ValueError:
        print("Vui long nhap mot so nguyen.")
        return
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    print(f"So tien {x_input} duoc doi thanh:")
    tong_so_to = 0
    con_lai = x_input
    for mg in menh_gia:
        so_to = con_lai // mg
        con_lai = con_lai % mg
        tong_so_to += so_to
        print(f"Loai {mg} gom {so_to} to")
    print(f"TONG CONG CO {tong_so_to} TO")
giai_bai_toan_doi_tien()