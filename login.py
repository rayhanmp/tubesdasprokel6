from load import countRow

def loginApp(user):
    # Memvalidasi input username dan password dari user
    # I.S : list yang berisi hasil konversi file user.csv
    # F.S : variable valid bertipe boolean, index bertipe integer
    
    # KAMUS LOKAL
    # index, i : int

    # ALGORITMA
    # Inisiasi variabel index, i, dan isLoggedIn
    isLoggedIn = False
    index = 0
    i = 0

    # Hitung jumlah row pada list user
    n_row = countRow(user) 
    
    # Minta input username dan password
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    # Validasi username dan isLoggedIn hasil input pada list user
    while i < (n_row) and isLoggedIn == False: # Jika i lebih kecil dari n_row dan isLoggedIn bernilai false
            if user[i][1] == username and user[i][3] == password: # Jika elemen pada row ke-i, kolom kedua dan keempat berturut-turut sama dengan input username dan password
                print("Halo", str(user[i][2])+"!", "Selamat datang di","Binomo")
                isLoggedIn = True # Ubah nilai isLoggedIn untuk menghentikan loop
                index = i # Ubah nilai index menjadi i terakhir
            else: # Jika tidak, maka:
                i += 1  # Jumlahkan i dengan 1

    # Cek apakah isLoggedIn masih bernilai false setelah i = n_row
    if isLoggedIn == False:
        print("Password atau username salah atau tidak ditemukan.")
    
    return isLoggedIn, index # Kembalikan dua variable yakni isLoggedIn dan index

def cekAdmin(user, index):
    # Mengecek apakah orang yang login merupakan user atau admin
    # I.S : list yang berisi hasil konversi file user.csv, index berupa integer dari urutan row orang yang telah sukses login
    # F.S : boolean yang menyatakan apakah orang yang login adalah admin atau bukan

    # KAMUS LOKAL
    # index : int

    # ALGORITMA
    if user[index][4] == "admin": # Jika elemen pada row (index) dan column (4) yang merupakan role adalah admin
        return True
    else: # Jika tidak, maka: 
        return False
