# Modul Exit
# Modul untuk keluar dari aplikasi

# Import modul yang diperlukan
from save import saveAllData

# Fungsi dan Prosedur
def exitApp(user, game, riwayat, kepemilikan):
    # Keluar aplikasi dengan/dengan tidak menyimpan data
    # I.S : data yang akan/tidak akan di save
    # F.S : aplikasi keluar dengan/dengan tidak menyimpan data

    # Kamus Lokal 
    # option : string

    # Algoritma
    while True: # Meminta input sampai valid
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        option = input("")

        if option in "Yy": # Jika input Y/y, simpan data
            saveAllData(user, game, riwayat, kepemilikan)
            break
        elif option in "Nn": # Jika input N/n, langsung keluar tanpa simpan data
            break
        else: # Input tidak valid
            continue

    exit() # Keluar aplikasi

