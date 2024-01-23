num1 = 23
num2 = 42

del num1 #Удаляет переменную
del num2, num3 #Удаляет обе переменные за один раз

a = int(5)
b = long(1010)
c = float(32)
d = complex(3,14)

text = 'Hello, world'
print(text[0])#Выводит первый символ
print(text[0:5]) #Выводит подстроку text т 0 до 5 символа
print(text[4:10]) #Выводит строку от 4-ого до 5-ого символа
print(text[0:14]) #Выводит всю строку
print(text[7:]) #Выводит строку с 7-ого символа
print(text[:5]) #С нулевого до 5-ого символа
print(text[:]) #Выводит всю строку
print([-1]) #Последний символ
#print([-1:-14]) НЕ СРАБОТАЕТ

my_list = [True, 786, 3.14, 'text', 70.2]
second_list = [123, 'text']
print(my_list)
print(my_list[0])
print(my_list[1:2])
print(my_list[3:5])
print(second_list * 2)
print(my_list + second_list)