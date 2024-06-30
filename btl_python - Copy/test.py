from fractions import Fraction
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

index = Tk()
index.title('Trang Chủ')
index.geometry('1000x600')
index.attributes("-topmost", True)

def thongke_khachhang():
    frame_container = Frame(index, bg="black", width=500, height=400)
    frame_container.place(x=150, y=0)

    input_thang = DateEntry(frame_container, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                            borderwidth=0, width=10, date_pattern="dd/mm/yyyy")
    input_thang.place(x=30, y=9)
    btn_thang_kh = Button(frame_container, text="Thống kê",
                          font=("Arial", 8, "bold"), fg="White", borderwidth=0,
                          bg="light blue", pady=2)
    btn_thang_kh.place(x=140, y=9)
    fram_bieudo = Frame(frame_container, bg='white')
    fram_bieudo.place(x=0, y=50)
def thongke_tau():
    frame_container = Frame(index, bg="white", width=500, height=400)
    frame_container.place(x=150, y=0)

    input_thang = DateEntry(frame_container, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                            borderwidth=0, width=10, date_pattern="dd/mm/yyyy")
    input_thang.place(x=30, y=9)
    btn_thang_kh = Button(frame_container, text="Thống kê",
                          font=("Arial", 8, "bold"), fg="White", borderwidth=0,
                          bg="light blue", pady=2)
    btn_thang_kh.place(x=140, y=9)
    fram_bieudo = Frame(frame_container, bg='white')
    fram_bieudo.place(x=0, y=50)
def thongke_ve():
    frame_container = Frame(index, bg="red", width=500, height=400)
    frame_container.place(x=150, y=0)

    input_thang = DateEntry(frame_container, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                            borderwidth=0, width=10, date_pattern="dd/mm/yyyy")
    input_thang.place(x=30, y=9)
    btn_thang_kh = Button(frame_container, text="Thống kê",
                          font=("Arial", 8, "bold"), fg="White", borderwidth=0,
                          bg="light blue", pady=2)
    btn_thang_kh.place(x=140, y=9)
    fram_bieudo = Frame(frame_container, bg='white')
    fram_bieudo.place(x=0, y=50)

frame_btntb = Frame(index, bg='white', width=140, height=300)
frame_btntb.place(x= 0 , y=30)

btn_khach = Button(frame_btntb, text="Thống kê khách hàng",
                font=("Arial", 8, "bold"), fg="White", borderwidth=0,
                bg="light blue", pady=6, padx=10,command=thongke_khachhang)
btn_khach.place(x=0, y= 0)
btn_tau = Button(frame_btntb, text="Thống kê tàu",
                font=("Arial", 8, "bold"), fg="White", borderwidth=0,
                bg="light blue", pady=6, padx=32, command=thongke_tau)
btn_tau.place(x=0, y= 40)
btn_ve = Button(frame_btntb, text="Thống kê vé",
                font=("Arial", 8, "bold"), fg="White", borderwidth=0,
                bg="light blue", pady=6, padx=34, command=thongke_ve)
btn_ve.place(x=0, y= 80)



index.mainloop()