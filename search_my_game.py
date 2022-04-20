import primitives

def cetak_game(game, kepemilikan, userid):
    # mencetak semua elemen dalam list game
    # I.S : sebuah list of string
    # F.S : menampilkan semua elemen dalam list game

    # KAMUS LOKAL
    # i, j, baris : integer

    # ALGORITMA
    # Deklarasi variabel
    i = 1
    j = 0
    baris = primitives.countRow(game)

    while i < baris:  # Looping dalam batas jumlah baris
        # Print kolom id, nama, harga, kategori, dan tahun rilis
        if punya_game(kepemilikan, userid, game[i][0]):
            print(game[i][0] + ' | ' + game[i][1] + ' | ' + game[i]
                  [4] + ' | ' + game[i][2] + ' | ' + game[i][3])
        i += 1  # Penambahan nilai i untuk mencetak baris selanjutnya


def cetak_kolom(x, game):
    # mencetak semua elemen pada kolom tertentu dalam list game
    # I.S : index baris game dan list game
    # F.S : menampilkan semua elemen pada kolom tertentu dalam list game

    # KAMUS LOKAL

    # ALGORITMA
    # Print kolom id, nama, harga, kategori, dan tahun rilis
    print(game[x][0] + ' | ' + game[x][1] + ' | ' + game[x]
          [4] + ' | ' + game[x][2] + ' | ' + game[x][3])


def punya_game(kepemilikan, userid, gameid):
    # mencetak kepemilikan user terhadap sebuah game
    # I.S : list kepemilikan, user id dan game id
    # F.S : boolean apakah user memiliki game tersebut

    # KAMUS LOKAL
    # i, j, baris : interger

    # ALGORITMA
    # Print kolom id, nama, harga, kategori, dan tahun rilis
    i = 1
    baris = primitives.countRow(kepemilikan)
    while i < baris:
        if kepemilikan[i][0] == gameid and int(kepemilikan[i][1]) == userid:
            return True  # Jika kepemilikan ditemukan, return True
        i += 1
    # Else, tidak ketemu game dan user yang pas
    return False


def cari_game(game, kepemilikan, userid):
    # Mencari elemen yang cocok dengan input user lalu mencetak barisnya
    # I.S : sebuah list of string
    # F.S : baris yang mengandung elemen sesuai dengan input

    # KAMUS LOKAL
    # ID_Game, Tahun_Rilis : string
    # i, baris : integer
    # Cek : Bool

    # ALGORITMA
    # Deklarasi variabel
    ID_Game = str(input('Masukkan ID Game: '))
    Tahun_Rilis = str(input('Masukkan Tahun Rilis Game: '))
    i = 0
    baris = primitives.countRow(game)
    Cek = False

    if ID_Game == '' and Tahun_Rilis == '':  # Jika 2 parameter kosong
        print("\nDaftar game pada inventory yang memenuhi kriteria: ")
        cetak_game(game, kepemilikan, userid)

    elif ID_Game == '':  # Jika parameter ID_Game kosong
        print("\nDaftar game pada inventory yang memenuhi kriteria: ")
        while i < baris:
            if Tahun_Rilis == game[i][3]:  # Jika input terdapat pada list
                if punya_game(kepemilikan, userid, game[i][0]):
                    cetak_kolom(i, game)
                    Cek = True
                i += 1
            else:
                i += 1  # Mengecek baris lain
        if Cek == False:  # Jika input berbeda dengan semua elemen list
            print('tidak ada game pada inventory-mu yang memenuhi kriteria')

    elif Tahun_Rilis == '':  # Jika parameter Tahun_Rilis kosong
        print("\nDaftar game pada inventory yang memenuhi kriteria: ")
        while i < baris:
            if ID_Game == game[i][0]:  # Jika input terdapat pada list
                if punya_game(kepemilikan, userid, game[i][0]):
                    cetak_kolom(i, game)
                    Cek = True
                i += 1
            else:  # Mengecek baris lain
                i += 1
        if Cek == False:  # Jika input berbeda dengan semua elemen list
            print('tidak ada game pada inventory-mu yang memenuhi kriteria')

    else:  # Jika kedua input tidak kosong
        print("\nDaftar game pada inventory yang memenuhi kriteria: ")
        while i < baris:
            # Jika input sama dengan elemen list
            if ID_Game == game[i][0] and Tahun_Rilis == game[i][3]:
                if punya_game(kepemilikan, userid, game[i][0]):
                    cetak_kolom(i, game)
                    i += 1
                    Cek = True
            else:  # Mengecek baris lain
                i += 1
        if Cek == False:  # Jika input berbeda dengan semua elemen list
            print('tidak ada game pada inventory-mu yang memenuhi kriteria')
