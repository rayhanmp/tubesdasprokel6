import primitives

def kolom(x, riwayat):
    # Mencetak elemen pada baris tertentu
    # I.S : sebuah list of string
    # F.S : baris yang mengandung elemen sesuai dengan input

    # KAMUS LOKAL
    # y, baris : integer

    # ALGORITMA
    # Deklarasi variabel
    baris = primitives.countRow(riwayat)
    y = 0

    while y < 5: # Looping dalam batas jumlah kolom
        while x < baris: # Looping dalam batas jumlah baris
            print(riwayat[x][y] + ' | ', end='') # Mencetak elemen pada baris tertentu
            y += 1 # Perubahan index kolom untuk pengecekan selanjutnya
            if y == 5 : # Jika semua kolom sudah dicek
                break
            elif y == 3: # Output tidak melibatkan kolom index 3
                y += 1

def riwayat_beli(riwayat, userid):
    # Mencari elemen yang cocok dengan input user lalu mencetak barisnya
    # I.S : sebuah list of string
    # F.S : baris yang mengandung elemen sesuai dengan input

    # KAMUS LOKAL
    # user : string
    # i, baris : integer

    # ALGORITMA
    # Deklarasi variabel
    i = 1
    baris = primitives.countRow(riwayat)
    hasGame = False

    print("\nDaftar game: ")
    while i < baris: # Looping dalam batas baris
        if userid == int(riwayat[i][3]): # Jika username terdapat dalam list
            hasGame = True
            kolom(i, riwayat) # Mencetak baris sesuai input
            print('') # Pindah ke baris selanjutnya
        i += 1 # Pengecekan baris selanjutnya
    
    if not hasGame: # User tidak punya riwayat pembelian game
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")