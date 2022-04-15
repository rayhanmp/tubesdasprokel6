import time

def kerangajaib():
    # Menjawab semua pertanyaan hidup (secara random)
    # I.S : Sebuah pertanyaan
    # F.S : Sebuah jawaban (Iya, Tidak, Mungkin, atau Bisa jadi)

    # Kamus Lokal
    # a, b, m, x : int
    # start_time : float
    # pertanyaan : string

    # Algoritma
    # Input pertanyaan (Tidak berpengaruh)
    pertanyaan = input("Apa pertanyaanmu? ")
    start_time = time.time()  # Waktu program memulai

    # Konstanta yang digunakan untuk Linear congruential generator
    a = 9   # Penentuan konstanta memiliki syarat : b dan m saling prima, a-1 habis dibagi semua faktor prima m,
    b = 3   # dan jika m habis dibagi 4, a-1 harus habis dibagi 4
    m = 4   # m adalah periode pengacakan (m = 4, berarti ada 4 kemungkinan angka)

    # Nilai angka random
    x = 0
    while (start_time + 1) > time.time():  # Selama 1 detik belum terlewati
        # Rumus LCG yang akan menghasilkan x = 0, 1, 2, 3 secara periodik
        # Nilai x akan random tergantung performa komputer dalam 1 detik
        x = (x*a + b) % m

    # Output berdasarkan angka yang sudah di randomized
    if x == 0:
        print("Iya")
    elif x == 1:
        print("Mungkin")
    elif x == 2:
        print("Bisa jadi")
    elif x == 3:
        print("Tidak")