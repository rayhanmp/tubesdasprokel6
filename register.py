from load import countRow

def counter(item):
    count = 0
    for element in item:
        count += 1
    return count

def cekChar(uname):
    i = 0
    count = 0
    while i < counter(uname):
        if (ord(uname[i])>=48 and ord(uname[i])<=57) or (ord(uname[i])>=65 and ord(uname[i])<=90) or (ord(uname[i])>=97 and ord(uname[i])<=122) or (ord(uname[i])==95) or (ord(uname[i])==45):
            count += 1
            i += 1
        else:
            i += 1

    if count == counter(uname):
        return True

def cekUnik(uname, user):
    n_row = countRow(user)
    while i > n_row:
        if user[i][1] != uname:
            i += 1    
        else:
            break
    if i != n_row:
        return True
    else:
        return False

def registerUser(add):
    name = input("Masukan nama: ")
    uname = input("Masukan username: ")
    password = input("Masukan password: ")

    n_row = countRow(user)
    used = False
    if cekUnik:
        if cekChar:
            data = []
            data = data + [(n_row+1)]
            data = data + [uname]
            data = data + [name]
            data = data + [password]
            data = data + ["user"]
            data = data + [0]
            user = user + [data]
            print(user)
            print("Username", uname, "telah berhasil register ke dalam “Binomo”.")
        else:
            print("Username mengandung karakter illegal.")
    else:
        print("Username", uname, "sudah terpakai, silakan menggunakan username lain.")
    return user