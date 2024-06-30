import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from index import show_index
import re

def ketnoi():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="quanlybanve"
    )

def login():
    taikhoan = input_tk.get()
    matkhau = input_mk.get()

    con = ketnoi()
    cur = con.cursor()
    if not taikhoan or not matkhau:
        messagebox.showerror("Thông báo", "Tên đăng nhập và mật khẩu không được để trống!")
        return
    try:
        cur.execute("SELECT * FROM taikhoan WHERE tk=%s AND mk=%s", (taikhoan, matkhau))
        result = cur.fetchone()
        if result:
            messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
            show_index(dangnhap)
        else:
            messagebox.showerror("Thông báo", "Tên đăng nhập hoặc mật khẩu không đúng!")
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi kết nối tới cơ sở dữ liệu: {err}")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def dangky_taikhoan(dangnhap_window, input_tk_dk, input_mk_dk, input_email_dk):
    dk_tk = input_tk_dk.get()
    dk_mk = input_mk_dk.get()
    dk_email = input_email_dk.get()

    if not dk_tk or not dk_mk or not dk_email:
        messagebox.showerror("Thông báo", "Vui lòng điền đầy đủ thông tin!")
        return
    if len(dk_tk) < 10:
        messagebox.showerror("Thông báo", "Tài khoản phải có ít nhất 10 ký tự")
        return
    if len(dk_mk) < 5:
        messagebox.showerror("Thông báo", "Mật Khẩu phải có ít nhất 5 ký tự")
        return
    if not dk_mk[0].isupper():
        messagebox.showerror("Thông báo", "Mật Khẩu phải bắt đầu bằng chữ cái viết hoa")
        return
    if not re.search(r'[A-Za-z]', dk_mk) or not re.search(r'\d', dk_mk):
        messagebox.showerror("Thông báo", "Mật Khẩu phải chứa cả chữ và số")
        return
    if not dk_email.endswith("@gmail.com"):
        messagebox.showerror("Thông báo", "Email phải có đuôi @gmail.com!")
        return
    con = ketnoi()
    cur = con.cursor()
    try:
        cur.execute("SELECT tk FROM taikhoan WHERE tk = %s", (dk_tk,))
        result_tk = cur.fetchone()
        if result_tk:
            messagebox.showerror("Thông báo", "Tài khoản đã tồn tại!")
            return

        cur.execute("SELECT email FROM taikhoan WHERE email = %s", (dk_email,))
        result_email = cur.fetchone()
        if result_email:
            messagebox.showerror("Thông báo", "Email đã tồn tại!")
            return

        cur.execute("INSERT INTO taikhoan (email, tk, mk) VALUES (%s, %s, %s)", (dk_email, dk_tk, dk_mk))
        con.commit()
        messagebox.showinfo("Thông báo", "Đăng ký thành công!")
        dangnhap_window.deiconify()
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi kết nối tới cơ sở dữ liệu: {err}")
    finally:
        con.close()

def dangky_window(dangnhap_window):
    dangnhap_window.withdraw()
    dangnhap_window.withdraw()
    dangky = Toplevel()
    dangky.title('Đăng ký')
    dangky.geometry('700x400')
    center_window(dangky, 700, 400)

    image_dk = Image.open(r'D:\BAITAPCACMON\BT-CODE\PY\btl_python\img\backgroud.jpg')
    background_image_dk = ImageTk.PhotoImage(image_dk)
    canvas_dk = Canvas(dangky, width=dangky.winfo_screenwidth(), height=dangky.winfo_screenheight())
    canvas_dk.pack(fill=BOTH, expand=YES)

    def resize_image_dk(event):
        new_width = event.width
        new_height = event.height
        resized_image_dk = image_dk.resize((new_width, new_height), Image.LANCZOS)
        background_image_resized_dk = ImageTk.PhotoImage(resized_image_dk)
        canvas_dk.create_image(0, 0, anchor=NW, image=background_image_resized_dk)
        canvas_dk.image = background_image_resized_dk

    canvas_dk.bind("<Configure>", resize_image_dk)

    frame_dk = Frame(dangky, bg="white", width=400, height=350)
    frame_dk.place(relx=0.5, rely=0.5, anchor=CENTER)

    lb_dk = Label(frame_dk, text="Đăng Ký", fg="gray", font=("Arial", 20, "bold"), bg='White')
    lb_dk.place(x=150, y=30)

    lb_tk_dk = Label(frame_dk, text="Tài Khoản", fg="gray", font=("Arial", 10, "bold"), bg='White')
    lb_tk_dk.place(x=50, y=100)

    lb_mk_dk = Label(frame_dk, text="Mật Khẩu", fg="gray", font=("Arial", 10, "bold"), bg='White')
    lb_mk_dk.place(x=50, y=160)

    lb_email_dk = Label(frame_dk, text="Email", fg="gray", font=("Arial", 10, "bold"), bg='White')
    lb_email_dk.place(x=50, y=220)
    def on_enter(e):
        input_tk_dk.delete(0, 'end')
    def on_leave(e):
        name=input_tk_dk.get()
        if name == '':
            input_tk_dk.insert(0,'Tài Khoản')
    input_tk_dk = Entry(frame_dk, fg="gray", font=("Arial", 12), highlightbackground="light blue", highlightthickness=1, borderwidth=0)
    input_tk_dk.place(x=150, y=100)
    input_tk_dk.insert(0,"Tài Khoản")
    input_tk_dk.bind('<FocusIn>', on_enter)
    input_tk_dk.bind('<FocusOut>', on_leave)
    noot = Label(frame_dk, fg="gray",text="tài khoản phải nhập 10 kí trở lên", font=("Arial", 8, "italic"), bg='White')
    noot.place(x=150, y =130)
    def on_enter(e):
        input_mk_dk.delete(0, 'end')
    def on_leave(e):
        name=input_mk_dk.get()
        if name == '':
            input_mk_dk.insert(0,'Mật Khẩu')
    input_mk_dk = Entry(frame_dk, fg="gray", font=("Arial", 12), highlightbackground="light blue", show="*", highlightthickness=1, borderwidth=0)
    input_mk_dk.place(x=150, y=160)
    input_mk_dk.insert(0,"Mật Khẩu")
    input_mk_dk.bind('<FocusIn>', on_enter)
    input_mk_dk.bind('<FocusOut>', on_leave)
    noot = Label(frame_dk, fg="gray", text="trên 5 kị tự, viết hoa chữ đầu, có cả số và chữ", font=("Arial", 8, "italic"), bg='White')
    noot.place(x=150, y=190)
    def on_enter(e):
        input_email_dk.delete(0, 'end')
    def on_leave(e):
        name=input_email_dk.get()
        if name == '':
            input_email_dk.insert(0,'x@gmail.com')
    input_email_dk = Entry(frame_dk, fg="gray", font=("Arial", 12), highlightbackground="light blue", highlightthickness=1, borderwidth=0)
    input_email_dk.place(x=150, y=220)
    input_email_dk.insert(0,"x@gmail.com")
    input_email_dk.bind('<FocusIn>', on_enter)
    input_email_dk.bind('<FocusOut>', on_leave)
    def hienthi_mk_dk():
        if input_mk_dk["show"] == "*":
            input_mk_dk.config(show="")
        else:
            input_mk_dk.config(show="*")

    anh_dk = Image.open(r'D:\BAITAPCACMON\BT-CODE\PY\btl_python\img\iconmk.webp')
    size_dk = anh_dk.resize((20, 10), Image.LANCZOS)
    img_dk = ImageTk.PhotoImage(size_dk)

    btn_mat_dk = Button(frame_dk, image=img_dk, command=hienthi_mk_dk, highlightbackground="black", highlightthickness=1, borderwidth=0)
    btn_mat_dk.place(x=310, y=250)

    btn_dangnhap_dk = Button(frame_dk, text="Đăng ký", bg="#57a1f8", fg="White", font=("Arial", 10, "bold"), padx=30, pady=3, borderwidth=0, command=lambda: dangky_taikhoan(dangnhap_window, input_tk_dk, input_mk_dk, input_email_dk))
    btn_dangnhap_dk.place(x=50, y=280)

    btn_huy_dk = Button(frame_dk, text="Hủy", bg="#57a1f8", fg="White", font=("Arial", 10, "bold"), padx=46, pady=3, borderwidth=0, command=lambda: on_cancel(dangky, dangnhap_window))
    btn_huy_dk.place(x=215, y=280)

    def on_cancel(window, dangnhap_window):
        window.destroy()
        dangnhap_window.deiconify()

    dangky.mainloop()

if __name__ == "__main__":
    dangnhap = Tk()
    dangnhap.title('Đăng nhập')
    dangnhap.geometry('700x400')
    center_window(dangnhap, 700, 400)
    dangnhap.attributes("-topmost", True)

    image = Image.open("D:/BAITAPCACMON/BT-CODE/PY/btl_python/img/backgroud.jpg")
    background_image = ImageTk.PhotoImage(image)

    canvas = Canvas(dangnhap, width=dangnhap.winfo_screenwidth(), height=dangnhap.winfo_screenheight())
    canvas.pack(fill=BOTH, expand=YES)

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        background_image_resized = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0, 0, anchor=NW, image=background_image_resized)
        canvas.image = background_image_resized

    canvas.bind("<Configure>", resize_image)

    frame = Frame(dangnhap, bg="white", width=400, height=350)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    lb = Label(frame, text="Đăng Nhập", fg="gray", font=("Arial", 20, "bold"), bg='White')
    lb.place(x=150, y=30)

    lb_tk = Label(frame, text="Tài Khoản", fg="gray", font=("Arial", 10, "bold"), bg='White')
    lb_tk.place(x=50, y=100)

    lb_mk = Label(frame, text="Mật Khẩu", fg="gray", font=("Arial", 10, "bold"), bg='White')
    lb_mk.place(x=50, y=160)
    def on_enter(e):
        input_tk.delete(0, 'end')
    def on_leave(e):
        name=input_tk.get()
        if name == '':
            input_tk.insert(0,'Tài Khoản')

    input_tk = Entry(frame, fg="gray", font=("Arial", 12), highlightbackground="light blue", highlightthickness=1, borderwidth=0)
    input_tk.place(x=150, y=100)
    input_tk.insert(0,"Tài Khoản")
    input_tk.bind('<FocusIn>', on_enter)
    input_tk.bind('<FocusOut>', on_leave)

    def on_enter(e):
        input_mk.delete(0, 'end')
    def on_leave(e):
        name=input_mk.get()
        if name == '':
            input_mk.insert(0,'Mật Khẩu')
    input_mk = Entry(frame, fg="gray", font=("Arial", 12), highlightbackground="light blue", show="*", highlightthickness=1, borderwidth=0)
    input_mk.place(x=150, y=160)
    input_mk.insert(0, "Mật Khẩu")
    input_mk.bind('<FocusIn>', on_enter)
    input_mk.bind('<FocusOut>', on_leave)
    def hienthi_mk():
        if input_mk["show"] == "*":
            input_mk.config(show="")
        else:
            input_mk.config(show="*")

    anh = Image.open(r'D:\BAITAPCACMON\BT-CODE\PY\btl_python\img\iconmk.webp')
    size = anh.resize((20, 10), Image.LANCZOS)
    img = ImageTk.PhotoImage(size)

    btn_mat = Button(frame, image=img, command=hienthi_mk, highlightbackground="black", highlightthickness=1, borderwidth=0)
    btn_mat.place(x=310, y=190)

    btn_dangnhap = Button(frame, text="Đăng nhập", bg="#57a1f8", fg="White", font=("Arial", 10, "bold"), padx=30, pady=3, borderwidth=0, command=login)
    btn_dangnhap.place(x=50, y=250)

    btn_dangky = Button(frame, text="Đăng ký", bg="#57a1f8", fg="White", font=("Arial", 10, "bold"), padx=45, pady=3, borderwidth=0, command=lambda: dangky_window(dangnhap))
    btn_dangky.place(x=215, y=250)

    dangnhap.mainloop()
