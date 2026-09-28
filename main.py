diem1 = float(input("Điểm môn 1: "))
diem2 = float(input("Điểm môn 2: "))
diem3 = float(input("Điểm môn 3: "))

# TODO: Tính điểm trung bình
diem_tb = (diem1+diem2+diem3)/3

# TODO: Xếp loại theo bảng trên
if diem_tb>=9:
    xep_loai = "Xuất sắc"
elif diem_tb>=8:
    xep_loai = "Giỏi"
elif diem_tb>=7:
    xep_loai = "Khá"
elif diem_tb>=5:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print()
print(f"Điểm trung bình: {diem_tb:.2f}")
print(f"Xếp loại       : {xep_loai}")