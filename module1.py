from random import *
#Создаём функции.

def passautomat():  
    #Пароль создаётся машиной.  
    str0=".,:;!_*-+()/#¤%&"
    str1="0123456789"
    str2="qwertyuiopasdfghjklzxcvbnm"
    str3=str2.upper() # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4=str0+str1+str2+str3
    ls=list(str4) # список, все символы выше будут в списке.
    shuffle(ls) #перемешивает значения
    # Извлекаем из списка 12 произвольных значений
    psword="".join([choice(ls) for x in range(12)])
    # Пароль готов
    return psword

def paskontrool(psword: str)->bool:
    ls=list(psword)
    for e in ls:
        if e.isdigit():    d=True
        if e.isalpha():    a=True
        if e.isupper():    u=True
        if e.islower():    l=True
        if e in list(".,:;!_*-+()/#¤%&"):   s=True
    if d==True and a==True and u==True and  l==True and s==True:
        otv=True
    else:
        otv=False
    return otv
def koik_k(users,passwords):
    i=0
    for user in users:
        print(user, end="-")
        print(passwords[i])
        i+=1
def passwords