import primitives

def TopUp(user):
    # Menambahkan saldo kepada user
    # I.S : Jumlah saldo yang ditambahkan
    # F.S : Jumlah saldo akhir

    # KAMUS LOKAL
    # username : string
    # i, saldo, baris : integer
    # userFound : boolean

    # ALGORITMA
    # Deklarasi variabel
    username = str(input('Masukkan username: '))
    saldo = int(input('Masukkan saldo: '))
    i = 0
    baris = primitives.countRow(user)

    while i < baris: # Looping dalam batas jumlah baris
        if username == user[i][1]: # Jika username tervalidasi
            if saldo > 0 : # Jika terjadi penambahan saldo awal
                print('Top up berhasil. Saldo ' + user[i][2] + ' bertambah menjadi ' + str(saldo+int(user[i][5])))
                user[i][5] = int(user[i][5]) + saldo
                return user # Kembalikan data yang sudah terupdate
            elif saldo < 0 and abs(saldo) < int(user[i][5]): # Jika terjadi pengurangan saldo akhir
                print('Top up berhasil. Saldo ' + user[i][2] + ' berkurang menjadi ' + str(saldo+int(user[i][5])))
                user[i][5] = int(user[i][5]) + saldo
                return user # Kembalikan data yang sudah terupdate
            else : # Jika jumlah pengurangan saldo lebih besar dibandingkan saldo awal
                print('Masukan tidak valid')
                return user # Kembalikan data semula
        else : # Mengecek username dalam batas
            i += 1

    # User tidak ditemukan
    print(f"Username “{username}” tidak ditemukan.")
    return user # Kembalikan data semula