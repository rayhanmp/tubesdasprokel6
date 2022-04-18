# Import modul yang diperlukan
from help import printNotAdmin, printNotLoggedIn, printNotUser

def isPermitted(isLoggedIn, isAdmin, allowedRole):
    # Menentukan permission berdasarkan 
    # I.S : Status log in, role (admin?), dan role yang dizinkan
    # F.S : boolean yang menyatakan permission

    # Kamus Lokal

    # Algoritma
    if allowedRole == "login/user": # Jika harus login dan role = user
        if isLoggedIn: # Cek Status Login
            if isAdmin: # Cek Status Admin
                # Jika bukan user, permission = False
                printNotUser()
                return False
            else: # adalah user, permission = true
                return True
        else: # not Logged In
            printNotLoggedIn()
            return False

    elif allowedRole == "login/admin": # Jika harus login dan role = user
        if isLoggedIn: # Cek Status Login
            if isAdmin: # Cek Status Admin
                # Jika admin, permission = True
                return True
            else: # bukan admin
                printNotAdmin()
                return False                
        else: # not Logged In
            printNotLoggedIn()
            return False

    elif allowedRole == "login/both": # Jika harus login dan boleh user/admin
        if isLoggedIn: # Cukup validasi login saja
            return True            
        else:
            printNotLoggedIn()
            return False

def countRow(list):
    # Menghitung panjang / banyaknya baris pada csv
    # I.S : sebuah list of string
    # F.S : panjang / jumlah baris pada list tersebut

    # Kamus Lokal
    # count : int

    # Algoritma
    count = 0
    for i in list:
        # Pada setiap baris di list, count ditambah 1
        count += 1
    return count

def konso(add,targetList):
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