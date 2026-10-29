# 1. Тооны шинж

# n = int(input("too:"))

# if n == 0:
#     print(0)
# elif n >= 0:
#     print("eyreg")
# else:
#     print("surug")



# 2. Үнэлгээ

# n = int(input("onoo: "))

# if 0 <= n < 100:
#     if n >= 90:
#         print("A")
#     elif n >= 80:
#         print("B")
#     elif n >= 70:
#         print("C")
#     elif n >= 60:
#         print("D")
#     else:
#         print("F")
# else:
#     print("buruu onoo")



# 3. Өндөр жил

# year = int(input("jil: "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Өндөр жил")
# else:
#     print("Энгийн жил")


# 4. Гурвалжны төрөл


# a, b, c = map(int, input().split())

# if a + b <= c or a + c <= b or b + c <= a:
#     print("Гурвалжин үүсэхгүй")
# elif a == b == c:
#     print("Тэгш талт")
# elif a == b or a == c or b == c:
#     print("Адил хажуут")
# else:
#     print("Энгийн")



# 5. Таксины төлбөр

# km = int(input("km: "))
# hour = int(input("tsag: "))
# vne = 1500

# if 6 <= hour <= 21:
#     if km == 1 or km == 2:
#         print(3000)
#     else:
#         print(km * 1500)
# else:
#     print(km * vne + 2000)



# 6. Тэгш тоонуудын нийлбэр

# n = int(input("too: "))

# count = 0

# for i in range(n):
#     if i % 2 == 0:
#         count += i
# print(count)



# 7. Цифрүүдийн нийлбэр

# n = int(input())

# total = 0

# while n > 0:
#     too = n % 10
#     total += too
#     n = n // 10

# print(total)



# 8. Тоог урвуулах


# n = int(input())

# total = 0

# while n > 0:
#     too = n % 10
#     total = total * 10 + too
#     n = n // 10

# print(total)



# 9. ФизБазз

# n = int(input("too: "))

# for i in range(1, n + 1):
#     if i % 15 == 0:
#         print("ФизБаз")
#     elif i % 3 == 0:
#         print("Физ")
#     elif i % 5 == 0:
#         print("Базз")
#     else:
#         print(i)




# 10. Нууц тоо таах

# secret = 37
# oroldlogo = 0

# while True:
#     too = int(input("too ug: "))
#     oroldlogo += 1
#     if too > secret:
#         print("ih")
#     elif too < secret:
#         print("baga")
#     else:
#         print("Зөв!", oroldlogo, "oroldlogo")
#         break

  

# 11. Үржүүлэх хүснэгт

# n = int(input("too: "))

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end =" ")
#     print()



# 12. Одон пирамид

# n = int(input())

# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))



