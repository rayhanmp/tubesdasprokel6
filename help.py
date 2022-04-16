# Modul Help
# Modul untuk menunjukkan list fungsi yang dapat diakses oleh user atau admin

# KAMUS
# preLoginHelp, adminHelp, userHelp : string

# ALGORITMA
# String yang berisi list fungsi yang dapat diakses sebelum login
preLoginHelp = """1. login - Melakukan login ke dalam aplikasi
2. help - Memunculkan list fungsi yang dapat diakses
3. kerangajaib - Menjawab semua pertanyaanmu
4. tictactoe - Minum coklat panas, bermain tictactoe"""

# String yang berisi list fungsi yang dapat diakses oleh admin 
adminHelp = """1. register - Melakukan registrasi user baru
2. login - Melakukan login ke dalam aplikasi
3. tambah_game - Menambah game yang dijual pada toko
4. ubah_game - Mengubah game yang dijual di toko
5. ubah_stok - Mengubah jumlah stok game yang dijual pada toko
6. list_game_toko - Memunculkan list game yang dijual di toko 
7. search_game_at_store - Mencari game yang dijual di toko
8. topup - Menambahkan saldo kepada user
9. help - Memunculkan list fungsi yang dapat diakses
10. save - Menyimpan perubahan data di aplikasi
11. exit - Keluar dari aplikasi
12. kerangajaib - Menjawab semua pertanyaanmu
13. tictactoe - Minum coklat panas, bermain tictactoe"""

# String yang berisi list fungsi yang dapat diakses oleh user
userHelp = """1. login - Untuk melakukan login ke dalam sistem
2. list_game_toko - Memunculkan list game yang dijual di toko 
3. buy_game - Membeli game dari toko
4. list_game - Memunculkan list game yang dimiliki
5. search_my_game - Mencari game yang dimiliki
6. search_game_at_store - Mencari game yang dijual di toko
7. riwayat - Melihat riwayat pembelian
8. help - Memunculkan list fungsi yang dapat diakses
9. save - Menyimpan perubahan data di aplikasi
10. exit - Keluar dari aplikasi
11. kerangajaib - Menjawab semua pertanyaanmu
12. tictactoe - Minum coklat panas, bermain tictactoe"""

# Fungsi dan Prosedur
def printHelp(isLoggedIn, isAdmin):
    # Mencetak list fungsi yang dapat diakses oleh user atau admin
    # I.S : status login dan role user
    # F.S : fungsi-fungsi yang dapat diakses sesuai status tercetak

    # Kamus Lokal
    # isLoggedIn, isAdmin : boolean (status user)
    
    # Algoritma
    print("=========== PERINTAH UNTUK BNMO ===========")

    if not isLoggedIn: # user belum login
        print(preLoginHelp)
    else:
        if isAdmin: #Jika admin, tampilkan list fungsi admin
            print(adminHelp)
        else: #Jika user, tampilkan list fungsi user
            print(userHelp)