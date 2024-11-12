import tkinter as tk #untuk membuat pengguna berbasis gui, dan disingkat menjadi tk

# Membuat jendela utama
window = tk.Tk()
window.title("Aplikasi Prediksi Prodi Pilihan") #judulnya
window.geometry("400x550")  # Mengatur ukuran jendela dgn lebar 400 piksel dan tinggi 550 piksel

# Label judul dgn jenis dan ukuran huruf (Arial, ukuran 16, dan bold untuk tebal).
label_judul = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
label_judul.pack(pady=10) #menempatkan label dgn jarak vertikal sebesar 10 piksel

# List untuk menyimpan input nilai dari pengguna
entries = []

# Membuat 10 input untuk nilai mata pelajaran
for i in range(10):  #untuk perulangan sbnyak 10 kali 
    label = tk.Label(window, text=f"Nilai Mata Pelajaran {i + 1}:") #untuk membuat label setiap mata pelajaran
    label.pack(anchor="w", padx=20) #menempatkan pada posisi horizontal
    
    entry = tk.Entry(window)  
    entry.pack(padx=20, pady=5)
    entries.append(entry)  #menambahkan kolom input ke dalam list entries agar dpt diakses

# Label untuk menampilkan hasil prediksi
label_hasil = tk.Label(window, text="", font=("Arial", 12), fg="blue") #label yang dimulai dgn teks kosong,(font arial ukuran 12)
label_hasil.pack(pady=20) #menempatkan diposisi vertikal

# Fungsi untuk menampilkan hasil prediksi
def tampilkan_prediksi():  #fungsi yang akan dijalankan ketika tombol ditekan.
    label_hasil.config(text="Prodi Pilihan: TeknologiInformasi")  #mengubah teks pada label_hasil menjadi "Prodi Pilihan: TeknologiInformasi".

# Tombol untuk memproses hasil prediksi
button_prediksi = tk.Button(window, text="Hasil Prediksi", command=tampilkan_prediksi)  #menjalankan fungsi tampilkan_prediksi ketika tombol ditekan.
button_prediksi.pack(pady=20)  #menempatkan pada posisi vertikal, 20 piksel

# Menjalankan aplikasi
window.mainloop()
