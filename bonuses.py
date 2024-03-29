# Import modul yang diperlukan
import time

# Realisasi Fungsi dan Prosedur

# KERANG AJAIB
def kerangajaib():
    # Menjawab semua pertanyaan hidup (secara random)
    # I.S : Sebuah pertanyaan
    # F.S : Sebuah jawaban (Iya, Tidak, Mungkin, atau Bisa jadi)

    # Kamus Lokal
    # a, b, m, x : int
    # start_time : float
    # pertanyaan : string

    # Algoritma
    # Input pertanyaan (Tidak berpengaruh)
    pertanyaan = input("Apa pertanyaanmu? ")
    start_time = time.time()  # Waktu program memulai

    # Konstanta yang digunakan untuk Linear congruential generator
    a = 9   # Penentuan konstanta memiliki syarat : b dan m saling prima, a-1 habis dibagi semua faktor prima m,
    b = 3   # dan jika m habis dibagi 4, a-1 harus habis dibagi 4
    # m adalah periode pengacakan (m = 4, berarti ada 4 kemungkinan angka)
    m = 4

    # Nilai angka random
    x = 0
    while (start_time + 1) > time.time():  # Selama 1 detik belum terlewati
        # Rumus LCG yang akan menghasilkan x = 0, 1, 2, 3 secara periodik
        # Nilai x akan random tergantung performa komputer dalam 1 detik
        x = (x*a + b) % m

    # Output berdasarkan angka yang sudah di randomized
    if x == 0:
        print("Iya")
    elif x == 1:
        print("Mungkin")
    elif x == 2:
        print("Bisa jadi")
    elif x == 3:
        print("Tidak")


# TIC TAC TOE
def tictactoe():
    # Bermain permainan favorit Doni : tic tac toe
    # I.S : Permainan dimulai
    # F.S : Permainan berakhir dengan kemenangan atau seri

    # Kamus Lokal
    # board : list of (list of string)
    # turn, X, Y : integer
    # gameEnded : boolean

    # Algoritma
    # Interface Awal Permainan
    print("""
  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \.
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___|

Legenda:
# Kosong
X Pemain 1
O Pemain 2""")

    # Inisialisasi
    board = [["#" for i in range(3)] for i in range(3)] # Papan kosong
    turn = 1 # Turn
    gameEnded = False # boolean untuk menentukan kondisi game

    while not gameEnded: # Selama permainan belum berakhir
        # Tunjukkan status papan
        printBoard(board)

        # Tentukan giliran pemain
        if turn % 2 == 0:
            player = "O"
        else:
            player = "X"

        while True: # Validasi input sampai benar
            print(f"\nGiliran Pemain {player}")

            # Input posisi x dan y
            Y = int(input("Baris: "))
            X = int(input("Kolom: "))

            # Validasi
            if not 1 <= X <= 3 or not 1 <= Y <= 3: # Input diluar range
                print("\nKotak tidak valid.")
                continue
            if board[Y-1][X-1] != "#": # Input di kotak yang terisi
                print("\nKotak sudah terisi. Silakan pilih kotak lain.")
                continue
            else: # Input benar
                board[Y-1][X-1] = player
                turn += 1 # Tambah turn
                break # Keluar dari loop
        # Check status game, apakah sudah berakhir atau belum
        gameEnded = isGameEnded(board) # Jika true, permainan berakhir

def isGameEnded(board):
    # Mengecek apakah permainan tic-tac-toe sudah berakhir
    # I.S : Sebuah papan -> list of (list of string)
    # F.S : Boolean yang menyatakan apakah permainan sudah berakhir

    # Kamus Lokal
    # board : list of (list of string)
    # i, j : integer

    # Algoritma
    for i in range(3):
        # Cek untuk setiap baris, apakah ada 3 X/O beruntun 
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "#":
            printBoard(board)
            print(f"\n{board[i][0]} menang secara horizontal")
            return True

        # Cek untuk setiap kolom, apakah ada 3 X/O beruntun 
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "#":
            printBoard(board)
            print(f"\n{board[0][i]} menang secara vertikal")
            return True

        # Cek untuk setiap diagonal, apakah ada 3 X/O beruntun
        if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
            if board[1][1] != "#":
                printBoard(board)
                print(f"\n{board[1][1]} menang secara diagonal")
                return True

    # Cek jika semua petak sudah terisi
    for i in range(3):
        for j in range(3):
            if board[i][j] == "#": # Jika ditemukan petak kosong, maka game belum berakhir
                return False
            # Jika sampai iterasi terakhir ([i][j] == [2][2]) tidak ada "#"
            # Maka permainan berakhir seri (kondisi menang sudah dicek diatas) 
            if i == j == 2: 
                printBoard(board)
                print(f"\nPermainan berakhir Seri")
                return True

    return False 

def printBoard(board):
    # Mencetak papan ke layar
    # I.S : Sebuah papan -> list of (list of string)
    # F.S : Papan sudah tercetak di layar

    # Kamus Lokal
    # board : list of (list of string)
    # i : integer

    # Algoritma
    print("\n=========== STATUS PAPAN ===========")
    for i in range(3): # Print setiap baris 
            print(board[i][0] + board[i][1] + board[i][2])

# CIPHER
def legalcharacters():    
    # Membuat list dari karakter-karakter yang legal untuk password
    # I.S : -
    # F.S : List of string dari legal characters

    # Kamus Lokal
    # characters : list of string
    # idx : integer

    # Algoritma
    # Inisialisasi
    characters = ["" for i in range(64)]
    idx = 0

    # Pengisian list dengan cara
    for i in range(48, 58):
        characters[idx] = chr(i)
        idx += 1
    for i in range(65, 91):
        characters[idx] = chr(i)
        idx += 1
    for i in range(97, 123):
        characters[idx] = chr(i)
        idx += 1
    characters[62], characters[63] = chr(95), chr(45)

    # Return
    return characters

# Simpan karakter-karakter legal ke list characters
characters = legalcharacters()

def char_id(x):
    # Mencari index suatu elemen pada list characters
    # I.S : elemen x dan list character
    # F.S : index suatu elemen pada list characters

    # Kamus Lokal
    # characters : list of string
    # id : integer

    # Algoritma
    # Inisialisasi
    id = 0

    for char in characters:
        if x == char: #Jika ketemu return id
            return id
        #Else
        id += 1

def encrypt(password):
    # Mengenkripsi password dengan affice cipher
    # I.S : string password 
    # F.S : password yang sudah terenkripsi

    # Kamus Lokal
    # const a, b, m : integer
    # x : integer
    # e : float
    # encrypted_pass : string

    # Algoritma
    # Inisialisasi affine cipher constant
    a = 5
    b = 9
    m = 64
    # Inisialisasi encrypted pass
    encrypted_pass = ""
    for char in password:
        # Pengisian encrypted pass dengan metode affine chiper
        x = char_id(char)
        e = (a*(x) + b) % m
        encrypted_pass += characters[int(e)]

    return encrypted_pass

def decrypt(encrypted_pass):
    # Mendekripsi password dengan affice cipher
    # I.S : string password yang terenkripsi
    # F.S : password yang sebenarnya

    # Kamus Lokal
    # const a, b, m : integer
    # x : integer
    # d : float
    # password : string

    # Algoritma
    # Inisialisasi affine cipher constant
    a_inv = 13 # modular multipiclative inverse dari a
    b = 9
    m = 64

    # Inisialisasi password
    password = ""
    for char in encrypted_pass:
        # Pengisian decrypted pass dengan metode affine chiper
        x = char_id(char)
        d = (a_inv*(x-b)) % m
        password += characters[int(d)]
    
    return password