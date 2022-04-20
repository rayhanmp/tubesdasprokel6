from primitives import countRow, konso

def addGame(game):
    # Menambahkan data game baru ke dalam list game sesuai input
    # I.S : sebuah list of list berisi string
    # F.S : sebuah list of list baru berisi string
    
    # KAMUS LOKAL
    # id, name, category, year, price, stock : string
    # n_row : int
    # newData : list of list berisi string

    # ALGORITMA
    name, category, year, price, stock = inputGame()
    n_row = countRow(game) # Hitung n_row
    id = ("G"+f"{(n_row):03}") # Hitung Field ID Game

    # Buat list dan lakukan penggabungan
    data = [id, name, category, year, price, stock] # Buat list berisi ID dan input
    newData = konso(data, game) # Inisiasi list of list newData sebagai return dari konso(data, game)

    return newData # Kembalikan list of list berisi string baru

def inputGame():
    # 
    # 
    # 

    # KAMUS LOKAL

    # ALGORITMA
    # Minta input pada user
    name = input("Masukan nama game: ")
    category = input("Masukan kategori: ")
    year = input("Masukan tahun rilis: ")
    price = input("Masukan harga: ")
    stock = input("Masukan stok awal: ")

    # Validasi apakah input benar, jika tidak, ulangi
    # While digunakan karena dapat bertindak sebagai pembatas (jika kondisi tidak terpenuhi, tidak dijalankan)
    while name == "" or category == "" or year == "" or price == "" or stock == "":
        print("\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        name = input("Masukan nama game: ")
        category = input("Masukan kategori: ")
        year = input("Masukan tahun rilis: ")
        price = input("Masukan harga: ")
        stock = input("Masukan stok awal: ")

    print("Selamat! Berhasil menambahkan game", name) # Apabila looping while telah berhenti, lakukan print
 
    return name, category, year, price, stock # Kembalikan variabel name, category, year, price, dan stock