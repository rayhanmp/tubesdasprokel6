from bonuses import encrypt
from primitives import countRow, konso

def cekChar(uname):
    # Mengecek apakah input username tidak mengandung karakter ilegal
    # I.S : string username
    # F.S : boolean yang menyatakan apakah username legal atau tidak

    # Kamus Lokal
    # count, i : integer
    # element : any

    # Algoritma
    i = 0
    count = 0
    while i < countRow(uname):
        # Hitung elemen pada username yang masuk kategori legal
        if (ord(uname[i]) >= 48 and ord(uname[i]) <= 57) or (ord(uname[i]) >= 65 and ord(uname[i]) <= 90) or (ord(uname[i]) >= 97 and ord(uname[i]) <= 122) or (ord(uname[i]) == 95) or (ord(uname[i]) == 45):
            count += 1
            i += 1
        else:
            i += 1

    
    if count == countRow(uname): # Semua karakter terhitung legal
        return True
    else: # Ada karakter ilegal
        return False


def cekUnik(uname, user):
    # Mengecek apakah input username tidak mengandung karakter ilegal
    # I.S : string username dan data user
    # F.S : boolean yang menyatakan apakah username unik atau tidak

    # Kamus Lokal
    # n_row, i : integer

    # Algoritma
    n_row = countRow(user) # Banyak baris di data user

    for i in range(n_row):
        # Jika pada baris ditemukan username yang sama return False
        if user[i][1] == uname:
            return False

    # tidak ditemukan username sama, return True
    return True


def registerUser(user):
    # Menambahkan user ke database jika user tervalidasi
    # I.S : list data user
    # F.S : list data user yang baru, baik sudah ditambahkan user baru maupun tidak

    # Kamus Lokal
    # name, uname, password, id : string
    # n_row : integer

    # Algoritma
    # Input data user
    name = input("Masukan nama: ")
    uname = input("Masukan username: ")
    password = input("Masukan password: ")
    
    # Cek banyak baris data
    n_row = countRow(user)
    id = str(n_row)

    if cekUnik(uname, user): # Cek apakah username unik
        if cekChar(uname): # Cek apakah karakter pada username diperbolehkan
            
            # Sudah melewati validasi, data user bisa ditambahkan ke list data
            data = [id, uname, name, encrypt(password), "user", "0"]
            newData = (konso(data, user))
            print("Username", uname, "telah berhasil register ke dalam “Binomo”.")
            return newData 

        else: # Ada karakter ilegal
            print("Username mengandung karakter illegal.")
            return user
    else: # Username sudah terpakai
        print("Username", uname, "sudah terpakai, silakan menggunakan username lain.")
        return user
