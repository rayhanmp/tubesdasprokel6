import primitives
import search_my_game

def cari_game_5(game):
    # Mencari elemen yang cocok dengan input user lalu mencetak barisnya
    # I.S : sebuah list of string
    # F.S : baris yang mengandung elemen sesuai dengan input

    # KAMUS LOKAL
    # id, nama, kategori, tahun, harga : string
    # i, baris : integer
    # Cek : Bool

    # ALGORITMA
    # Deklarasi variabel
    id = str(input('Masukkan ID Game: '))
    nama = str(input('Masukkan nama Game: '))
    kategori = str(input('Masukkan kategori Game: '))
    tahun = str(input('Masukkan Tahun Rilis Game: '))
    harga = str(input('Masukkan Harga Game: '))

    i = 0
    baris = primitives.countRow(game)
    Cek = False

    print("\nDaftar game pada inventory yang memenuhi kriteria: ")
    while i < baris:  # Looping dalam batas jumlah baris
        if (  # semua kemungkinan yang mungkin terjadi
            (id == '' or id == game[i][0])
            and (nama == '' or nama == game[i][1])
            and (kategori == '' or kategori == game[i][2])
            and (tahun == '' or tahun == game[i][3])
            and (harga == '' or harga == game[i][4])
        ):
            # Mencetak baris yang memiliki elemen sama dengan input
            search_my_game.cetak_kolom(i, game)
            i += 1
            Cek = True
        else:
            i += 1  # Perubahan urutan barus yang akan dicek
    if Cek == False:  # Jika input tidak sama dengan semua elemen list
        print('tidak ada game pada inventory-mu yang memenuhi kriteria')
