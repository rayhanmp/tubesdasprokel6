from load import countRow

def konso (add,targetList):
    # Menambahkan sebuah list of string ke dalam list of string lainnya, berfungsi mirip Append
    # I.S : sebuah list of string yang hendak ditambahkan dan sebuah list of string tujuan
    # F.S : sebuah list of string baru yang merupakan gabungan kedua list 

    # KAMUS LOKAL
    # temp, targetlist : list di dalam list berisi string
    # add : list berisi string

    # ALGORITMA
    temp = [["" for i in range(countRow(targetList[0]))] for j in range((countRow(targetList)+1))] # Inisiasi list of list temp

    # Masukan isi targetList ke dalam list sementara
    for i in range(countRow(targetList)): 
        for j in range(countRow(targetList[0])):
            temp[i][j] = targetList[i][j] # Ganti elemen dengan index yang bersesuaian
    
    # Masukan isi data baru ke dalam list kosong dalam temp
    for j in range(countRow(targetList[0])):
        temp[countRow(targetList)][j] = add[j]

    return temp # Kembalikan list of list berisi string temp

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
    id = ("G"+f"{(n_row+1):03}") # Hitung Field ID Game

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
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        name = input("Masukan nama game: ")
        category = input("Masukan kategori: ")
        year = input("Masukan tahun rilis: ")
        price = input("Masukan harga: ")
        stock = input("Masukan stok awal: ")

    print("Selamat! Berhasil menambahkan game", name) # Apabila looping while telah berhenti, lakukan print
 
    return name, category, year, price, stock # Kembalikan variabel name, category, year, price, dan stock