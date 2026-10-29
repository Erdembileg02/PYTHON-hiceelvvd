# ============================================================
# HICHEEL 1 — PYTHON ХИЧЭЭЛИЙН ТЭМДЭГЛЭЛ
#
# СЭДВҮҮД
# 01. Хувьсагч, оролт/гаралт, арифметик үйлдэл
# 02. Нөхцөлт оператор (if / elif / else)
# 03. Давталт (for)
# 04. Давталт (while)
# 05. Жагсаалт (list)
# 06. Тэмдэгт мөр (string)
# 07. Tuple
# 08. Set ба Dictionary
# 09. Жагсаалт болон алгоритмын бодлогууд
# 10. Хоёр хэмжээст жагсаалт
# 11. Функц
#
# Жишээ кодуудыг ажиллуулах шаардлагатай бол тухайн хэсгийн
# мөрүүдийн эхний # тэмдгийг арилгана.
# ============================================================

# ------------------------------------------------------------
# 01. Хувьсагч, оролт/гаралт, арифметик үйлдэл
# ------------------------------------------------------------


# #task 1
# a = 27
# s = a // 10
# d = a % 10
# print(s + d)

# #task 2
# a = 135
# s = a // 60
# d = a % 60
# print(s,d)

# #task 3
# a = 125
# s = a // 60
# d = a % 60
# print(s,d)

# #task 4
# a = 12345
# d = a % 10
# print(d)

# #task 5
# a = 57
# s = a // 10
# print(s)

# #task 6
# a =27
# s = a // 10
# d = a % 10
# print(d * 10 + s)

# #task 7
# a = 34
# s = a // 3
# d = a % 3
# print(s + d)

# #task 8
# a = 20
# b = 5
# c = a // b
# print(c)

# #task 9
# a = 20
# b = a // 6
# c = b % 2
# print(b,c)

# # orolt = 5
# # b = (orolt * 25)
# # c = (orolt * 30)
# # print(b, c)

# # a, b = map( int, input("2_too_oruul: ").split())
# # x = a * b
# # y = (a + b)*2
# # print(x, y)

# a= int("too oruul: 1 ")
# b= int(input("hoyr dahi too: "))
# x= int(a-b)
# print(x)

# a=int(input("sec oruul: "))
# tsag = a // 3600
# second = a % 60
# minute = a % 3600 // 60
# print(tsag,"tsag", minute,"minute", second,"second")

# a = int(input("tsag: ")),int(input("minute: ")),int(input("sec: "))
# total_sec = a[0] * 3600 + a[1] * 60 + a[2]
# print("total sec:", total_sec)

# a=map(int(input("tsag: ").split("minute: ")))
# x = int("tsag" * 60)
# y = int("minute" * 60)
# w = (x* y)
# print(w)

# a = map(int, input("tsag minute: ").split())
# tsag, minute = a
# w = tsag * 60 + minute
# print(w)

# a = 2,3,4
# b = 2 * 3 * 4
# print(b)

# a = 583
# x = (a // 10) % 10
# print(x)

# a = 527
# x =5 + 7
# print(x)

# a = 736
# x = 7, 3, 6
# print(x)

# a = 2026
# x = 2 + 0 + 2 + 6
# print(x)

# n = 3700
# x = 3 * 1000 + 1 * 500 + 2 * 100
# print(x)

# a, b = (15), (27)
# x = (b, a)
# print(x)

# a = 357
# x = a // 100
# y = a % 100
# print(x, y)

# a = int(input("udur, tsag, minute: "))
# udur = a // 1440
# tsag = a // 1440
# minute = a % 60
# print(udur, tsag, minute)

# a = int(input("myngat, zuut, aravt, negj: "))
# myngat = a // 1000
# zuut = a // 100 % 10
# aravt = a % 10 // 2
# negj = a
# print(myngat, zuut, aravt, negj)


#task 1
# print("Bat")

#task 2
# a = 15, 23
# x = 15 + 23
# print(x)

#task 3
# a = 8, 5
# x = 8 * 5
# print(x)

#task 4
# a = 7
# x = 7 * 2
# print(x)

#task 5
# nas = 15
# x = (nas + 1)
# print(x)

#task 6
# a = 20
# x = a * 9 / 5 + 32
# print(x)

#task 7
# a = 47
# x = (4 + 7)
# print(x)

#task 8


#task 9
# a = int(input("minute: "))
# tsag = a // 60
# minute = a % 60
# print(tsag, minute)

#task 10
# a = int(input("sec: "))
# minute = a // 60
# sec = a % 60
# print(minute, sec)


#task 1

# name = input("ner: ")
# print("sain uu", name)

#task 2

# a = 12
# b = 7
# f = a + b
# print(f)

#task 3

# a = float(input())
# b = float(input())
# c = a + b
# print(c)

#task 4

# a = int(input("too: "))
# b = str(a)
# c = int(a)
# print(f"{type(b)}\n{type(c)}")

#task 5

# a = "sain uu"
# print(len(a))

#task 6

# a = input()
# print(a[0])
# print(a[-1])

#task 1


# ------------------------------------------------------------
# 02. Нөхцөлт оператор (if / elif / else)
# ------------------------------------------------------------


# a = 10
# b = int(input("too: "))
# if a == b:
#     print("tentsvv")
# else:
#     print("bish")

# udur = input()
# if udur =="6" or udur =="7":
#     print("amraltiin udur")
# else:
#     print("ajliin udur")

# unah_dvn = 60
# deed_dvn = 100
# dvn = int(input())
# if unah_dvn <= dvn and deed_dvn >= dvn:
#     print("tentssen")
# else:
#     print("tentseegvi")


# score = int(input())
# if score < 0 or score > 100:
#     print("invalid score")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# age = int(input("nas: "))
# if age >= 18:
# 	ticket = input("ticket bgyu? ")
# 	if ticket == "baigaa":
# 		print("orj bolnoo")
# 	else:
# 		print("ticket hergtei")
# else:
# 	print("Tom bolood ireerei")

# username = input("username: ")
# if username == "Erdembileg" or "erdembileg":
#     password = input("password: ")
#     if password == "0206":
#         print("logged in")
#     else:
#         print("password incorrect")
# else:
#     print("password incorrect")

#task 11
# too = int(input("too oruul: "))
# if too >= -1:
#         if too >= 1:
#             print("positive")
#         else:
#             print("zero")
# else:
#      print("negative")

#task 12
# too =18
# if too == 18:
#     print("even")
# else:
#     print("odd") 

#task 13
# nas = int(input("nasaa bic: "))
# if nas >= 18:
#     print("adult")
# else:
#     print("child")

#task 14
# too_1 = int(input("ehnii too: "))
# too_2 = int(input("2dh too: "))
# if too_1 >= too_2:
#     if too_2 >= too_1:
#         print(too_2)
#     else:
#         print(too_1)    
#     print(too_1)
# else:
#     print(too_2)

#task 15
# a = 10
# b = 20
# c = 30
# if a <= b <= c:
#     print("yes")
# else:
#     print("no")

#task 16
# onoo = int(input("Onoo: "))
# if onoo < 0 or onoo > 100:
#     print("aldaa!")
# elif onoo >= 90:
#     print("A")
# elif onoo >= 80:
#     print("B")
# elif onoo >= 70:
#     print("C")
# elif onoo >= 60:
#     print("D")
# else:
#     print("F")

#task 17
# a = int(input("too oruul: "))
# if a % 3 == 0:
#     print("yes")
# else:
#     print("no")

#task 18
# a = 14
# b = 8
# c = 25
# if a >= b <= c:
#     print(b)
# else:
#     print("error")

#task 19
# a = int(input("Too: "))
# if 0<= a <= 50:
#     print("yes")
# else:
#     print("no")

# task 20
# nas = int(input("NAS: "))
# if nas >= 12:
#     tasalbar = input("Tasalbar bgyu: ")
#     if tasalbar == "baigaa":
#         print("Enter")
#     else:
#         print("No")

#     print("Enter")
# else:
#     print("No")

#task 21
# onoo = int(input("Onoo: "))
# irts = int(input("Irts: "))
# if onoo >= 60:
#     if irts >= 80:
#         print("pass")
#     else:
#         print("fail")
#     print("pass")
# else:
#     print("fail")

#task 22
# a = input("nuuts vg: ")
# b = input("batalgaajuulah nuuts vg: ")
# if a == "python123":
#     if b == "python123":
#         print("correct")
#     else:
#         print("wrong")
#     print("correct")
# else:
#     print("wrong")

#task 23
# a, b, c = map(int, input().split())
# if (a > b and a < c) or (a < b and a > c):
#     print(a)
# elif(b > c and b < a) or (b < c and b > a):
#     print(b)
# else:
#     print(c)

#task 24
# a, b = map(int, input().split())
# 0 <= a <=100
# 0 <= b <=100
# if a >= 90 and b >= 90:
#     print("Excellent")
# elif a >= 70 and b >= 80:
#     print("good")
# else:
#     print("Need improvement")

#task 25
# day = int(input("1-7 udur: "))
# week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# if 1 <= day <= 7:
#     print(week[day - 1])
#     if day >= 6:
#         print("weekend")
#     else:
#         print("workday")
# else:
#     print("aldaa!")

#task 26
# a = int(input("Too oruul: "))
# if 100 < a and a % 2 == 0:
#     print("Large even")
# elif  100 < a :
#     print("Large")
# elif a <= 0 :
#     print("Negative")
# elif  0 < a <100:
#     print("Medium")

#task 27
# vne, nas = map(int,input("baraanii vne?: ").split())
# if vne and nas <= 18 :
#     print( vne,"20% хөнгөлөлт")
# elif vne and nas >= 60:
#     print(vne, "30% хөнгөлөлт")
# else:
#     print(vne,"баярлалаа")

#task 28
# a, b, c = map(int, input().split())
# if a + b > c and a + c > b and b + c > a:
#     print("yes")
# else:
#     print("no")

#task 29
# nas = int(input("nas: "))
# password = int(input("pass: "))
# if nas > 18 :
#     print("Done")
# else:
#     print("Denied")
# if password == 1234:
#     print("Done")
# else:
#     print("Wrong password")
# admin = input("admin erh bgyu?: ")
# if admin =="baigaa":
#     print("Admin access")
# else:
#     print("User access")


#task 30
# a, b = map(int, input("ATM: ").split())
# c = a - b
# if b <= 0 or b % 1000:
#     print("Invilid amount")

# elif b > a:
#     print("Insufficient balance")
# else:
#     print("Remaining:")
#     print(c)



#task 1
# y = int(input("жил: "))
# if (y % 4 == 0 and y % 100 > 0) or y % 400 == 0:
#     print("yes")
# else:
#     print("no")

#task 2
# a, b, c = map(int, input().split())
# if a == b ==c:
#     print("Equilateral")
# elif a == b or b == c or a == c:
#     print("Isosceles")
# else:
#     print("Scales")

#task 3
# n = int(input("nas: "))
# d = input("day: ")
# if n <12 or n > 60:
#     print("5000")
# elif d == "weekend":
#     print("12000")
# else:
#     print("10000")

#task 4
# name = input("username: ")
# password = input("password: ")
# if name == "admin":
#     if password == "1234":
#         print("welcome")
#     else: 
#         print("loginn failded")
# else:
#     print("account blocked")

#task 5
# x1, y1, x2, y2 = map(int, input().split())
# x, y = map(int, input().split())
# if x1 <= x <= x2 and y1 <= y <= y2:
#     print("INSIDE")
# else:
#     print("OUTSIDE")

#task 6
# a1, b1, a2, b2 = map(int, input().split())
# if a1 <= b2 and a2 <= b1:
#     print("YES")
# else:
#     print("NO")

#task 7
# day = int(input("day: "))
# month = int(input("month: "))
# year = int(input("year: "))
# if month < 1 or month > 12 or day <= 31:
#     if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#         if 1 <=month <= 31:
#             print("VALID")
#     else:
#             print("INVALID")
# if 1<= month <=28:
#      if month == 4 or month == 6 or month == 9 or month == 11:
#           print("VALID")
# else:
#      print("INVALID")
# if month == 2:
#      if year % 4 == 0:
#         print("VALID")
# else:
#         print("INVALID")

#task 8
# r, c = map(int, input().split())
# if r < 1 or r > 8 or c < 1 or c > 8:
#     print("INVALID")
# elif (r + c) % 2 ==0:
#     print("black")
# else:
#     print("white")

#task 9
# dvn, irts, zurcil = map(int, input().split())
# if dvn >= 90 and irts >= 95 and zurcil == 0:
#     print("Full")
# elif dvn >= 80 and irts >= 90 and zurcil <= 1:
#     print("Half")
# else:
#     print("None")

#task 10
# player_1, player_2 = map(int, input().split())
# if player_1 == player_2:
# 	print("Draw")
# elif (player_1, player_2) in ((1, 2), (2, 1), (3, 2)):
# 	print("Player 1")
# else:
# 	print("Player 2")
    
#task 1
# a, b, c = map(int, input().split())

# if a <= b and b <= c:
#     print(a, b, c)

# elif a <= c and c <= b:
#     print(a, c, b)

# elif b <= a and a <= c:
#     print(b, a, c)

# elif b <= c and c <= a:
#     print(b, c, a)

# elif c <= a and a <= b:
#     print(c, a, b)

# else:
#     print(c, b, a)


# ------------------------------------------------------------
# 03. Давталт (for)
# ------------------------------------------------------------


# a = "sain uu"
# for i in range(5):
#     print(a)

# for i in range(10):
#     print(i)

# for i in range(1,11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# ner = "Erdembileg"
# for i in range(5):
#     print(ner)

# total = 0
# for i in range(11):
#     total += i
# print(total)

# a = 0
# for i in range(101):
#     a+=i
# print(a)

# a = 0
# for i in range(0,21,2):
#     a += i
# print(a)

# a = 0
# for i in range(1,31):
#     if i % 3 == 0:
#         a += i
# print(a)

#task 10
# a = 5
# for i in range(1,a):
#     a += i
# print(a)

#task 11
# a = 0
# for i in range(1,21):
#     if i % 2 == 0:
#         a = a + 1
# print(a)

#task 12
# a = 0
# for i in range(1, 101):
#     if i % 5 == 0:
#         a = a + 1
# print(a)

#task 13
# a = 0
# for i in range(1,51):
#     if i % 3 == 0:
#         a = a + 1
# print(a)

#task 14

# a = 0
# b = 0
# for i in range(1,21):
#     if i % 2 == 0:
#         a += 1
#         b+= 1
# print(a,b)


# #task 15

# a = 0
# for i in range(1,50):
#        if a % 2 == 0:
#         a += 7
# print(a)

#task 16

# a = 0
# b = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         a += i
#         b += 1
# print(a)
# print(b)

#task 17

# a = 0
# for i in range(1, 101):
#     if i % 3 == 0 or  i % 5 == 0 :
#         a += 1
# print(a)

#task 18

# a = 0
# for i in range(1, 100):
#     if i % 3 == 0:
#         a += i
# print(a)

#task 19
# n = int(input("surgciin too: "))

# niilber = 0
# deesh = 0

# for i in range(n):
#     dvn = int(input("dvn: "))
#     niilber += dvn
#     if dvn > 80:
#         deesh += 1

# dundaj = niilber / n
# print("dvngiin niilber: ", niilber)
# print("dundaj: ", dundaj)
# print("80+ dvn: ", dvn)

#task 20

# n = int(input("heden dvn: "))
# high = 0
# for i in range(n):
#     onoo = int(input("dvn: "))
#     if onoo > high:
#         high = onoo
# print("hamgiin undur dvn: ", high)

#task 1

# for i in range(10, 51, 3):
#     print(i)

# task 2
# n = 15
# for i in range(1,n):
#     if i % 2 == 0:
#         n += i
#         print(i)

#task 3

# a = 0
# for i in range(1,51,2):
#         a += i
# print(a)

#task 4

# a = 0
# for i in range(1,101):
#     if i % 4 == 0:
#         a += 1
# print(a)

#task 5

# a = 0
# for i in range(10):
#     b = int(input())
#     if b > 0:
#         a += b
# print(a)

#task 6

# a = 0
# for i in range(10, 101):
#     if i % 5 == 0:
#         a += i
# print(a)

#task 7

# n = 12345
# b = 0
# for i in str(n):
#     b += int(i)
# print(b)

#task 8

# a = 0
# for i in range(1, 101):
#     if i % 7 == 0 and a < 5:
#      a += 1
#      print(i)

#task 9

# a = 0
# for i in range(1, 50):
#     if i % 2 == 0 and (i +2)>= 50:
#         print(i)

#task 10
# a = 0
# for i in range(10):
#     b = int(input())
#     if b > 0:
#         if a == 0 or b < a:
#             a = b
# print(a)



# ------------------------------------------------------------
# 04. Давталт (while)
# ------------------------------------------------------------


#task 1

# a = 1
# while a <= 10:
#     print(a)
#     a += 1

#task 2

# a = 11
# while 1 != a:
#     a -= 1
#     print(a)
    
#task 3

# a = 0
# i = 1
# while i <= 100:
#     a += i
#     i += 1
# print(a)

#task 4

# a = 1
# while a < 1000:
#     print(a)
#     a *= 2

#task 5

# i = 1             # i aa 5 boltln hevlej bna. Ghde 5 hze c bolohgvi. True
# while i <= 5:
#     print(i)

# i = 10            # i= 10n 5 baga bish tull shuud ajillahgui zogsoj bna. False
# while i <= 5:
#     print(i)
#     i+=1

# i = 1             # i = 1 dooshoo buyu hasah bolood dooshoo hyzgaargvi yvj bna
# while i <= 5:
#     i -= 1
#     print(i)

# import random
# secret = 6
# oroldlogo = 0
# print("1-100 too taagaarai: ")
# while True:
#     taasan = int(input("taah too: "))
#     oroldlogo += 1
#     if taasan < secret:
#         print("ihdee")
#     elif taasan > secret:
#         print("bagadaa")
#     else:
#         print("zuv taasan!!!")
#         print("niit oroldlogo: ", oroldlogo)
#         break



#####################################################################################


# a = 0
# n = int(input("too ug: "))
# while a <= n:
#    a += 1
#    print(a)


####################################################################################


# n = 11
# while n > 1:
#     n -= 1
#     print(n)


####################################################################################


# n = int(input("too: "))
# a =0
# while a <= n:
#     print(a)
#     a += 2    
    

#######################################3


# n = int(input("too ug: "))
# a = 1
# while a < n:
#     print(a)
#     a +=2


##########################################


# n = int(input("too ug: "))
# i = 1
# a = 0
# while i <= n:
#     a += i
#     i += 1
# print(a)

#######################################


# n = int(input("too ug: "))
# i = 2
# a = 0
# while i <= n:
#     a += i
#     i += 2
# print(a)


############################################


# n = int(input("too ug: "))
# a = 3
# while a < n:
#     print(a)
#     a += 3


############################################

# n = int(input(" heden too ug: "))
# i = 0
# eyreg = 0
# surug = 0
# teg = 0
# while i < n:
#     too = int(input("too: "))
#     if too > 0:
#         eyreg += 1
#     elif too < 0:
#         surug += 1
#     else:
#         teg += 1
#     i += 1
# print("eyreg: ", eyreg)
# print("surug: ", surug)
# print("teg: ", teg)


#########################################

# n = int(input("heden too uguh ve?: "))
# i = 1
# a = 0
# while i <= n:
#     too = int(input("too ug: "))
#     if too > 0:
#         a += too
#         i += 1
# print(a)


############################################

# n = int(input("heden too oruulah ve: "))
# i = 1
# ih_too = 0
# while i <= n:
#     too = int(input("too oruul: "))
#     if too > ih_too:
#         ih_too = too
#         i += 1    
# print("hamgiin ih too: ",ih_too)



###############################################


# i = 1
# while i < 10:
#     print(i)
#     i += 1
#     if i ==3:
#         break


###############################################


# n = int(input("heden too oruulah ve: "))
# i = 1
# f = int(input("too oruul: "))
# while i < n:
#     too = int(input("too oruul: "))
#     if too < f:
#         f = too
#     i += 1
# print(f)


##################################################


# n = int(input("heden uguh ve: "))
# i = 1
# while i <= n:
#     if i % 3 == 0 and i % 5 == 0:
#           print(i)
#     i += 1


#     
######################################################


# n = int(input("too oruul: "))
# i = 0
# while n > 0:
#     n //= 10
#     i += 1
# print(i)


######################################################


# n = int(input("too oruul: "))
# niilber = 0
# while n > 0:
#     b = n % 10
#     niilber += b
#     n //= 10
# print(niilber)


######################################################


# n = int(input("too oruul: "))
# a = 0
# while n > 0:
#     b = n % 10
#     a = a * 10 + b
#     n = n // 10
# print(a)


######################################################


# n = int(input("too: "))
# original = n
# a = 0
# while n > 0:
#     b = n % 10
#     a = a * 10 + b
#     n = n // 10
# if original == a:
#     print("palindrom")
# else:
#     print("not palindrom")


######################################################


# n = int(input())
# i = 1
# count = 0
# while i <=n:
#     if n % i == 0:
#         count += 1
#     i += 1
# if count == 2:
#     print("anhnii too")
# else:
#     print("anhnii too bish")


######################################################


# n = int(input())
# i = 1
# a = 2
# while a <= n:
#     i = 1
#     count = 0
#     while i <= a:
#         if a % i == 0:
#             count += 1
#         i += 1
#     if count == 2:
#         print(a)
#     a += 1


######################################################


# n = int(input())
# i = 1
# while i <= 10:
#     print(n, "*", i, "=", n * i)
#     i += 1


######################################################


# password = input("pass oruul: ")
# while password != "python123":
#     print("wrong password")
#     password = input("try again: ")
# print("correct")


######################################################


# for i in range(0, 10):
#     i += 1
#     print(i)


######################################################


# for i in range(1, 20):
#     if i % 2 == 0:
#         print(i)


######################################################


# for i in range(0, 20):
#     if i % 2 == 0 :
#         i += 1
#         print(i)


######################################################


# n = int(input("too ug: "))
# i = 1
# while i <= 10:
#     print(n, "*", i, "=",n * i)
#     i += 1


######################################################



# n = int(input("too ug: "))
# for i in range(0, n):
#     i += 1
#     print(i)


######################################################


# n = int(input("too ug: "))
# for i in range(n, 0, -1):
#     print(i)


######################################################


# for i in range(1, 50):
#         if i % 3 == 0:
#             print(i)


######################################################


# for i in range(1, 31):
#     if i % 5 != 0:
#         print(i) 


######################################################


# total = 0
# i = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         total += 1
# print(total)


######################################################


# total = 0
# for i in range(1, 100):
#     if i % 7 == 0:
#         total += 1
# print(total)


######################################################


# total = 0
# for i in range(1, 100):
#     i += 1
#     total += i
# print(total)


######################################################


# total = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         total += i
# print(total)


######################################################

# davhar, orts, haalga = map(int, input().split())
# toot = int(input())

# neg_orts = davhar * haalga

# orts_dugaar = (toot - 1) // neg_orts + 1

# orts_dotorh_toot = (toot - 1) % neg_orts + 1

# davhar_dugaar = (orts_dotorh_toot - 1) // haalga + 1

# haalga_dugaar = (orts_dotorh_toot - 1) % haalga + 1

# print(orts_dugaar, davhar_dugaar, haalga_dugaar)


# ######################################################


# secret = 17
# ih = 0
# baga = 0
# surug = 0
# n = int(input("too: "))
# if n > secret:
#     print("ih")
# elif n < secret:
#     print("baga")
# elif n == secret:
#     print("zuv taalaa!")
# else:
#     print("sondgoi too")


######################################################


# for weekday in range(5):
#     print(f"weekday", end=" ")
#     for hour in range(3):
#         print(f"hour", end=" ")
#     print()


######################################################


# angi_too = int(input("нийт хэдэн анги вэ?"))
# for angi in range(1, angi_too + 1):
#     print("\n", angi, "-р анги")
# suragch_too = int(input("Хэдэн сурагчтай вэ? "))
# niit_onoo = 0
# tentsen = 0

# hamgiin_ih_onoo = -1
# hamgiin_ih_ner = ""

# for suragch in range(1, suragch_too + 1):

#     print("\n", suragch, "-р сурагч")

#     ner = input("Нэр: ")

#     while True:
#         onoo = int(input("Оноо: "))

#         if onoo >= 0 and onoo <= 100:
#             break


#         print("Оноо 0-100 хооронд байна.")

#     niit_onoo = niit_onoo + onoo

#     if onoo >= 60:
#         tentsen = tentsen + 1

#     if onoo > hamgiin_ih_onoo:
#         hamgiin_ih_onoo = onoo
#         hamgiin_ih_ner = ner

# dundaj = niit_onoo / suragch_too

# print("\n---", angi, "-р ангийн тайлан ---")
# print("Дундаж оноо:", dundaj)
# print("Тэнцсэн сурагч:", tentsen)
# print("Тэнцээгүй сурагч:", suragch_too - tentsen)
# print("Хамгийн өндөр оноо:", hamgiin_ih_onoo)
# print("Шилдэг сурагч:", hamgiin_ih_ner)


######################################################


# for hour in range(24):
#     for minute in range(60):
#         print(hour, ":", minute)



######################################################


# n = int(input("сурагч: "))
# m = int(input("шалгалт: "))
# print( end=" ")
# if  0 < m  < 100:
#     if m >= 60:
#         print("тэнцсэн")
#     else:
#         print("тэнцээгүй")


######################################################


# ------------------------------------------------------------
# 05. Жагсаалт (list)
# ------------------------------------------------------------


# min = baga
# max = ih
# sum()/len() = dunsaj
# sum = bvh toonii niilber
# len = tsiipriin shirheg
# a.remove() = songoson tsipriig ustgana
# a.pop = indexeern ustgana 
# a.sort = bagaas ihrvv daraalluulna
# a.sort(reverse = true) = esergeern
# a.append = tsiper nemne

# a =(1, 2, 3, 4)
# print(sum(a))


######################################################


# a = [6,4,3,5,1,2]
# a.sort(reverse = True)
# print(a)


######################################################

# lab 1

# score = [72, 95, 61]
# score.append(88)
# score.insert(1,80)
# score.remove(61)
# score.sort(reverse=True)
# print(score)


######################################################

# lab 2

# playlist = ["tansag", "nvd", "perfect"]
# playlist.append("ulaan")
# playlist.remove("nvd")
# playlist.sort()
# print(playlist)
# a =input("duu oruul: ")


# jims = ["apple", "banana", "mango"]
# if "mango" in jims:
#     print("bna")
# else:
#     print("bhgu")


# jims = ["apple", "banana", "mango"]
# for i in range(len(jims)):
#     print(jims)


# ------------------------------------------------------------
# 06. Тэмдэгт мөр (string)
# ------------------------------------------------------------


# 8(3)

#task 1

# n = input().split()
# print(len(n))

#task 2

# n = list(input().split())
# a = n[0]
# for i in n:
#     if len(i) > len(a):
#         a = i
# print(a)

#task 3

# n = input()
# a = 0
# for i in n:
#     if i in"аэиоуөү":
#         a += 1
# print(a)

#task 4

# n = input().split()
# a = input()
# print(n.count(a))

#task 5

# n = input().split()
# n.sort()
# print(n)

#task 6

# n = input().split()
# for i in n:
#     if i == i[::-1]:
#         print(i)


# ------------------------------------------------------------
# 07. Tuple
# ------------------------------------------------------------


#task 1

# colors = ("ulaan", "nogoon", "tsenher")
# print(colors)

#task 2

# a = ("nohoi", "muur", "tuulai", "mori")
# print(f"{a[0]}\n{a[2]}\n{a[3]}\n")

#task 3

# a = (100,)
# print(type(a))

#task 4

# subject = ("matematic", "mongol hel", "angli hel", "python")
# print(subject[0], subject[2], subject[3])


#task 5

# number = (10, 20, 30, 40, 50)
# print(number[0:3])

#task 6

# number = (10, 20, 30, 40, 50)
# print(number[2:5])

#task 7

# fruits = ("alim", "banana", "jvrj", "usan vzem")
# print(len(fruits))

#task 8

# numbers = (45, 12, 89, 23, 7)
# print("hamgiin ih", max(numbers))
# print("hamgiin baga", min(numbers))

#task 9

# scores = (80, 90, 70, 100)
# print("niilber", sum(scores))
# print("dundaj", sum(scores)// len(scores))

#task 10


# numbers = (50, 10, 40, 20, 30)
# b = sorted(numbers)
# print(b)

#task 11

# a = (10, 20, 10, 30, 10, 40)
# print(a.count(10))

#task 12

# fruits = ("алим", "банана", "жүрж", "усан үзэм")
# print(fruits.index("жүрж"))

#task 13

# animals = ("nohoi", "muur", "tuulai")
# a = input("amitan: ")
# if a in animals:
#     print("bna")
# else:
#     print("alga")

#task 14

# student = ("Ану", 12, "7А")
# name, age, student_class = student
# print(f"{"ner:",name}\n{"nas:",age}\n{"angi:",student_class}")

#task 15

# coordinate = (15, 25)
# x, y = coordinate
# print(f"x={x}\ny={y}")

#task 16

# book = ("Python сурах", "Бат", 250)
# title, author, pages = book
# print(f"nom: {title}\nzohiolch: {author}\nhuudas: {pages}")

#task 17

# a = 5
# b = 10
# a, b = b, a
# print(f"a= {a}\nb= {b}")

#task 18

# numbers = (10, 20, 30, 40, 50)
# a, *b = numbers
# print(f"ahnii utga= {a}\nvldsen utga= {b}")

#task 19

# numbers = (1, 2, 3, 4, 5, 6)
# first, *middle, last = numbers
# print(f"ehnii= {first}\ndundah= {middle}\nsvvliih= {last}")

#task 20

# student = ("Тэмүүлэн", "Математик", "Python", "Англи хэл")
# name, *subject = student
# print(f"suragc= {name}\nhiceelvvd= {subject}")

#task 21

# product = ("Дэвтэр", 3500, 4)
# name, price, quantity = product
# print(f"baraa = {name}\nnegj vne = {price}\ntoo shirheg = {quantity}\nniit vne: {price * quantity}")

#task 22

# students = (
#     ("Ану", 90),
#     ("Бат", 75),
#     ("Сараа", 100)
# )
# for name, score in students:
#     print(f"{name}:{score}")

#task 23

# students = (
#     ("Ану", 90),
#     ("Бат", 75),
#     ("Сараа", 100)
# )
# for name, score in students:
#     if score > 80:
#         print(f"{name}")

#task 24

# colors = ("улаан", "ногоон", "цэнхэр")
# a = list(colors)
# a.append("шар")
# b = tuple(a)
# print(b)


# ------------------------------------------------------------
# 08. Set ба Dictionary
# ------------------------------------------------------------


# Python Set ба Dictionary — Дасгалууд


# I. Set дасгалууд

# 1. Давхардлыг арилгах

# nums = [1, 2, 2, 3, 4, 4, 5]
# print(set(nums))

# 2. Жимс нэмэх

# fruits = {"apple", "banana"}
# fruits.add("orange")
# print(fruits)

# 3. Утга устгах

# fruits = {"apple", "banana", "orange"}
# fruits.remove("banana")
# print(fruits)

# 4. Байгаа эсэхийг шалгах

# nums = {10, 20, 30, 40}
# if 20 in nums:
#     print("Yes")
# else:
#     print("No")

# 5. Хэдэн ялгаатай тоо байна вэ?

# a = {1, 2, 2, 3, 3}
# set(a)
# print(len(a))

# 6. Давхардсан нэрс

# names = ["Bat", "Sara", "Bat", "Bold", "Sara", "Anu"]
# a = set(names)
# print(len(a))

# 7. Хоёр set-ийг нэгтгэх

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)

# 8. Ижил утгуудыг олох

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a & b)

# 9. Зөвхөн эхний set-д байгаа утгууд

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a - b)

# 10. Хоёр хичээл хоёуланг нь сурдаг сурагчид

# Python сурдаг сурагчид:

# python_students = {"Bat", "Sara", "Bold", "Anu"}

# # Java сурдаг сурагчид:

# java_сурдаг_сурагчид = {"Sara", "Bold", "Temuulen"}
# print(python_students & java_сурдаг_сурагчид)

# 11. Зөвхөн нэг хичээл сурдаг сурагчид

# Python сурдаг сурагчид:

# python_students = {"Bat", "Sara", "Bold", "Anu"}

# # # # Java сурдаг сурагчид:

# java_сурдаг_сурагчид = {"Sara", "Bold", "Temuulen"}
# print(python_students ^ java_сурдаг_сурагчид)

# 12. Оруулсан үсгүүд

# a = input("vg: ")
# b = set(a)
# print(len(b))


# II. Dictionary дасгалууд

# 13. Сурагчийн мэдээлэл

# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 95
# }
# print(student)

# 14. Нэрийг хэвлэх

# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 90
# }
# print(student["name"])

# 15. Оноог өөрчлөх

# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 85
# }
# student["score"]=98
# print(student)

# 16. Шинэ мэдээлэл нэмэх

# student = {
#     "name": "Anu",
#     "age": 18
# }
# student.update({"city": "Ulaanbaatar"})
# print(student)

# 17. Мэдээлэл устгах

# student = {
#     "name": "Bold",
#     "age": 20,
#     "score": 88
# }
# del student["age"]
# print(student)

# 18. Key-үүдийг хэвлэх

# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# for key in car:
#     print(key)

# 19. Value-уудыг хэвлэх

# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# print(car.values())

# 20. Key болон value-г хамтад нь хэвлэх

# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 95
# }
# for key,value in student.items():
#     print(key,value)

# 21. Key байгаа эсэх

# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 92
# }
# if "score" in student:
#     print("bna")
# else:
#     print("bhgu")

# 22. Барааны мэдээлэл

# product = {
#     "name": "Keyboard",
#     "price": 120000,
#     "stock": 5
# }
# if product ["stock"] >= 0:
#     print("Available")
# else:
#     print("Out of stock")

# 23. Сурагчдын оноо

# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }
# for name, score in scores.items():
#     if score >= 80:
#         print(name)

# 24. Хамгийн өндөр оноо

# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }
# best = max(scores, key = scores.get)
# scores = scores[best]
# print(f"{best}:{scores}")

# 25. Dictionary-ийн бүх value-ийн нийлбэр

# sales = {
#     "Monday": 10,
#     "Tuesday": 15,
#     "Wednesday": 20
# }
# a = sum(sales.values())
# print(a)

# 26. Үгийн давтамж

# a = input()
# counts ={}
# for word in a.split():
#     counts[word]=counts.get(word, 0)+1
# for word, n in counts.items():
#     print(word, n)


# III. Set + Dictionary хосолсон дасгалууд

# 27. Давхардалгүй хичээлүүд

# students = {
#     "Bat": ["Python", "Java"],
#     "Sara": ["Python", "C++"],
#     "Bold": ["Java", "Python"]
# }
# a = set()
# for i in students.values():
#     a.update(i)
# for course in a:
#     print(course)

# 28. Хэдэн өөр хот байна вэ?

# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Temuulen": "Darkhan"
# }
# a = set(students.values())
# print(len(a))

# 29. Нэг хотод амьдардаг сурагчид

# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet"
# }
# for name, city in students.items():
#     if city == "Ulaanbaatar":
#         print(name)

# 30. Давхардалгүй утгуудтай dictionary

# data = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30,
#     "e": 20
# }
# print(set(data.values()))




# Python Set + Dictionary — Дунд түвшний дасгалууд
# SET — Дунд түвшин

# 1. Нийтлэг найзууд

# user1 = {"Bat", "Sara", "Bold", "Anu"}
# user2 = {"Bold", "Anu", "Temuulen", "Naraa"}
# print(user1 & user2)

# 2. Шинэ тоглоом тоглоогүй хүмүүс

# # Нийт тоглогчид:
# players = {"Bat", "Sara", "Bold", "Anu", "Naraa", "Temuulen"}

# # Шинэ тоглоом тоглосон хүмүүс:
# played = {"Bat", "Bold", "Naraa"}
# print(players - played)

# 3. Хоёр багийн ялгаа

# team_a = {"Bat", "Bold", "Anu", "Sara"}
# team_b = {"Anu", "Sara", "Naraa", "Temuulen"}
# print(team_a - team_b | team_b - team_a)

# 4. Сургалтад бүртгүүлэх

# # Сурагчийн мэддэг хэлнүүд:
# known = {"Python", "HTML", "CSS"}

# # Сургалтын шаардлагатай хэлнүүд:
# required = {"Python", "JavaScript", "SQL"}
# print(required - known)

# 5. Давтагдсан хичээл

# subjects = [
#     "Python",
#     "Math",
#     "Python",
#     "English",
#     "Math",
#     "Physics"
# ]
# a = set(subjects)
# print(a)
# print(len(a))

# 6. Нууц үгийн үсгүүд

# password = input("Input: ")

# letters = 0
# digits = 0

# for c in password:
#     if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
#         letters += 1
#     elif '0' <= c <= '9':
#         digits += 1

# print("Letters:", letters)
# print("Digits:", digits)

# 7. Нийт орсон үсгүүд

# a = input("1: ")
# b = input("2: ")
# characters = set(a) | set(b)
# print(len(characters))

# DICTIONARY — Дунд түвшин

# 8. Шалгалтын дүн

# students = {
#     "Bat": 75,
#     "Sara": 92,
#     "Bold": 61,
#     "Anu": 88,
#     "Naraa": 54
# }

# for name, score in students.items():
#     if score > 90:
#         print(name, "-" "excellent")
#     elif score > 80:
#         print(name, "-" "pass")
#     else:
#         print(name, "-" "fail")

#task 9

# products = {
#     "apple": 3000,
#     "banana": 2500,
#     "milk": 4500,
#     "bread": 3500
# }
# name = input("Input:")
# count = int(input())
# total = products[name]*count
# print(total)

# task 10
# sales = {
#     "keyboard": 15,
#     "mouse": 23,
#     "monitor": 8,
#     "headset": 17
# }
# best = max(sales, key = sales.get)
# score = sales[best]
# print(f"{best} {score}")

# task 11
# employees = {
#     "Bat": 1500000,
#     "Sara": 1800000,
#     "Bold": 1300000,
#     "Anu": 2100000
# }
# for name, salary in employees.items():
#     if salary < 1500000:
#         employees[name] = int(salary * 1.1)
# print(employees)

# task 12
# people = {
#     "Bat": 17,
#     "Sara": 21,
#     "Bold": 19,
#     "Anu": 16,
#     "Naraa": 25
# }
# for name , age in people.items():
#     if age >= 18:
#         print(name)

# task 13
# scores = {
#     "Bat": 70,
#     "Sara": 85,
#     "Bold": 60,
#     "Anu": 95
# }
# for name , sco in scores.items():
#     if sco <100 :
#         sco +=5
#         print(name,sco)

# task 14
# products = {
#     "keyboard": 120000,
#     "mouse": 50000,
#     "monitor": 450000,
#     "headset": 80000
# }
# n = int(input())
# for name , une in products.items():
#     if une> 100000:
#         print(name)
        
# task 15
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Naraa": "Darkhan",
#     "Temuulen": "Ulaanbaatar"
# }
# n = input()
# se = set()
# for name , city in students.items():
#     if city == n:
#         se.add(name)
# print(se)

# task 16
#games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# players = set()
# for name , game in games.items():
#     if "CS2" in game:
#         players.add(name)
# print(players)

# task 17
# games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# game = set()
# for players in games.values():
#     game.update(players)
# print(game)

# task 18
# games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# players = []
# for name in games:
#     player_game = games[name]
#     if "CS2," and "WoW" in player_game:
#         players.append(name)
# print(players)

# task 19
# skills = {
#     "Bat": {"Python", "HTML", "CSS"},
#     "Sara": {"Python", "JavaScript"},
#     "Bold": {"HTML", "CSS", "JavaScript"},
#     "Anu": {"Python", "SQL", "JavaScript"}
# }
# student_skill = []
# for name ,student in skills.items():
#     if "Python" in student and "JavaScript" in student:
#         student_skill.append(name)
# print(student_skill)

# # task 20
# employees = {
#     "Bat": {"English", "Mongolian"},
#     "Sara": {"English", "Korean"},
#     "Bold": {"Mongolian", "Japanese"},
#     "Anu": {"English", "Japanese"}
# }
# empo = []
# for name , hell in employees.items():
#     if "English" in hell and "Korean" not in hell:
#         empo.append(name)
# print(empo)

#task 21
# web_users = {"Bat", "Sara", "Bold", "Anu"}
# mobile_users = {"Sara", "Anu", "Naraa"}
# print(len(web_users & mobile_users))

#task 22
# status = {
#     "Bat": "online",
#     "Sara": "offline",
#     "Bold": "online",
#     "Anu": "offline",
#     "Naraa": "online"
# }
# online = set()
# for name in status:
#     if status[name] == "online":
#         online.add(name)
# print(online)
# name = input()
# if name in online:
#     print("online")
# else:
#     print("offline")

#task 23
# courses = {
#     "Python": {"Bat", "Sara", "Bold"},
#     "JavaScript": {"Sara", "Anu", "Bold"},
#     "SQL": {"Bat", "Anu"}
# }
# n = input()
# for course, students in courses.items():
#     if n in students: 
#         print(course)

#task 24
# courses = {
#     "Python": {"Bat", "Sara", "Bold"},
#     "JavaScript": {"Sara", "Anu", "Bold"},
#     "SQL": {"Bat", "Anu"}
# }

# counts = {}
# for course, students in courses.items():
#     for s in students:
#         counts[s] = counts.get(s, 0) + 1

# max_count = max(counts.values())
# top = [s for s, c in counts.items() if c == max_count]
# print(top, max_count)




# ------------------------------------------------------------
# 09. Жагсаалт болон алгоритмын бодлогууд
# ------------------------------------------------------------

# nums = list(map(int, input().split()))

# nums.sort()

# print(nums[-2])


#task 2

# nums = list(map(int, input().split()))
# result = []

# for i in nums:
#     if i not in result:
#         result.append(i)

# print(result)

# text = input()

# reverse = ""

# for i in range(len(text)-1, -1, -1):
#     reverse += text[i]

# if text == reverse:
#     print("YES")
# else:
#     print("NO")

#task 4

# words = input().split()

# longest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print(longest)

#task 5

# text = input().lower()
# vowels = "аэиоуөү"
# count = 0

# for ch in text:
#     if ch  in vowels:
#         count += 1

# print(count)

#task 6

# n = int(input())
# total = 0

# for i in range(1, n + 1):
#         total += i

# print(total)

#task 7

# n = int(input())
# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit
#     n // 10

# print(total)

#task 8

# n = int(input())
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse + digit
#     n //= 10

# print(reverse)




# 1 Хоёр дахь хамгийн их тоо

# nums = [7, 3, 9, 9, 2, 5, 7, 8]

# nums.sort()
# a = set(nums)
# b = list(a)
# print(b[-2])

# 2 Хоёр дахь хамгийн бага тоо

# nums = [7, 3, 9, 9, 2, 5, 7, 8]

# nums = [7, 3, 9, 9, 2, 5, 7, 8]
# nums.sort()
# a = set(nums)
# b = list(a)
# print(b[1])


# 3 Хамгийн урт дараалсан сондгой хэсэг

# nums = [2, 1, 3, 5, 4, 7, 9, 11, 6]

# a = 0
# b = 0
# for n in nums:
#     if n % 2 == 1:
#         b += 1
#         a = max(a, b)
#     else:
#         b = 0
# print(a)



# 4 Хамгийн урт өсөх дараалал

# nums = [1, 2, 4, 2, 3, 5, 7, 1]
# a = 0
# b = 0
# for n in nums:
#     if n % 2 == 1:
#         b += 1
#         a = max(a, b)
#     else:
#         b = 0
# print(a)



#5 Хамгийн олон давтагдсан тоо
# nums= [1, 2, 4, 2, 3, 5, 7, 1]
# count ={}
# for n in nums:
#     count[n]= count.get(n, 0) + 1
# m = max(count.values())
# print(min(n for n, c in count.items()if c == m))


#6 Давтамжийн хамгийн бага

# nums= [1, 2, 4, 2, 3, 5, 7, 1]
# count ={}
# for n in nums:
#     count[n]= count.get(n, 0) + 1
# m = min(count.values())
# print(min(n for n, c in count.items()if c == m))


#7 Хоёр list-ийн нийтлэг элемент

# a = [1, 2, 3, 4, 5]
# b = [3, 5, 7, 8, 1]
# print(sorted(set(a)&set(b)))


#8 Нийлбэр нь хамгийн их хос

# nums =[4, 7, 2, 9, 5]
# s = sorted(nums, reverse=True)
# print(s[0], s[1])





# ------------------------------------------------------------
# 10. Хоёр хэмжээст жагсаалт (nested list)
# ------------------------------------------------------------


# m = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(0,len(m)):
#     for j in m[i]:
#         print(j, end="")
#     print()


# I. Index ашиглах — Амархан

# 1. 6 тоог хэвлэ

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# for i in nums:
#     print(i)


# 2. "Bold" нэрийг хэвлэ

# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]

# a = students[2][0]
# print(a)


# 3. 2 дахь мөрийг хэвлэ

# nums = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]

# a = nums[1]
# print(a)


# 4. 70 тоог хэвлэ

# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# a = nums[2][0]
# print(a)


# 5. Хамгийн эхний утгыг хэвлэ

# nums = [
#     [5, 10],
#     [15, 20]
# ]

# a = nums[0][0]
# print(a)


# 6. Хамгийн сүүлийн утгыг хэвлэ

# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# a = nums[2][1]
# print(a)


# II. Nested loop — Суурь


# 7. Бүх мөрийг хэвлэ

# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# for i in nums:
#     print(i)


# 8. Бүх тоог хэвлэ

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# for i in range(len(nums)):
#     for j in nums[i]:
#         print(j)


# 9. Бүх тоог нэг мөрөнд хэвлэ

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# for i in range(len(nums)):
#     for j in nums[i]:
#         print(j, end=" ")


# 10. 10-аас их тоонуудыг хэвлэ

# nums = [
#     [3, 12, 5],
#     [20, 7, 15]
# ]

# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j > 10:
#             print(j, end=" ")


# III. Count ба Sum — Дунд


# 11. Нийт хэдэн тоо байгааг ол

# nums = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         count+=1
# print(count)


# 12. Бүх тооны нийлбэрийг ол

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         count += j
# print(count)


# 13. Тэгш тоонуудыг хэвлэ

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j % 2 == 0:
#             print(j, end = " ")


# 14. Сондгой тоонуудын тоог ол

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j % 2 != 0:
#             print(j, end = " ")


# 15. Тэгш тоонуудын нийлбэрийг ол

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j % 2 == 0:
#             count += j
# print(count, end = " ")


# 16. Эерэг тоонуудын тоог ол

# nums = [
#     [-3, 5, 0],
#     [7, -2, 8],
#     [-1, 4, 0]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j > 0:
#             count += 1
# print(count)


# 17. Сөрөг тоонуудын нийлбэрийг ол

# nums = [
#     [-2, 3, -5],
#     [4, -1, 6]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j <0:
#             count += j
# print(count)


# IV. Min / Max — Дунд


# 18. Хамгийн их тоог ол

# nums = [
#     [4, 8, 2],
#     [10, 3, 7],
#     [1, 6, 5]
# ]

# a = nums[1]
# print(max(a))

# 19. Хамгийн бага тоог ол

# nums = [
#     [7, 2, 9],
#     [4, -3, 6],
#     [8, 1, 5]
# ]

# a = []
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         a.append(j)
#         b = min(a)
# print(b)


# 20. Мөр бүрийн нийлбэрийг ол

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# count = 0
# for i in nums:
#         count = sum(i)
#         print(count)


# 21. Мөр бүрийн хамгийн их тоог ол

# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]


# count = 0
# for i in nums:
#         count = max(i)
#         print(count)


# 22. Мөр бүрийн хамгийн бага тоог ол

# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]


# count = 0
# for i in nums:
#         count = min(i)
#         print(count)



# V. Хайлт ба нөхцөл — Дунд/Хэцүү


# 23. 7 тоо байгаа эсэхийг шалга

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# if 7 in sum(nums, []):
#     print("YES")
# else:
#     print("NO")

# 24. Өгөгдсөн тоо хэдэн удаа байгааг ол

# nums = [
#     [1, 2, 3],
#     [2, 4, 2],
#     [5, 2, 6]
# ]

# target = 2

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j == target:
#             count += 1
# print(count)


# 25. 5-аас их тоонуудын нийлбэрийг ол

# nums = [
#     [1, 7, 3],
#     [9, 2, 6],
#     [4, 8, 5]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if 5 < j:
#             count += j
# print(count)


# 26. Хамгийн их нийлбэртэй мөрийг ол

# nums = [
#     [1, 2, 3],
#     [10, 20, 30],
#     [4, 5, 6]
# ]

# a = []
# count = 0
# for i in nums:
#     count = sum(i)
#     a.append(count)
# print(nums[a.index(max(a))])


# VI. Сурагчийн өгөгдөл — Хэцүү


# 27. Сурагч бүрийн нэр ба насыг хэвлэ

# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]

# for student in students:
#     print(student[0], student[1])


# 28. 18-аас дээш настай сурагчдыг хэвлэ

# students = [
#     ["Bat", 17],
#     ["Sara", 19],
#     ["Bold", 20],
#     ["Anu", 16]
# ]

# for key, value in students:
#     if value > 18:
#         print(key, value)




# ------------------------------------------------------------
# 11. Функц
# ------------------------------------------------------------


#task 1

# def gurvaljin():
#     a, b, c = map(int, input("too: ").split())
#     return  a + b + c
# x = gurvaljin()
# print(x)


#task 2

# def niilber():
#     a, b = map(int, input("too: ").split())
#     return a + b
# x = niilber()
# print(x)


#task 3

# def tegsh():
#     a, b = map(int, input().split())
#     return a * b, (b + a) * 2
# x = tegsh()
# print(x)


#task 4

# def funkts():
#     a = int(input("too: "))
#     return 3 * a - 5
# x = funkts()
# print(x)


#task 5

# def kub():
#     a = int(input("too: "))
#     return a ** 3, 6 * a ** 2
# x = kub()
# print(x)


#task 6

# def funkts2():
#     a = int(input("too: "))
#     return (4 * a ** 2) - (3 * a) + 5
# x = funkts2()
# print(x)


#task 7

# def svvliih():
#     a = int(input("too: "))
#     return a % 100 % 10
# x = svvliih()
# print(x)


#task 8

# def dund():
#     a = int(input("too: "))
#     return a % 100 // 10
# x = dund()
# print(x)


#task 9

# def vrjver():
#     a = int(input("too: "))
#     return (a % 10) * (a // 10)
# x = vrjver()
# print(x)


#task 10

# def nem():
#     a = int(input("too: "))
#     return (a // 100) + (a % 100 // 10) + (a % 100 % 10)
# x = nem()
# print(x)



#task 1

# def hello():
#     print("hello python!")
# hello()


#task 2

# def greet(name):
#     print("sn bna uu?", name)
# greet("bat")


#task 3

# def introduce(name, age):
#     print(name, age,"nastai")
# introduce("bat", 18)


#task 4

# def add(a, b):
#     print(a + b)
# add(10, 20)


#task 5

# def square(num):
#     return num ** 2
# result = square(5)
# print(result)


#task 6

# def max_num(a, b):
#     return max(a, b)
# a = max_num(15, 20)
# print(a)


#task 7

# def check_even(num):
#     if num % 2 == 0:
#         print("even")
#     elif num % 2 != 0:
#         print("odd")
#     return num
# check_even(7)      


#task 8

# def check_age(age):
#     if age >= 18:
#         print("adult")
#     else:
#         print("minor")
#     return age
# check_age(18)

#task 9

# def get_grade(score):

#         if 90 <= score <=100:
#             return "A"
#         elif 80 <= score <= 90:
#             return "B"
#         elif 70 <= score <= 80:
#             return "C"
#         elif 60 <= score <= 70:
#             return "D"
#         else:
#             return "F"
# score = int(input("dvn: "))
# while 0 > score or score > 100:
#     print("wrong")
# score = int(input("try again:"))
# print(get_grade(score))


#task 10

# def print_numbers(n):
#     for i in range(1, n +1):
#         print(i, end="")
# print_numbers(5)


#task 11

# def sum_numbers(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return print(total) 
# sum_numbers(5)


#task 12

# def count_even(n):
#     count = 0
#     for i in range(1, n +1):
#         if i % 2 == 0:
#             count += 1
#     return print(count)
# count_even(10)


#task 13

# def count_digits(num):



#task 14

# def find_max(nums):
#     return print(max(nums))
# find_max([4, 8, 2, 15, 6])


#task 15

# def find_min(nums):
#     return print(min(nums))
# find_min([7, 3, 9, 1, 5])


#task 16

# def count_even(nums):
#     count = 0
#     for i in nums:
#         if i % 2 == 0:
#             count+=1
#     print(count)
# count_even([1, 2, 4, 7, 8, 10])


#task 17

# def list_sum(nums):
#     count = 0
#     for i in nums:
#         count += i
#     return count
# print(list_sum([10, 20, 30, 40]))


#task 18

# def get_age(students, name):
#     return students[name]
# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }

# print(get_age(students, "Sara"))


#task 19

# def find_student(students, name):
#     if name in students:
#         return "found"
#     else:
#         return "not found"
# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }

# print(find_student(students, "Sara"))


#task 20

# def average_score(students):
#     total_count = sum(students.values())
#     count = len(students)
#     return total_count / count
# students = {
#     "Bat": 80,
#     "Sara": 90,
#     "Bold": 70
# }

# print(average_score(students))


#task 21

# def unique_count(nums):
#     a = set(nums)
#     return len(a)
# nums = [1, 2, 2, 3, 3, 3, 4]
# print(unique_count(nums))


#task 22

# def unique_count(nums):
#     a = set(nums)
#     return (a)
# nums = [1, 2, 2, 3, 3, 3, 4]
# print(unique_count(nums))


#task 23

# def greet(name="Guest"):
#     print("hello", name)
# greet("Bat")


#task 24

# def power(num, exponent = 2):
#     return num ** exponent
# print(power(5))
# print(power(2, 3))


#task 25

# def discount(price, percent = 10):
#      a = price * percent / 100
#      return int(price - a)
# print(discount(10000))
# print(discount(10000, 20))


#task 26

# def sum_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(sum_all(1, 2, 3))
# print(sum_all(10, 20, 30, 40))


#task 27

# def find_max(*args):
#     return max(args)
# print(find_max(5, 8, 2, 10, 3))


#task 28

# def count_even(*args):
#     count = 0
#     for i in args:
#         if i % 2 == 0:
#             count += 1
#     return count
# print(count_even(1, 2, 4, 7, 8, 10))


#task 29


# def show_info(**kwargs):
#     for key, values in kwargs.items():
#         print(key, values)
# show_info(name="Bat", age=18, city="Ulaanbaatar")


#task 30

# def calculate_total(**prices):
#     count = 0
#     for name, prices in prices.items():
#         count += prices
#     return count
# print(calculate_total(
#     apple=2000,
#     banana=3000
#     orange=2500
# ))


#task 31

# def analyze_numbers():
#     count = 0
#     count2 = 0
#     for num in nums:
#         if num % 2 == 0:
#             count += 1
#         elif num % 2 != 0:
#             count2 += 1
#     return max(nums), min(nums), sum(nums), count, count2
# nums = list(map(int, input().split()))
# print(list(analyze_numbers()))
