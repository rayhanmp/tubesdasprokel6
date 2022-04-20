from primitives import countRow

def getIndexGame(game, id_game):
    # Mencari index urutan row game di list game berdasarkan ID Game
    # I.S : sebuah list of string dan string
    # F.S : sebuah integer berupa index baris game yang hendak diubah

    # KAMUS LOKAL
    # found : bool
    # i, index, n_row : int

    # ALGORITMA
    # Deklarasi variabel 
    found = False
    i = 0
    index = 0

    # Hitung jumlah row dalam list game
    n_row = countRow(game)

    # Cek index id_game
    while i < (n_row) and found == False: # Jika i lebih kecil dari n_row dan found bernilai false
        if game[i][0] == id_game: # Jika elemen pada row ke-i, kolom pertama sama dengan id_game
            found = True # Ubah nilai found untuk menghentikan loop
            index = i # Ubah nilai index menjadi i terakhir
        else: # Jika tidak, maka:
            i += 1  # Jumlahkan i dengan 1
    
    return index # Kembalikan index

def ubahGame(game):
    # Mengubah elemen list game pada baris tertentu dengan data baru sesuai input admin
    # I.S : sebuah list of string
    # F.S : list game berubah pada kolom dan baris tertentu sesuai input admin

    # KAMUS LOKAL
    # id_game, name, category, year, price : string
    # index : int

    # ALGORITMA
    id_game = input("Masukan ID game: ") # Minta input id_game

    index = getIndexGame(game, id_game) # Dapatkan nilai index dengan fungsi getIndexGame

    # Minta input data yang dapat diganti
    name = input("Masukan nama game: ")
    category = input("Masukan kategori: ")
    year = (input("Masukan tahun rilis: "))
    price = (input("Masukan harga: "))

    # Ganti informasi elemen pada list game, row sesuai index, dan kolom 1, 2, 3, 4
    if name != "": # Cek apakah input kosong
        game[index][1] = str(name)
    
    if category !="":
        game[index][2] = str(category)
    
    if year != "":
        game[index][3] = str(year)

    if price != "":
        game[index][4] = str(price)

    return game # Kembalikan list of list berisi string game

        