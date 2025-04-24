import tkinter as tk
from tkinter import messagebox, Menu, Scrollbar
from datetime import datetime

semua_catatan = {}

def tambah_catatan():
    judul = kotak_judul.get().strip()
    isi = kotak_isi.get("1.0", tk.END).strip()
    if not judul or not isi:
        messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
        return
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M")
    label = f"{judul} ({waktu})"
    semua_catatan[label] = (isi, waktu)
    daftar_catatan.insert(tk.END, label)
    kotak_judul.delete(0, tk.END)
    kotak_isi.delete("1.0", tk.END)

def tampilkan_catatan(event):
    try:
        pilihan = daftar_catatan.get(daftar_catatan.curselection())
        isi, _ = semua_catatan[pilihan]
        kotak_isi.delete("1.0", tk.END)
        kotak_isi.insert(tk.END, isi)
    except:
        pass

def hapus_catatan():
    try:
        pilihan = daftar_catatan.get(daftar_catatan.curselection())
        konfirmasi = messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus '{pilihan}'?")
        if konfirmasi:
            daftar_catatan.delete(daftar_catatan.curselection())
            del semua_catatan[pilihan]
            kotak_isi.delete("1.0", tk.END)
    except:
        messagebox.showerror("Error", "Pilih catatan yang ingin dihapus.")

def tentang_aplikasi():
    messagebox.showinfo("Tentang", "Aplikasi Catatan Harian v1.0\nDibuat dengan Tkinter")

jendela = tk.Tk()
jendela.title("Catatan Harian")

menu_utama = Menu(jendela)
menu_file = Menu(menu_utama, tearoff=0)
menu_file.add_command(label="Keluar", command=jendela.quit)
menu_utama.add_cascade(label="File", menu=menu_file)

menu_bantuan = Menu(menu_utama, tearoff=0)
menu_bantuan.add_command(label="Tentang", command=tentang_aplikasi)
menu_utama.add_cascade(label="Bantuan", menu=menu_bantuan)

jendela.config(menu=menu_utama)

tk.Label(jendela, text="Judul:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
kotak_judul = tk.Entry(jendela, width=40)
kotak_judul.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

tk.Button(jendela, text="Tambah Catatan", command=tambah_catatan).grid(row=1, column=1, sticky="e", padx=5)
tk.Button(jendela, text="Hapus Catatan", command=hapus_catatan).grid(row=1, column=2, sticky="w", padx=5)

daftar_catatan = tk.Listbox(jendela, width=30, height=15)
daftar_catatan.grid(row=2, column=0, padx=5, pady=5, sticky="n")
scrollbar = Scrollbar(jendela, orient="vertical", command=daftar_catatan.yview)
scrollbar.grid(row=2, column=1, sticky="nsw")
daftar_catatan.config(yscrollcommand=scrollbar.set)
daftar_catatan.bind("<<ListboxSelect>>", tampilkan_catatan)

kotak_isi = tk.Text(jendela, width=50, height=15, state=tk.NORMAL)
kotak_isi.grid(row=2, column=2, padx=5, pady=5)

jendela.mainloop()
