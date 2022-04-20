from primitives import konso, countRow

def buy_game(id_user, arraygame, arrayuser, arraykepemilikan, arrayriwayat):
    # Membeli game dari toko
    # I.S : id user, array game, array user, dan array kepemilikan
    # F.S : array kepemilikan dan array user yang sudah terupdate berdasarkan pembelian

    # Kamus Lokal
    # game_id : string
    # found, user_found, have_game : boolean
    # bar, baris, stok : integer
    # saldo : float

    # Algoritma

    # id game
    game_id = input("Masukkan ID Game: ") 
    
    # cek apakah ID Game terdaftar
    game_found = False
    for i in range(countRow(arraygame)):
        if arraygame[i][0] == game_id:
            game_found = True
            bar = i
            break

    if game_found: # Game terdaftar
        # cek stok game
        stok = int(arraygame[bar][5])
        if stok <= 0:
            print("Stok Game tersebut sedang habis.")
        else: # stok > 0
            # cek user
            user_found = False
            for j in range(1, countRow(arrayuser)):
                if int(arrayuser[j][0]) == id_user:
                    user_found = True
                    baris = j
                    break

            if user_found:
                # cek apakah sudah memiliki game tersebut atau belum
                have_game = False
                for k in range (countRow(arraykepemilikan)):
                    if arraykepemilikan[k][0] == game_id and int(arraykepemilikan[k][1]) == id_user:
                        have_game = True
                        break

                if have_game == True: # game dimiliki user
                    print("Anda sudah memiliki game tersebut.")
                    return arraykepemilikan, arrayuser # return array awal

                else: # game tidak dimiliki user
                    # cek saldo user
                    saldo = float(arrayuser[baris][5])
                    if saldo < float(arraygame[bar][4]):
                        print("Saldo anda tidak cukup untuk membeli game tersebut.")
                        return arraykepemilikan, arrayuser # return array awal

                    else: # saldo cukup
                        # cek ketermilikan game oleh user                    
                        print("Game " + str(arraygame[bar][1]) + " berhasil dibeli.")
                        # konsokan kepemilikan baru
                        arraykepemilikan = konso([game_id, id_user], arraykepemilikan) 
                        # kurangi saldo user
                        arrayuser[baris][5] = float(arrayuser[baris][5]) - float(arraygame[bar][4]) 
                        # masukkan ke riwayat, by default tahun belinya adalah 2022
                        arrayriwayat = konso([game_id, arraygame[bar][1], arraygame[bar][4], id_user, 2022], arrayriwayat)
                        return arraykepemilikan, arrayuser, arrayriwayat # return array baru

            else: # user tidak ada
                print("ID user tidak ditemukan.")
                return arraykepemilikan, arrayuser # return array awal

    else: # game tidak ada
        print("ID Game tidak ditemukan.")
        return arraykepemilikan, arrayuser # return array awal