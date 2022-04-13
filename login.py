from load import loadData, CSVtoList, countColumn, countRow


def loginApp(user):

    username = input("Masukan username: ")
    password = input("Masukan password: ")

    n_row = countRow(user)
    i = 0
    valid = False

    for i in range(n_row):
            if user[i][1] == username and user[i][3] == password:
                print("Halo", str(user[i][2])+"!", "Selamat datang di","Binomo")
                valid = True

    if valid == False:
        print("Password atau username salah atau tidak ditemukan.")
    
    return valid
            
            
