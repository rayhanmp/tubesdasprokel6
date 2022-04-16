import time

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


def tictactoe():
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

    board = [["#" for i in range(3)] for i in range(3)]
    turn = 1
    gameEnded = False

    while not gameEnded:
        printBoard(board)

        if turn % 2 == 0:
            player = "O"
        else:
            player = "X"

        while True:
            print(f"\nGiliran Pemain {player}")
            Y = int(input("Baris: "))
            X = int(input("Kolom: "))

            if not 1 <= X <= 3 or not 1 <= Y <= 3:
                print("\nKotak tidak valid.")
                continue
            if board[Y-1][X-1] != "#":
                print("\nKotak sudah terisi. Silakan pilih kotak lain.")
                continue
            else:
                board[Y-1][X-1] = player
                turn += 1
                break

        gameEnded = isGameEnded(board)

def isGameEnded(board):
    for i in range(3):

        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "#":
            printBoard(board)
            print(f"\n{board[i][0]} menang secara horizontal")
            return True

        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "#":
            printBoard(board)
            print(f"\n{board[0][i]} menang secara vertikal")
            return True

        if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
            if board[1][1] != "#":
                printBoard(board)
                print(f"\n{board[1][1]} menang secara diagonal")
                return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == "#":
                return False
            if i == j == 2:
                printBoard(board)
                print(f"\nPermainan berakhir Seri")
                return True

    return False 

def printBoard(board):
    print("\n=========== STATUS PAPAN ===========")
    for i in range(3):
            print(board[i][0] + board[i][1] + board[i][2])