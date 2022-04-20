from primitives import countRow

def list_game(arraykepemilikan, arraygame, id_user):
    # Listing game yang dimiliki
    # I.S : data kepemilikan, data game, dan id user
    # F.S : list game yang dimiliki tercetak

    # Kamus Lokal
    # temp1 : list of string
    # count, idx : integer
    # found : boolean

    # Algoritma    
    count = 0 
    for i in range(1, countRow(arraykepemilikan)): # hitung game yang dimiliki
        if id_user == int(arraykepemilikan[i][1]):
            count += 1

    # inisialisasi array dengan panjang sama dengan jumlah game yang dimiliki
    temp1 = ["" for i in range(count)]

    idx = 0 # isi array dengan id game yang dimiliki user
    for i in range(1, countRow(arraykepemilikan)):
        if id_user == int(arraykepemilikan[i][1]):
            temp1[idx] = arraykepemilikan[i][0]
            idx += 1

    if count > 0: # jika jumlah game user lebih dari 0
        print("\nDaftar game yang kamu miliki: ")
        for e in temp1: # cetak game yang dimiliki
            for i in range(countRow(arraygame)):
                if e == arraygame[i][0]: # game id yang dimiliki user sama dengan game id di data
                    print(arraygame[i][0] + " | " + arraygame[i][1] + " | " +
                        arraygame[i][2] + " | " + arraygame[i][3] + " | " + arraygame[i][4])
    else: # user tidak punya game
        print("Maaf, kamu belum memiliki game. Ketik perintah buy_game untuk beli.")
