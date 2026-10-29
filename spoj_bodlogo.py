# Гурвалжин

# a = list(map(int, input().split()))
# print(sum(a))


# 2 тооны нийлбэр

# a = list(map(int, input().split()))
# print(sum(a))


# Куб

# a = int(input())
# b = a*a*a
# c = b+a*a
# print(b,c)


# Тэгш өнцөгт

# a,b = map(int, input().split())
# x = a * b
# y = x - b
# print(x, y)

# Функц 1

# x = int(input())
# y = 3 * x - 5
# print(y)

# Функц 2

# x = int(input())
# y = 4*x**2 - 3 * x + 5
# print(y)

# Сүүлийн цифр

# a = int(input())
# b = a % 100
# c = b % 10
# print(c)

# Аравтын орны цифр

# a = int(input())
# b = a % 100
# c = b // 10
# print(c)

#2 оронтой тоо

# a = int(input())
# b = a % 100
# c = b % 10
# d = b // 10
# e = c * d
# print(e)

# 3 оронтой тоо

# a = int(input())
# b = a % 100
# c = b % 10
# d = b // 10
# x = d // 10
# i = d + c + x
# print(i)


# n = int(input())

# num = 0

# while n > 0:
#     digit = n % 10
#     num += digit
#     n = n // 10

# print(num)

# Минут секунд

# a = int(input("sec: "))
# b = a // 60
# c = a % 60
# print(b, c)

# Цаг минут секунд

# a = int(input("sec: "))
# b = a // 3600
# c = b // 3600
# d = a % 3600
# print(b, c, d)

# Минут секунд -> секунд

# a, b = map(int,input().split())
# x = a * 60
# y = x + b
# print(y)

# хоног цаг

# a = int(input("tsag: "))
# b = a // 24
# c = a % 24
# print(b, c)

#Хоног цаг -> цаг

# a, b = map(int, input().split())
# c = a * 24
# d = c + b
# print(d)

# Жил сар

# a = int(input())
# b = a // 12
# c = a % 12
# print(b, c)

# Жил сар -> сар

# a, b = map(int, input().split())
# c = a * 12
# d = c + b
# print(d) 

# Хоёр тооны их

# a, b = map(int, input().split())
# c = a, b
# print(max(c))

# Хоёр тооны бага

# a, b = map(int, input().split())
# c = a, b
# print(min(c))

# 3 тооны их

# a, b, c = map(int, input().split())
# d = a, b, c
# print(max(d))

# 4 тооны бага

# a = [3, 2, 1, 4]
# print(min(a))

# Нийлбэр 80

# a = []
# b = list(map(int, input().split()))
# for i in b:
#     if i > 80:
#         a.append(i)
#         print(sum(a))



# Үржвэр 5

# a = list(map(int, input().split()))
# b = 1 
# for i in a :
#     if i < 5 :
#        b = i*b
# print(b)


# Тэгш тооонуудийн нийлбэр

# a = list(map(int, input().split()))
# b = 0
# for i in a :
#     if i % 2 == 0 :
#        b = i+b
# print(b)

# Сондгой тоонуудийн үржвэр

# a = list(map(int, input().split()))
# b = 1 
# for i in a :
#     if i % 2  != 0:
#        b = i*b
# print(b)

# Тэнцүү 5

# a = list(map(int, input().split()))
# print(a.count(5))



# text = "banana"
# print(text.count("a"))
 
# text = "bAnAnA"
# print(text.upper())

# text = "bAnAnA"
# print(text.replace("A", "a"))

# text = "bAnAnA, python"
# print(text.replace("python", "jims"))

# 3-д хуваагдах

# a = list(map(int, input().split()))
# b = 0
# for i in a:
#     if i % 3 == 0:
#         b += 1
# print(b)

# 11-д хуваагддаггүй

# a = list(map(int, input().split()))
# b = 0
# for i in a:
#     if i % 11 != 0:
#         b = i + b
# print(b)

# 10-аас их


# a = int(input("too: "))
# if a > 10:
#     print("yes")
# else:
#     print("no")

# 5-аас бага

# a = int(input("too: "))
# if a < 5:
#     print("yes")
# else:
#     print("no")

# Тэгш тоонууд YES

# a = list(map(int,input("too: ").split()))
# b = 0
# for i in a :
#     if i % 2 == 0:
#         b += i
#     print("yes")
# else:
#     print("no")

# IOI

# print("IOI")

# IOI 3 удаа

# for i in range(3):
#     print("IOI")

# IOI n удаа

# a = int(input())
# for i in range(a):
#     print("IOI")

# Эхний n тооны нийлбэр

# total = 0
# a = int(input("too: "))
# for i in range(1, a + 1 ):  
#     total += i
# print(total)

# n!

# n = int(input())
# a = 1
# while n > 0:
#     a = a * n
#     n = n - 1
# print(a)

# 100-г n удаа нэм

# n = int(input())
# a = 0
# i = 0
# while i < n:
#     a += 100
#     i += 1
# print(a)

# a тоог n удаа нэм

# a, n = map(int, input("too: ").split())
# sum = 0
# i = 0
# while i < n:
#     sum = sum + a
#     i = i + 1
# print(sum)

# 2-ын n зэрэг

# n= int(input("too: "))
# a = n ** 2
# print(a)

# a тооны n зэрэг

# a = int(input("too: "))
# o = 0
# while o < a:
#     b = int(input())
#     i = a ** b
#     o += i
# print(o)

#  Тэнцсэн, унасан

# n = int(input("too: "))
# if n > 3:
#     print("tentssen")
# else:
#     print("tentseegvi")    

# 5-аас онц руу

# n = int(input("too: "))
# if n == 5:
#     print("onts")
# elif n == 4:
#     print("sain")
# elif n == 3:
#     print("dund")
# else:
#     print("muu")

# Тоон үнэлгээнээс үсгэнд

# n = int(input("too: "))
# if n > 89:
#     print("A")
# elif n > 79:
#     print("B")
# elif n > 69:
#     print("C")
# elif n > 59:
#     print("D")
# else:
#     print("F")

# Гараг

# n = int(input("garag: "))
# if 1 <= n <= 7:
#     if n == 1:
#         print("Monday")
#     elif n == 2:
#         print("Tuesday")
#     elif n == 3:
#         print("Wednesday")
#     elif n == 4:
#         print("Thursday")
#     elif n == 5:
#         print("Friday")
#     elif n == 6:
#         print("Saturday")
#     else:
#         print("Sunday")

# Улирал

# n = int(input())
# if 1 <= n <= 12:
#     if 2 <= n <= 4:
#         print("Spring")
#     elif 5 <= n <= 7:
#         print("Summer")
#     elif 8 <= n <= 10:
#         print("Autumn")
#     else:
#         print("winter")

# Гурвалжин эсэх

