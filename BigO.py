#task 1
# O(1)

#task 2
# O(n)

#task 3
# O(1)

#task 4
# O(n)

#task 5
# B. O(n)

#task 6
# O(n2)

#task 7
# O(n2)

#task 8
# O(n2)

#task 9
# O(n)

#task 10
# O(n2)

#task 11
# O(log n)

#task 12


#task 13
# O(1)
# O(n)

#task 14
# O(n)

#task 15
# O(n2)

#bonus
# O(1)
# O(log n)
# O(n)
# O(n2)

# 🔥
# A
# O(1)

# B
# O(n)

# C
# O(n2)

# D
# O(log n)




# 1. Нөхцөл (if/elif/else, match, харьцуулалт, логик оператор)
# 1.1 🟢 Кино театрын нас

# a = int(input("nas: "))

# if a < 18:
#     print("oroh bolomjgvi")
# else:
#     print("oroh bolomjtoi")


# 1.2 🟢 Тэгш үү, сондгой юу?

# a = int(input("too: "))

# if a % 2 == 0:
#     print("tegsh")
# elif a % 2 != 0:
#     print("sondgoi")


# 1.3 🟢 Аль нь их вэ?

# a = int(input("too: "))
# b = int(input("too: "))


# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# if a == b:
#     print("tentsvv")


# 1.4 🟡 Долоо хоногийн өдөр

# a = int(input("garag: "))

# if 0 < a < 8:
#     if a == 1:
#         print("Monday")
#     elif a == 2:
#         print("Tuesday")
#     elif a == 3:
#         print("Wednesday")
#     elif a == 4:
#         print("Thursday")
#     elif a == 5:
#         print("Friday")
#     elif a == 6:
#         print("Saturday","amraltiin udur")
#     else:
#         print("Sunday","amraltiin udur")
# else:
#     print("buruu too")


# 1.5 🟡 Таксины төлбөр


# a = int(input("KM: "))
# b = int(input("hour: "))

# if a <= 2:
#     x = 3000
# else:
#     x = 3000 + 3 * 1500
# if b >= 22 or b < 6:
#     print(x * 1.2)
# else:
#     print(x)


# 1.6 🔴 Шаталсан цахилгааны төлбөр

# a = int(input("kwh: "))
# if a <= 150:
#     print(a * 100)
# elif 151 < a < 300:
#     print(150 * 100 + (a - 150)*150 )
# elif a > 300:
#     print(150 * 150 + 150 * 150 + (a - 150) * 150)


# 1.7 🔴 Нэвтрэх систем (гүн шийдвэр)

# username = input()
# password = input()
# is_blocked = input() == "True"
# failed_attempts = int(input())

# if is_blocked:
#     print("Таны эрх хаагдсан байна")

# elif username == "" or password == "":
#     print("Мэдээллээ бүрэн оруулна уу")


# elif username != "admin":
#     print("Хэрэглэгч олдсонгүй")

# elif password != "1234":
#     if failed_attempts >= 2:
#         print("Эрх хаагдлаа")
#     else:
#         print("Нууц үг буруу")

# else:
#     print("Амжилттай нэвтэрлээ")


