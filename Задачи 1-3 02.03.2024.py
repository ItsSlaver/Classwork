#Задача 1
def schet ():
    a = input ("Введите первое число: ")
    a = float (a)
    b = input ("Введите второе число: ")
    b = float (b)
    u = input ("Введите третье число: ")
    u = float (u)
    if a > b:
        print(a-b)
    elif a > u:
        print(a-u)
    else:
        print(b-a-u)
    return a, b, u
c, d, i = schet()
#Задача 2
def schet ():
    a = input ("Введите первое число: ")
    a = float (a)
    b = input ("Введите второе число: ")
    b = float (b)
    if a > b:
        print(a-b)
    else:
        print(b-a)
    return a, b
c, d = schet()
def schet1 ():
    a = input ("Введите первое число: ")
    a = float (a)
    b = input ("Введите второе число: ")
    b = float (b)
    if a > b:
        print(a+b)
    else:
        print(b/a)
    return a, b
c, d = schet1()
#Задача 3
def Quastion ():
    a = "Душ"
    print("То холодный - то горячий, то висячий - то стоячий.")
    b = str(input("Введите ответ: "))
    if b == a:
        print("Верно: То холодный - то горячий, то висячий - то стоячий. - ", b)
    else:
        print("Неверно: перезагрузите программу и порпобуйте заново")
    return a, b
c, d = Quastion()
def Quastion1 ():
    x = "Велосипед"
    print("Беру двумя руками, сую между ногами.")
    z = str(input("Введите ответ: "))
    if z == x:
        print("Верно: Беру двумя руками, сую между ногами. - ", z)
    else:
        print("Неверно: перезагрузите программу и порпобуйте заново")
    return x, z
c, d = Quastion1()
def Quastion2 ():
    v = "Прутья веника"
    print("Мы - ребята удалые, лазим в щели половые!")
    m = str(input("Введите ответ: "))
    if v == m:
        print("Верно: Мы - ребята удалые, лазим в щели половые! - ", v)
    else:
        print("Неверно: перезагрузите программу и порпобуйте заново")
    return v, m
c, d = Quastion2()