import tkinter as tk 
from tkinter import ttk, messagebox, PhotoImage
from tkinter.ttk import Combobox
from tkinter import filedialog
from PIL import Image
import os

def ProgramStart():
    try:

        def cikis():
            sor = messagebox.askyesno("FormatRyce","Çıkmak istediğinizden emin misiniz?")

            if sor == True:
                pencere.destroy()

        def about():
            def close():
                hakkinda_pencere.destroy()

            hakkinda_pencere = tk.Toplevel()
            hakkinda_pencere.title("FormatRyce | Hakkında")
            hakkinda_pencere.geometry("350x200+350+350")
            hakkinda_pencere.resizable(False,False)
            icon_hakkinda = PhotoImage(file="formatryce_logo.PNG")
            hakkinda_pencere.iconphoto(False, icon_hakkinda)
            hakkinda_pencere.attributes("-topmost",True)

            baslik_hakkinda = tk.Label(hakkinda_pencere, text="FormatRyce Hakkında", fg="Red", font="Arial 15 bold")
            baslik_hakkinda.pack()

            gelisme = tk.Label(hakkinda_pencere, text="FormatRyce .png veya \nfarklı formatta olan\ndosyaları istenilen formata çeviren\nbasit bir resim uzantı programıdır.\n\nVersion : 1.5.0 [PRE-ALPHA]", font="Arial 13 bold")
            gelisme.pack()

            kapat = ttk.Button(hakkinda_pencere, text="Kapat", command=close)
            kapat.pack()
            kapat.place(x="130", y="160")

            hakkinda_pencere.mainloop()

        def enterr():
            if resim_yolu.get().strip() == "":
                messagebox.showerror("FormatRyce","Lütfen resim dosyasının yolunu giriniz!")
            else:

                if resim_adlandir.get().strip() == "":
                    messagebox.showerror("FormatRyce","Lütfen resim dosyanızı adlandırınız!")
                else:

                    if resim_format.get().strip() == "":
                        messagebox.showerror("FormatRyce","Lütfen değiştirmek istediğiniz dosya formatını seçiniz! ya da dosya yolunu kontrol ediniz!")
                    else:
                        if resim_format.get().strip() == "PNG":
                            try:
                                image = Image.open(resim_yolu.get().strip())
                                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                                resim_adlandir_now = f"{resim_adlandir.get().strip()}.png"
                                now_image = os.path.join(desktop_path, resim_adlandir_now)
                                image.save(now_image)
                                messagebox.showinfo("FormatRyce",f"{resim_adlandir.get().strip()} Adında bir PNG dosyası masaüstünüze oluşturuldu!")
                            except:
                                messagebox.showerror("FormatRyce","Resim dosya formatı değiştirilemedi!")

                        if resim_format.get().strip() == "İCO":
                            try:
                                image = Image.open(resim_yolu.get().strip())
                                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                                resim_adlandir_now = f"{resim_adlandir.get().strip()}.ico"
                                now_image = os.path.join(desktop_path, resim_adlandir_now)
                                image.save(now_image)
                                messagebox.showinfo("FormatRyce",f"{resim_adlandir.get().strip()} Adında bir İCO dosyası masaüstünüze oluşturuldu!")
                            except:
                                messagebox.showerror("FormatRyce","Resim dosya formatı değiştirilemedi!")

                        if resim_format.get().strip() == "JPEG":
                            try:
                                image = Image.open(resim_yolu.get().strip())
                                image = image.convert("RGB")
                                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                                resim_adlandir_now = f"{resim_adlandir.get().strip()}.jpeg"
                                now_image = os.path.join(desktop_path, resim_adlandir_now)
                                image.save(now_image)
                                messagebox.showinfo("FormatRyce",f"{resim_adlandir.get().strip()} Adında bir JPEG dosyası masaüstünüze oluşturuldu!")
                            except:
                                messagebox.showerror("FormatRyce","Resim dosya formatı değiştirilemedi!")

                        if resim_format.get().strip() == "GİF":
                            try:
                                image = Image.open(resim_yolu.get().strip())
                                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                                resim_adlandir_now = f"{resim_adlandir.get().strip()}.gif"
                                now_image = os.path.join(desktop_path, resim_adlandir_now)
                                image.save(now_image)
                                messagebox.showinfo("FormatRyce",f"{resim_adlandir.get().strip()} Adında bir GİF dosyası masaüstünüze oluşturuldu!")
                            except:
                                messagebox.showerror("FormatRyce","Resim dosya formatı değiştirilemedi!")

        def yolu_sec():
            dosya_yolu_acma = filedialog.askopenfilename(title="Görsel Dosyasını Seçiniz")

            if dosya_yolu_acma:
                resim_yolu.delete(0, tk.END)
                resim_yolu.insert(0, dosya_yolu_acma)

        def delete_entry_data():
            eminmisin = messagebox.askyesno("FormatRyce","Entry bilgilerini silmek istediğinden emin misin?")

            if eminmisin == True:
                resim_yolu.delete(0, tk.END)
                resim_adlandir.delete(0, tk.END)
                resim_format.delete(0, tk.END)

        def updates():
            def kapat_update():
                update_pencere.destroy()

            update_pencere = tk.Toplevel()
            update_pencere.geometry("310x160+350+350")
            update_pencere.resizable(False,False)
            icon_update = PhotoImage(file="formatryce_logo.PNG")
            update_pencere.iconphoto(False, icon_update)
            update_pencere.title("FormatRyce | Güncelleme")
            update_pencere.attributes("-topmost", True)

            baslik_updates = tk.Label(update_pencere, text="Güncellemeler", fg="red", font="Arial 18 bold")
            baslik_updates.pack()

            gelisme_updates = tk.Label(update_pencere, text="Güncelleme Yok", fg="black", font="Arial 13 bold")
            gelisme_updates.pack()

            kapat_updates = ttk.Button(update_pencere, text="Kapat", command=kapat_update)
            kapat_updates.pack()

            update_pencere.mainloop()

        pencere = tk.Tk()
        pencere.geometry("250x290+500+400")
        pencere.resizable(False, False)
        pencere.title("FormatRyce")
        icon = PhotoImage(file="formatryce_logo.PNG")
        pencere.iconphoto(False, icon)
        pencere.attributes("-topmost", False)

        baslik = tk.Label(text="FormatRyce", fg="blue", font="Arial 15 bold")
        baslik.pack()
        baslik.place(x="70", y="10")

        resim_yolu_text = tk.Label(text="Dosya Yolu :", fg="red", font="Arial 13 bold")
        resim_yolu_text.pack()
        resim_yolu_text.place(x="80", y="45")

        resim_yolu = ttk.Entry(width=35)
        resim_yolu.pack()
        resim_yolu.place(x="20", y="67")

        resim_adlandir_text = tk.Label(text="Resim Adı :", fg="red", font="Arial 13 bold")
        resim_adlandir_text.pack()
        resim_adlandir_text.place(x="85", y="115")

        resim_adlandir = ttk.Entry()
        resim_adlandir.pack()
        resim_adlandir.place(x="65", y="140")

        resim_format_text = tk.Label(text="Dosya Türü :", fg="red", font="Arial 13 bold")
        resim_format_text.pack()
        resim_format_text.place(x="75", y="175")

        resim_format = Combobox(values=("PNG","JPEG","İCO","GİF"))
        resim_format.pack()
        resim_format.place(x="55", y="200")

        enter = ttk.Button(text="Enter", command=enterr)
        enter.pack()
        enter.place(x="89", y="240")

        dosya_yolu_sec = ttk.Button(text="Dosya Yolu Seç",command=yolu_sec)
        dosya_yolu_sec.pack()
        dosya_yolu_sec.place(x="81", y="88")

        menu = tk.Menu()
        pencere.config(menu=menu)

        secilen_menu = tk.Menu(pencere, tearoff=0)
        image_menu = tk.Menu(pencere, tearoff=0)
        application_info = tk.Menu(pencere, tearoff=0)

        menu.add_cascade(label="Menu", menu=secilen_menu)
        application_info.add_command(label="Hakkında", command=about)
        application_info.add_command(label="Güncelleme", command=updates)
        secilen_menu.add_cascade(label="Görsel", menu=image_menu)
        secilen_menu.add_cascade(label="Bilgi", menu=application_info)
        image_menu.add_command(label="Entry Bilgilerini Temizle", command=delete_entry_data)
        image_menu.add_command(label="Görsel Formatı Değiştir", command=enterr)
        secilen_menu.add_separator()
        secilen_menu.add_command(label="Çıkış", command=cikis)

        pencere.mainloop()

    except Exception as AppError:
        os.system("cls")
        print(f"AppMessage: {AppError}")

if __name__ == "__main__":
    ProgramStart()
