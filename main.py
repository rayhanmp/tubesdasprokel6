# Program BNMO
# ...

# Kamus
# isLoggedIn, isAdmin : boolean
# func : string
# user, game, riwayat, kepemilikan : list of (list of string)

# Algoritma Program
# Import modul yang diperlukan
from riwayat import riwayat_beli
from help import printHelp
from load import loadData, isFolderExist, printWelcome
from others import kerangajaib, tictactoe
from save import saveAllData
from exit import exitApp
from login import loginApp, cekAdmin
from register import registerUser
from changegame import ubahGame
from addgame import addGame
from search_my_game import cari_game
from search_game_at_store import cari_game_5
from topup import TopUp
from riwayat import riwayat_beli
from primitives import isPermitted

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
            registerUser(user)

    # LOGIN
    elif func == "login":
        isLoggedIn, userId = loginApp(user)
        if isLoggedIn == True:
            if cekAdmin(user, userId):
                isAdmin = True

    # TAMBAH GAME
    elif func == "tambah_game":
        # Validasi untuk Permission (harus login dan harus admin)
        if isPermitted(isLoggedIn, isAdmin, "login/admin"):
            addGame(game)    

    # UBAH GAME  
    elif func == "ubah_game":
        # Validasi untuk Permission (harus login dan harus admin)
        if isPermitted(isLoggedIn, isAdmin, "login/admin"):
            ubahGame(game)
    
    elif func == "ubah_stok":
        ...
    elif func == "list_game_toko":
        ...
    elif func == "buy_game":
        ...
    elif func == "list_game":
        ...

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