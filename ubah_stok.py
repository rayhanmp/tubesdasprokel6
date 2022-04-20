from primitives import countRow

def ubah_stok(arraygame):
    # Mengubah stok game di toko
    # I.S : list data game (arraygame)
    # F.S : list data game baru yang sudah di tambah stoknya

    # Kamus Lokal
    # IDgame, game : string
    # i, baris, jumlah_stok, jumlah_awal, jumlah_baru : integer
    # found : boolean

    # Algoritma    
    IDgame =  (input("Masukkan ID game: ")) # field ID wajib diisi

    # Cari game dengan IDGame di array game
    found = False    
    for i in range (countRow(arraygame)):
        if arraygame[i][0] == IDgame:
            baris = i # ambil baris yang memiliki id game yang sesuai
            IDgame = IDgame
            found = True
            break # telah menemukan id game pada data

    if found: # kalau id game yang dimasukin ga ada    
      jumlah_stok = int(input("Masukkan jumlah: ")) # stok tambahan atau kurangan
      jumlah_awal = int(arraygame[baris][5]) # stok awal
      game = arraygame[baris][1] # game terpilih 

      # stok setelah penambahan atau pengurangan 
      jumlah_baru = jumlah_awal + jumlah_stok
      if jumlah_stok < 0: # stok dikurangi
        if jumlah_baru < 0: # gagal jika stok akhir menjadi negatif
          print (f"Stok game {game} gagal dikurangi karena stok kurang. Stok sekarang: {jumlah_awal} (< {jumlah_stok})")
          return arraygame
        else: # berhasil
          arraygame[baris][5] = jumlah_baru
          print (f"Stok game {game} berhasil dikurangi. Stok sekarang: {jumlah_baru}")
          return arraygame
      else: # stok ditambah
          arraygame[baris][5] = jumlah_baru
          print (f"Stok game {game} berhasil ditambah. Stok sekarang: {jumlah_baru}") # tampilinnya berhasil ditambah
          return arraygame
    else:
      print ("Tidak ada game dengan ID tersebut")
      return arraygame
    
    # di akhir selalu return arraygame, baik ada perubahan maupun tidak