def counter(item):
    count = 0
    for i in item:
        count += 1
    return count

def registerUser():
    uname = input("Masukan username: ")

    count = 0
    i = 0
    while i < counter(uname):
        if (ord(uname[i])>=48 and ord(uname[i])<=57) or (ord(uname[i])>=65 and ord(uname[i])<=90) or (ord(uname[i])>=97 and ord(uname[i])<=122) or (ord(uname[i])==95) or (ord(uname[i])==45):
            count += 1
            i += 1
        else:
            i += 1

    if count == counter(uname):
        print("Valid dong kk")
    else:
        print("Mntapphhh salah looooo")

registerUser()