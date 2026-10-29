# ============================================================
# HICHEEL 1 — 07. Tuple
# ============================================================



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

