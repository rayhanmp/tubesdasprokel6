# Modul load
# Modul untuk melakukan proses load data csv ke bentuk python list

# Kamus
# parser : argparse.ArgumentParser (tipe dari modul argparse)
# args : argparse.Namespace (tipe dari modul argparse)

# Algoritma Program Utama
# Import modul yang diperlukan
import argparse
import os

try:
    parser = argparse.ArgumentParser(
        description="Mencari folder data di directory")  # Buat object parser dengan modul argparse
    parser.add_argument("folder_name", type=str, help="Folder Name") # Tambah argument folder_name
    args = parser.parse_args() # Simpan semua argument ke Namespace dengan parse_args()

except:  # Tidak ada argumen yang diberikan -> print error
    print("""\nTidak ada nama folder yang diberikan!
Usage: python main.py <nama_folder>""")

# Fungsi dan Prosedur

def isFolderExist():
    # Mengecek directory apakah folder_name tersedia 
    # I.S : folder_name yang di parse dari argument parser
    # F.S : boolean yang menyatakan keberadaan folder di directory

    # Kamus Lokal -

    # Algoritma
    try: # Mencegah error
        if os.path.exists(args.folder_name): # Folder ada di directory
            return True
        else: # Folder tidak ada di directory
            print("Folder \"{}\" tidak ditemukan.".format(args.folder_name))
            return False
    except NameError: # Mencegah error akibat argument tidak diberikan
        return False

def loadData(f):
    # Load data dari csv dalam bentuk python list
    # I.S : nama file data csv yang ingin di load (misal: "user.csv")
    # F.S : list of (list of column) dari csv

    # Kamus Lokal
    # folder, path : string

    # Algoritma    
    folder = args.folder_name # Nama folder dari argument parser

    path = folder + "/" + f # Path file data yang ingin di load
    return CSVtoList(path) # Return list yang sudah dikonversi oleh fungsi CSVtoList


def countColumn(row):
    # Menghitung jumlah kolom pada baris
    # I.S : sebuah string yang menggambarkan sebuah baris di csv (contoh: "id;username;nama")
    # F.S : jumlah kolom berdasarkan string tersebut

    # Kamus Lokal
    # count : int
    # char : string

    # Algoritma    
    count = 1 
    for char in row:
        # Setiap ada character ";" (pemisah kolom di csv), count ditambah 1  
        if char == ";": 
            count += 1
    return count


def countRow(list):
    # Menghitung panjang / banyaknya baris pada csv
    # I.S : sebuah list of string
    # F.S : panjang / jumlah baris pada list tersebut

    # Kamus Lokal
    # count : int

    # Algoritma
    count = 0
    for i in list:
        # Pada setiap baris di list, count ditambah 1
        count += 1
    return count


def CSVtoList(path):
    # Konversi file csv ke dalam list python
    # I.S : string yang melambangkan path dari file csv yang ingin dikonversi
    # F.S : list python dari csv tersebut

    # Kamus Lokal
    # count, n_row, n_col : int
    # f : file di directory
    # csv_file : list of string (comma-delimited)
    # csv_list : list of (list of string)

    # Algoritma
    f = open(path, "r") # Buka file sesuai path
    csv_file = f.readlines() # Baca isinya dalam bentuk list

    # Hitung banyak baris dan kolom
    n_row = countRow(csv_file)
    n_col = countColumn(csv_file[0]) 
    
    # Inisialisasi list
    csv_list = [["" for i in range(n_row)] for j in range(n_col)]

    for i in range(n_row): # Untuk setiap baris 
        j = 0
        for char in csv_file[i]: # Untuk setiap karakter di baris 
            if char == ";": # Jika karakter ";", pindah kolom
                j += 1
            else:
                csv_list[i][j] += char # Isi kolom

    return csv_list # Return list


def printWelcome():
    # Mencetak interface awal setelah data di load
    # I.S : data sudah di load
    # F.S : interface selamat datang yang tercetak

    # Kamus Lokal -
    
    # Algoritma
    print("""Loading...\n
Hi! BNMO here! Mau apa hari ini?
Ketik \"help\" jika perlu bantuan\n""")