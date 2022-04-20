from primitives import countRow

def list_game_toko(arraygame):
    # Listing game di Toko Berdasarkan ID, Tahun Rilis dan Harga
    # I.S : list data game
    # F.S : list game yang tersedia tercetak berdasarkan skema sorting yang dipilih

    # Kamus Lokal
    # skema, temp : string
    # i, j : integer

    # Algoritma    
    skema = input("Skema sorting : ") # Input skema

    if skema == "tahun+": # Skema tahun ascending
        # Sorting dengan Bubble Sort
        for i in range(1, countRow(arraygame)):
            for j in range(i+1, countRow(arraygame)):
                if (arraygame[i][3] > arraygame[j][3]):
                    temp = arraygame[i]
                    arraygame[i] = arraygame[j]
                    arraygame[j] = temp

    elif skema == "tahun-": # Skema tahun descending
        # Sorting dengan Bubble Sort
        for i in range(1, countRow(arraygame)):
            for j in range(i+1, countRow(arraygame)):
                if (arraygame[i][3] < arraygame[j][3]):
                    temp = arraygame[i]
                    arraygame[i] = arraygame[j]
                    arraygame[j] = temp

    elif skema == "harga+": # Skema harga ascending
        # Sorting dengan Bubble Sort
        for i in range(1, countRow(arraygame)):
            for j in range(i+1, countRow(arraygame)):
                if (arraygame[i][4] > arraygame[j][4]):
                    temp = arraygame[i]
                    arraygame[i] = arraygame[j]
                    arraygame[j] = temp

    elif skema == "harga-": # Skema harga descending
        # Sorting dengan Bubble Sort
        for i in range(1, countRow(arraygame)):
            for j in range(i+1, countRow(arraygame)):
                if (arraygame[i][4] < arraygame[j][4]):
                    temp = arraygame[i]
                    arraygame[i] = arraygame[j]
                    arraygame[j] = temp

    elif skema == "": # Skema id ascending
        arraygame = arraygame # tidak perlu ubah apa-apa, id ascending by default

    else: # Skema tidak valid
        print("Skema sorting tidak valid!")
        return # Langsung return tanpa pencetakan list
    
    print("\nDaftar game:")
    for i in range(1, countRow(arraygame)): # Cetak list game dari array yang sudah di sort
        print(str(i) + ". " + arraygame[i][0] + " | " + arraygame[i][1] + " | " + arraygame[i][4] +
              " | " + arraygame[i][2] + " | " + arraygame[i][3] + " | " + arraygame[i][5])
