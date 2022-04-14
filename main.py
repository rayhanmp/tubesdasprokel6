# Program BNMO
# ...

# Kamus
# isLoggedIn, isAdmin : boolean
# func : string
# user, game, riwayat, kepemilikan : list of (list of string)

# Algoritma Program
# Import modul yang diperlukan
from help import printHelp
from load import loadData, isFolderExist, printWelcome
from save import saveAllData
from exit import exitApp
from login import loginApp, cekAdmin
from register import registerUser
from changegame import ubahGame
from addgame import addGame

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
    func = input("") # Input perintah dari pengguna
    if func == "register":
        registerUser(user)
    elif func == "login":
        isLoggedIn, index = loginApp(user)
        if isLoggedIn == True:
            if cekAdmin(user, index):
                isAdmin = True

    elif func == "tambah_game":
        addGame(game)
    elif func == "ubah_game":
        ubahGame(game)
    elif func == "ubah_stok":
        ...
    elif func == "list_game_toko":
        ...
    elif func == "buy_game":
        ...
    elif func == "list_game":
        ...
    elif func == "search_my_game":
        ...
    elif func == "search_game_at_store":
        ...
    elif func == "topup":
        ...
    elif func == "riwayat":
        ...
    elif func == "help":
        printHelp(isLoggedIn, isAdmin)
    elif func == "save":
        user = registerUser(user)
        saveAllData(user, game, riwayat, kepemilikan)
    elif func == "exit":
        exitApp(user, game, riwayat, kepemilikan)        
    else: # Perintah tidak tersedia
        print(f"Maaf. Perintah {func} tidak dikenali. Coba ketikkan \"help\" untuk " 
        "melihat daftar perintah yang dapat digunakan")