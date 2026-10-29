# ============================================================
# HICHEEL 1 — 04. Давталт (while)
# ============================================================



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

