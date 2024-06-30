from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import database

def show_ThongKe(frame_noidung):

    for widget in frame_noidung.winfo_children():
        widget.destroy()

    def thongke_khachhang():
        frame_container = Frame(frame_noidung, bg="white", width=850, height=700)
        frame_container.place(x=150, y=0)

        fram_bieudo = Frame(frame_container, bg='white')
        fram_bieudo.place(x=0, y=9)

        monthly_counts = database.analyze_customers_by_month()
        fig = plt.figure(figsize=(8, 5))
        plt.plot(monthly_counts.index.astype(str), monthly_counts.values, marker='o', linestyle='-')
        plt.xlabel('Tháng')
        plt.ylabel('Số lượng khách hàng')
        plt.title('Thống kê khách hàng')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        # Tạo canvas để nhúng đồ thị vào frame_noidung
        canvas = FigureCanvasTkAgg(fig, master=fram_bieudo)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def thongke_tau():
        frame_container = Frame(frame_noidung, bg="white", width=850, height=700)
        frame_container.place(x=150, y=0)


        fram_bieudo = Frame(frame_container, bg='white')
        fram_bieudo.place(x=0, y=9)

        # Lấy dữ liệu thống kê từ cơ sở dữ liệu
        seat_stats = database.get_seat_stats()

        # Tạo biểu đồ
        fig, ax = plt.subplots(figsize=(8, 5))
        tau = [row[0] for row in seat_stats]
        ghe_trong = [row[1] for row in seat_stats]
        ghe_khong_trong = [row[2] for row in seat_stats]

        bar_width = 0.35
        index = range(len(tau))

        ax.bar(index, ghe_trong, bar_width, label='Ghế Trống', color='b')
        ax.bar([i + bar_width for i in index], ghe_khong_trong, bar_width, label='Ghế Không Trống', color='r')

        ax.set_xlabel('Tên Tàu')
        ax.set_ylabel('Số Lượng Ghế')
        ax.set_title('Thống kê ghế trống và ghế không trống của từng tàu')
        ax.set_xticks([i + bar_width / 2 for i in index])
        ax.set_xticklabels(tau, rotation=45)
        ax.legend()

        plt.tight_layout()

        # Tạo canvas để nhúng đồ thị vào frame_noidung
        canvas = FigureCanvasTkAgg(fig, master=fram_bieudo)
        canvas.draw()
        canvas.get_tk_widget().pack()



    def thongke_ve():
        frame_container = Frame(frame_noidung, bg="white", width=850, height=700)
        frame_container.place(x=150, y=0)


        fram_bieudo = Frame(frame_container, bg='white')
        fram_bieudo.place(x=0, y=9)

        # Lấy dữ liệu thống kê từ cơ sở dữ liệu
        total_price_stats = database.get_total_ticket_price_by_month_year()

        # Xử lý dữ liệu để tạo danh sách tháng và tổng giá tiền vé tương ứng
        months = [f"{row[1]}/{row[0]}" for row in total_price_stats]
        total_prices = [row[2] for row in total_price_stats]

        # Tạo biểu đồ
        fig, ax = plt.subplots(figsize=(8, 5))

        ax.plot(months, total_prices, marker='o', linestyle='-', color='b')

        ax.set_xlabel('Tháng/Năm')
        ax.set_ylabel('Tổng Giá Vé (VND)')
        ax.set_title('Tổng Giá Vé theo Tháng và Năm')
        ax.tick_params(axis='x', rotation=45)

        plt.tight_layout()

        # Tạo canvas để nhúng đồ thị vào frame_noidung
        canvas = FigureCanvasTkAgg(fig, master=fram_bieudo)
        canvas.draw()
        canvas.get_tk_widget().pack()



    frame_btntb = Frame(frame_noidung, bg='white', width=140, height=300)
    frame_btntb.place(x=0, y=30)

    btn_khach = Button(frame_btntb, text="Thống kê khách hàng",
                       font=("Arial", 8, "bold"), fg="White", borderwidth=0,
                       bg="#57a1f8", pady=6, padx=10, command=thongke_khachhang)
    btn_khach.place(x=0, y=0)
    btn_tau = Button(frame_btntb, text="Thống kê tàu",
                     font=("Arial", 8, "bold"), fg="White", borderwidth=0,
                     bg="#57a1f8", pady=6, padx=32, command=thongke_tau)
    btn_tau.place(x=0, y=40)
    btn_ve = Button(frame_btntb, text="Thống kê vé",
                    font=("Arial", 8, "bold"), fg="White", borderwidth=0,
                    bg="#57a1f8", pady=6, padx=34, command=thongke_ve)
    btn_ve.place(x=0, y=80)



