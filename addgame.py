def addGame(game):
    name = input("Masukan nama game: ")
    category = input("Masukan kategori: ")
    year = int(input("Masukan tahun rilis: "))
    price = int(input("Masukan harga: "))
    stock = int(input("Masukan stok awal: "))

    while name == "" or category == "" or year == "" or price == "" or stock == "":
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        name = input("Masukan nama game: ")
        category = input("Masukan kategori: ")
        year = input("Masukan tahun rilis: ")
        price = input("Masukan harga: ")
        stock = input("Masukan stok awal: ")

    print("Selamat! Berhasil menambahkan game", name)
