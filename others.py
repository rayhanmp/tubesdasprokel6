import time

def kerangajaib():
    # Menjawab semua pertanyaan hidup (secara random)
    # I.S : Sebuah pertanyaan
    # F.S : Sebuah jawaban (Iya, Tidak, Mungkin, atau Bisa jadi)

    # Kamus Lokal
    # count, n_row, n_col : int
    # f : file di directory
    # csv_file : list of string (comma-delimited)
    # csv_list : list of (list of string)

    # Algoritma
    pertanyaan = input("Apa pertanyaanmu? ")
    start_time = time.time()


    a = 9
    b = 3
    m = 4

    x = 0
    count = 0
    while (start_time + 1) > time.time():
        x = (x*a + b) % m 

    if x == 0:
        print("Iya")
    elif x == 1:
        print("Mungkin")
    elif x == 2:
        print("Bisa jadi")
    elif x == 3:
        print("Tidak")

