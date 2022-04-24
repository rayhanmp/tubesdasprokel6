# Program BNMO

# DESKRIPSI PROGRAM
# Program BNMO adalah sebuah platform yang dibuat untuk mengorganisasi koleksi video game. 

# BATASAN
# Pengguna dapat membuat akun untuk kemudian melihat-lihat game di toko.
# Pengguna dapat membeli game dari toko tersebut dengan topup saldo mereka.
# Pengguna harus melakukan save agar data game yang dibeli tersimpan ke dalam library secara permanen.
# Admin memiliki keleluasaan untuk menambah, mengubah, ataupun mengurangi game di toko.

# CATATAN : Gunakan folder encrypt_data untuk menjalankan program dan lihat init_data untuk password yang benar

# Kamus
# isLoggedIn, isAdmin : boolean
# func : string
# userId : integer
# user, game, riwayat, kepemilikan : list of (list of string)

# Algoritma Program
# Import modul yang diperlukan
from primitives import isPermitted
from load import loadData, isFolderExist, printWelcome
from register import registerUser
from login import loginApp, cekAdmin
from addgame import addGame
from changegame import ubahGame
from buy_game import buy_game
from ubah_stok import ubah_stok
from store_game import list_game_toko
from buy_game import buy_game
from user_game import list_game
from search_my_game import cari_game
from search_store import cari_game_5
from riwayat import riwayat_beli
from topup import TopUp
from riwayat import riwayat_beli
from help import printHelp
from save import saveAllData
from exit import exitApp
from bonuses import kerangajaib, tictactoe

# Loading data
if isFolderExist(): # Jika folder ada, maka load data dari folder tersebut
    user = loadData("user.csv")
    game = loadData("game.csv")
    riwayat = loadData("riwayat.csv")
    kepemilikan = loadData("kepemilikan.csv")

    printWelcome() # Prosedur untuk antarmuka
else: # Jika folder tidak ada, langsung exit aplikasi
    exit() 

# Inisiasi status user
isLoggedIn = False
isAdmin = False

# Masuk ke program 
while True:
    func = input("\n") # Input perintah dari pengguna

    # REGISTER
    if func == "register":
        if isPermitted(isLoggedIn, isAdmin, "login/admin"): # Validasi untuk Permission
            user = registerUser(user)

    # LOGIN
    elif func == "login":
        if isLoggedIn == False:
            isLoggedIn, userId = loginApp(user)
            if isLoggedIn == True:
                if cekAdmin(user, userId):
                    isAdmin = True
        else:
            print("Anda sudah login.")

    # TAMBAH GAME
    elif func == "tambah_game":
        # Validasi untuk Permission (harus login dan harus admin)
        if isPermitted(isLoggedIn, isAdmin, "login/admin"):
            game = addGame(game)    

    # UBAH GAME  
    elif func == "ubah_game":
        # Validasi untuk Permission (harus login dan harus admin)
        if isPermitted(isLoggedIn, isAdmin, "login/admin"):
            ubahGame(game)
    
    # UBAH STOK
    elif func == "ubah_stok":
        # Validasi untuk Permission (harus login dan harus admin)
        if isPermitted(isLoggedIn, isAdmin, "login/admin"):
            game = ubah_stok(game)

    # LIST GAME DI TOKO
    elif func == "list_game_toko":
        # Validasi untuk Permission (harus login dan bisa user/admin)
        if isPermitted(isLoggedIn, isAdmin, "login/both"):
            list_game_toko(game)

    # BELI GAME
    elif func == "buy_game":
        # Validasi untuk Permission (harus login dan harus user)
        if isPermitted(isLoggedIn, isAdmin, "login/user"):
            kepemilikan, user, riwayat = buy_game(userId, game, user, kepemilikan, riwayat)

    # LIST GAME YANG DIMILIKI
    elif func == "list_game":
        # Validasi untuk Permission (harus login dan harus user)
        if isPermitted(isLoggedIn, isAdmin, "login/user"):
            list_game(kepemilikan, game, userId)
        
    # CARI GAME YANG DIMILIKI
    elif func == "search_my_game":
        # Validasi untuk Permission (harus login dan harus user)
        if isPermitted(isLoggedIn, isAdmin, "login/user"):
            cari_game(game, kepemilikan, userId)

    # CARI GAME DI TOKO
    elif func == "search_game_at_store":
        # Validasi untuk Permission (harus login dan bisa user/admin)
        if isPermitted(isLoggedIn, isAdmin, "login/both"):
            cari_game_5(game)

    # TOPUP
    elif func == "topup":
        # Validasi untuk Permission (harus login dan harus admin)
        if isPermitted(isLoggedIn, isAdmin, "login/admin"):
            user = TopUp(user)

    # RIWAYAT PEMBELIAN
    elif func == "riwayat":
        # Validasi untuk Permission (harus login dan harus user)
        if isPermitted(isLoggedIn, isAdmin, "login/user"):   
            riwayat_beli(riwayat, userId)

    # HELP
    elif func == "help":
        # Tidak perlu validasi
        printHelp(isLoggedIn, isAdmin)

    # SAVE
    elif func == "save":
        # Tidak perlu validasi
        saveAllData(user, game, riwayat, kepemilikan)

    # EXIT
    elif func == "exit":
        # Tidak perlu validasi
        exitApp(user, game, riwayat, kepemilikan)        

    # KERANG AJAIB
    elif func == "kerangajaib":
        # Tidak perlu validasi
        kerangajaib()

    # TIC TAC TOE
    elif func == "tictactoe":
        # Tidak perlu validasi
        tictactoe()

    else: # Perintah tidak tersedia
        print(f"Maaf. Perintah {func} tidak dikenali. Coba ketikkan \"help\" untuk " 
        "melihat daftar perintah yang dapat digunakan")
