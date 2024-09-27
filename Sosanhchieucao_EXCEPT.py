ban1_name, ban1_height = input("Nhap ten va chieu cao ban 1: ").split()
ban2_name, ban2_height = input("Nhap ten va chieu cao ban 2: ").split()
try:

    ban1_height = int(ban1_height)
    ban2_height = int(ban2_height)

    if ban1_height <= 0 or ban2_height <= 0:
        print("Chieu cao phai lon hon 0, vui long nhap lai")
    elif ban1_height > ban2_height:
        print(ban1_name, "cao hon ban", ban2_name)
    elif ban1_height < ban2_height:
        print(ban1_name, "thap hon ban", ban2_name)
    else:
        print(ban1_name, "cao ngang ban", ban2_name)

except:
    print("Dinh dang dau vao kh hop le")