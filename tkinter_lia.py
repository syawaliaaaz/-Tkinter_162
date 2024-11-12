import tkinter as tk  # mengimpor library tkinter sebagai tk untuk membuat GUI

def prediksi_prodi():
    # fungsi untuk menampilkan prediksi prodi (sementara, selalu menampilkan Teknologi Informasi)
    hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")

# membuat jendela utama GUI
root = tk.Tk()  # membuat jendela utama dengan nama root
root.title("Aplikasi Prediksi Prodi Pilihan")  # memberi judul jendela utama
root.configure(bg="pink")  # mengatur background (bg) menjadi warna pink

# membuat label judul dan mengatur font-nya
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Segoe UI Black", 18))  
judul_label.pack(pady=10)  # menempatkan label judul di tengah jendela dengan jarak vertikal 10 piksel

# membuat frame untuk input nilai
nilai_frame = tk.Frame(root)  # membuat frame bernama nilai_frame untuk menampung input nilai
nilai_frame.pack()  # menempatkan frame di jendela utama

# membuat input nilai mata pelajaran dengan tata letak grid yang lebih baik
for i in range(10):  # loop untuk membuat 10 label dan entry input nilai
    nilai_label = tk.Label(nilai_frame, text=f"Nilai Mata Pelajaran {i+1}:")  # label untuk setiap mata pelajaran
    nilai_label.grid(row=i, column=0, sticky="e")  # menempatkan label di kolom 0, baris arah kanan
    nilai_entry = tk.Entry(nilai_frame)  # membuat entry untuk input nilai
    nilai_entry.grid(row=i, column=1, padx=10)  # menempatkan entry di kolom 1 dengan jarak horizontal 10 piksel

# membuat tombol hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi)  # tombol untuk memprediksi prodi
prediksi_button.pack(pady=10)  # menempatkan tombol di tengah jendela dengan jarak vertikal 10 piksel

# membuat label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="")  # membuat label kosong untuk hasil prediksi
hasil_label.pack()  # menempatkan label hasil di bawah tombol

# menjalankan aplikasi
root.mainloop()  # menjalankan loop utama tkinter agar jendela tetap tampil
