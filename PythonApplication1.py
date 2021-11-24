from module1 import *

users=["Timur"]
passwords=["1234"]

while True:
    print("Näita kõike-0, Sign up-1, Sign in-2, Sign out-3")
    v=int(input())
    if v==0:
        koik_k(users, passwords)
    if v==1:
        print("Sing up")
        while 1:
            log=input("Kasutajatunnus")
            if log not in users:
                print("Tunnus soobib")
                break
            else:
                print("See nimi juba on olemas listis")
        v=input("Arvuti-A või ise-I loob parool")
        if v.upper()=="A":
            pas=passautomat()

    if v==2:
        print("Sing in")
        while 1:
            log=input("Login:")
            if log in users:
                print("Te peate olema registreerima.")
            if passwords.index(pas)==users.index(user):
                print("Tere tulemast")
    if v==3:
        print("Sing out")
        break

password=passautomat()
print(password)