import quanlyhoadon,quanlykhachang,quanlyuser
import os
import json

print("+--------------MENU_USER-------------------------------+")
print("|Chon TAOUSER de tao user                              |")
print("|Chon XOAUSER de xoa user                              |")
print("|Chon XEMUSER de xem danh sach user                    |")
print("|Chon LOGIN de login                                   |")
print("|                                                      |")
print("+--------------MENU_HOA_DON----------------------------+")
print("|Chon C de tao hoa don                                 |")
print("|Chon R de xem thong tin hoa don                       |")
print("|Chon T de tinh tong doanh thu                         |")
print("|Chon A de tinh tong hang hoa ban ra                   |")
print("|Chon C de tao hoa don                                 |")
print("|                                                      |")
print("+--------------MENU_HANG_HOA---------------------------+")
print("|Chon HH de xem hang theo thang                        |")
print("|Chon LHH de xem loai hang hoa chay nhat               |")
print("|Chon THH de tao hang hoa                              |")
print("|Chon XHH de xem hang hoa                              |")
print("|Chon TLH de tao loai hang hoa                         |")
print("|Chon XLH de xem loai hang hoa                         |")
print("+------------------------------------------------------+")
print("|                                                      |")
print("+--------------MENU_KHACH_HANG-------------------------+")
print("|Chon XDSKH de xem danh sach khach hang                |")
print("|Chon XTTKH de xem thong tin khach hang                |")
print("|Chon XKHTM de xem khach hang than mat                 |")
print("+------------------------------------------------------+")
print("|                                                      |")
print("|Chon E de thoat                                       |")
print("+------------------------------------------------------+")

while True:
    x = input("=> chon chuc nang:")
    print("=> ban da chon chuc nang:",x)
    if x.upper() == 'HH':
      quanlyhoadon.hanghoatheothang()
    if x.upper() == 'LHH':
      quanlyhoadon.loaihh_chaynhat()
    if x.upper() == 'TLH':
      quanlyhoadon.tao_loaihanghoa()
    if x.upper() == 'XLH':
      quanlyhoadon.xem_loaihanghoa()
    if x.upper() == 'THH':
      quanlyhoadon.tao_hanghoa()
    if x.upper() == 'XHH':
      quanlyhoadon.xem_hanghoa()
    if x.upper() == 'C':
      quanlyhoadon.tao_hoadon()
    if x.upper() == 'R':
      quanlyhoadon.xem_hoadon()
    if x.upper() == 'T':
      quanlyhoadon.xem_tongdoanhthu()
    if x.upper() == 'A':
      quanlyhoadon.tonghanghoaban()
    if x.upper() == 'TAOUSER':
      quanlyuser.tao_user()
    if x.upper() == 'XOAUSER':
      quanlyuser.xoa_user()
    if x.upper() == 'XEMUSER':
      quanlyuser.xem_user()
    if x.upper() == 'LOGIN':
      quanlyuser.login()
    if x.upper() == 'XDSKH':
      quanlykhachang.xem_dskhachhang()
    if x.upper() == 'XTTKH':
      quanlykhachang.xem_thongtin_KH()
    if x.upper() == 'XKHTM':
      quanlykhachang.khachhang_thanmat()
    if x.upper() == 'E':
        print("Tam biet! Hen gap lai")
        break
        

