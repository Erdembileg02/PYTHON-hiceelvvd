# ============================================================
# HICHEEL 1 — 08. Set ба Dictionary
# ============================================================



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
