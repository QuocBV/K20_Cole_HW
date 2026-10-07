import csv
from io import StringIO
from datetime import datetime
import re

NHAN_VIEN_CSV = """id,name,department,salary,start_date,email
1,Nguyen Van An,Engineering,25000000,2021-03-15,an.nguyen@company.com
2,Tran Thi Bich,Data,30000000,2020-07-01,bich.tran@company.com
3,Le Van Cuong,Engineering,BAD_VALUE,2022-01-10,cuong.le@company.com
4,Pham Thi Dung,Marketing,18000000,2023-13-45,dung.pham@company.com
5,Hoang Van Em,Data,35000000,2019-11-20,em.hoang@company.com
6,,Engineering,22000000,2022-05-30,f@company.com
7,Nguyen Thi Giang,HR,20000000,2021-08-15,giang.nguyen@company.com
8,Do Van Hung,Data,28000000,2020-03-10,hung.do@company.com
9,Vu Thi Lan,Marketing,17000000,2023-06-01,lan.vu@BAD-EMAIL
10,Bui Van Minh,Engineering,32000000,2018-12-25,minh.bui@company.com
11,Ly Thi Mai,HR,19500000,2021-04-22,mai.ly@company.com
12,Dang Van Nam,Engineering,27000000,2022-09-14,nam.dang@company.com
13,Trinh Thi Oanh,Data,31000000,2020-11-05,oanh.trinh@company.com
14,Ngo Van Phuc,Marketing,16500000,2023-02-28,phuc.ngo@company.com
15,Vo Thi Quynh,Engineering,24000000,2021-12-10,quynh.vo@company.com
16,Phan Van Son,Data,33000000,2019-05-20,son.phan@company.com
17,Ta Thi Tam,HR,21000000,2022-07-01,tam.ta@company.com
18,Nguyen Van Uy,Engineering,NULL,2023-01-15,uy.nguyen@company.com
19,Le Thi Van,Marketing,19000000,2024-05-40,van.le@company.com
20,Bui Van Xuan,Data,29500000,2020-08-30,xuan.bui@company.com
21,,Engineering,26000000,2021-11-11,y.dang@company.com
22,Hoang Thi Yen,HR,20500000,2022-03-25,yen.hoang@company.com
23,Dinh Van An,Data,34000000,2018-09-10,an.dinh@company.com
24,Quach Thi Binh,Marketing,17500000,2023-10-12,binh.quach@BAD-EMAIL
25,Luong Van Chien,Engineering,28500000,2021-06-05,chien.luong@company.com
26,Diep Thi Dao,Data,31500000,2020-02-20,dao.diep@company.com
27,Ngo Van Dong,Engineering,BAD_VALUE,2022-04-18,dong.ngo@company.com
28,Chu Thi Ha,HR,22000000,2019-12-12,ha.chu@company.com
29,Ly Van Khanh,Marketing,18500000,2023-08-08,khanh.ly@company.com
30,Mai Thi Lien,Data,360000000,2000-00-00,lien.mai@company.com
"""


def ReadCsvFromString(str_data):
    dt = StringIO(str_data)
    return csv.DictReader(dt)


def chiPhiLuongPhongBan(csvData):

    dicChiPhiPb = {}
    for row in csvData:
        phong_ban = row["department"]
        salStr = row["salary"]
        try:
            luong = int(salStr)
        except ValueError:
            continue
        dicChiPhiPb[phong_ban] += luong
    print(f"chiPhiLuongPhongBan: {dicChiPhiPb}")
    return dicChiPhiPb


def GetValidData():
    csvData = ReadCsvFromString(NHAN_VIEN_CSV)
    patternEmail = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    ngayHIentai = datetime.now()
    thongTinHopLe = []
    thongTinLoi = []

    for row in csvData:
        idNv = row["id"]
        name = row["name"]
        department = row["department"]
        salary = row["salary"]
        start_date = row["start_date"]
        email = row["email"]
        errors = []
        # valid date time
        try:
            start_date_valid = datetime.strptime(start_date, "%Y-%m-%d")

        except ValueError:
            errors.append(f"Ngày vào làm không hợp lệ ({start_date})")
        # valid salary
        try:
            salary_valid = int(salary)

        except ValueError:
            errors.append(f"Lương không hợp lệ ({salary})")
        # Email valid
        if not re.match(patternEmail, row["email"]):
            errors.append(f"Email không hợp lệ ({email})")

        if errors:
            thongTinLoi.append(
                {
                    "id": row["id"],
                    "name": row["name"],
                    "errors": errors,
                }
            )
        else:
            kinh_nghiem = round((ngayHIentai - start_date_valid).days / 365, 1)
            thongTinHopLe.append(
                {
                    "id": idNv,
                    "name": name,
                    "department": department,
                    "salary": salary_valid,
                    "kinh_nghiem": kinh_nghiem,
                    "email": email,
                }
            )
    return thongTinHopLe, thongTinLoi


dataValid, erros = GetValidData()
if dataValid:
    ky_cuu = max(dataValid, key=lambda x: x["kinh_nghiem"])
    moi_nhat = min(dataValid, key=lambda x: x["kinh_nghiem"])
