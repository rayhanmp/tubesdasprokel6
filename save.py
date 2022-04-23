# Modul save
# Modul untuk melakukan proses save data ke dalam folder tertentu

# Import modul yang diperlukan
from primitives import countRow
import os

# Fungsi dan Prosedur

def saveData(folder, data, filename):
    # Menyimpan sebuah file data ke folder
    # I.S : list data, nama file, dan folder yang ingin dituju
    # F.S : file data terbentuk di folder

    # Kamus Lokal
    # f : SEQFILE of string
    # csv_list : list of string (dengan format comma delimited seperti csv)

    # Algoritma
    f = open(folder + "/" + filename, 'w')  # Buat file di folder
    # Konversi list python ke bentuk list comma-delimited
    csv_list = listToCSV(data)

    f.writelines(csv_list)  # Tulis setiap baris ke dalam file


def saveAllData(user, game, riwayat, kepemilikan):
    # Menyimpan semua data ke folder
    # I.S : data user, game, riwayat, dan kepemilikan dalam bentuk python list
    # F.S : folder dengan 4 csv dari data di atas terbentuk

    # Kamus Lokal
    # folder : string

    # Algoritma
    folder = input("Masukkan nama folder penyimpanan: ")  # Input nama folder
    
    print("\nSaving...")
    if not os.path.exists(folder): # Belum ada foldernya
        os.mkdir(folder)  # Buat dengan library os
    
    # Save masing-masing data ke dalam folder tersebut
    saveData(folder, user, "user.csv")
    saveData(folder, game, "game.csv")
    saveData(folder, riwayat, "riwayat.csv")
    saveData(folder, kepemilikan, "kepemilikan.csv")

    print(f"Data telah disimpan pada folder {folder}!")


def listToCSV(data):
    # Mengkonversi list python ke dalam list comma-delimited
    # I.S : list data dalam format list python
    # F.S : list data dalam format comma-delimited

    # Kamus Lokal
    # n_row : int
    # csv_list : list of string

    # Algoritma    
    n_row = countRow(data) # Hitung jumlah baris
    csv_list = ["" for i in range(n_row)] # Inisiasi list

    for i in range(n_row):
        j = 0
        for col in data[i]: # Untuk setiap kolom di baris
            if j == 0: # Di awal, isi baris dengan data saja
                csv_list[i] += str(col)
                j += 1
            else: # Selanjutnya, tambahkan ";" di awal sebagai pemisah kolom
                csv_list[i] += ";" + str(col)
                j += 1
        # Tambahkan line break di akhir 
        csv_list[i] += "\n"

    return csv_list # Return list
