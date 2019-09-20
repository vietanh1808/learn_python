import os

ds_hang_tonkho = []

def ghi_kho():
    file_w = open("../danhmuc/phieunhapkho.csv", "w")
    for hanghoa in ds_hang_tonkho:
        str_save = hanghoa['id'] + '#' + str(hanghoa['soluong']) + '\n'
        file_w.write(str_save)
def load_tonkho():
    with open("../danhmuc/phieunhapkho.csv", "r") as f:
        line = f.readline()
        while line:
            hang_tonkho = {}
            str_read = line.split("#")
            hang_tonkho['id'] = str_read[0]
            if str_read[1].endswith('\n'):
                hang_tonkho['soluong'] = str_read[1][:len(str_read[1])-1]
            else:
                hang_tonkho['soluong'] = str_read[1]
            ds_hang_tonkho.append(hang_tonkho)
            line = f.readline()
load_tonkho()
def nhapkho():
    while True:
        nhap = input("Moi ban nhap id hang hoa: ")
        for hanghoa in ds_hang_tonkho:
            if nhap in hanghoa['id']:
                soluong = int(input("Moi ban nhap so luong can nhap: "))
                hanghoa['soluong'] = int(hanghoa['soluong'])
                hanghoa['soluong'] += soluong
                ghi_kho()
                return 
def kiemtra_kho(id, soluong): # khi tao hoa don hang hoa
    for hanghoa in ds_hang_tonkho:
        if id == hanghoa['id']:
            hanghoa['soluong'] = int(hanghoa['soluong'])
            if hanghoa['soluong'] < soluong:
                print("[!] Khong du luu tru hang hoa trong kho")
                return 1
            else:
                hanghoa['soluong'] -= soluong
                ghi_kho()
                return
def xuat_tonkho():
    while True:
        nhap = input("Moi ban nhap id hang hoa can xem: ")
        for hanghoa in ds_hang_tonkho:
            if nhap == hanghoa['id']:
                print("[+] Ton kho {}: {}".format(hanghoa['id'], hanghoa['soluong']))
                return

# xuat_tonkho()
# print(ds_hang_tonkho)