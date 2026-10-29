# class player:
#     def __init__(self, name, skins):
#         self.name = name
#         self.skins = skins

# player1 = player("Erdembileg", 1)
# player2 = player("Erdmee", 1)

# print(player1.name)
# print(player1.skins)

# print(player2.name)
# print(player2.skins)



# 2-р дасгал. Хоёр сурагч үүсгэх

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# student1 = student("Naraa", 17)
# student2 = student("Temvvlen", 19)

# print(student1.name)
# print(student1.age)

# print(student2.name)
# print(student2.age)



# 3-р дасгал. Сурагчийн анги нэмэх

# class student:
#     def __init__(self, ner, nas, angi):
#         self.ner = ner
#         self.nas = nas
#         self.angi = angi

# student1 = student("bat", 18,"12A")

# print("ners",":", student1.ner)
# print("nas",":", student1.nas)
# print("angi",":", student1.angi)



# 4-р дасгал. Оноо хадгалах

# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# student1 = student("bat", 85)
# student2 = student("saraa", 95)

# print(student1.name,"-", student1.score)

# print(student2.name,"-", student2.score)



# 5-р дасгал. Сурагчийн оноог нэмэх

# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def_score(self):
#         self.score += 5

# student1 = student("bat", 80)
# student1.add_score()
# print(student1.name)
# print(student1.score)



# 6-р дасгал. Сурагчийн мэдээлэл хэвлэх method

# class student:
#     def __init__(self, ner, nas, angi):
#         self.ner = ner
#         self.nas = nas
#         self.angi = angi

#     def show_info(self):
#         print(f"{student1.ner}\n{student1.nas}\n{student1.angi}")

# student1 = student("Saraa", 19, "12B")
# student1.show_info()



# 7-р дасгал. Сурагч тэнцсэн эсэхийг шалгах

# class student:
#     def __init__(self, ner, score):
#         self.ner = ner
#         self.score = score

#     def check_result(self):
#         if self.score > 60:
#             print(self.ner, ":", "tentssen")
#         else:
#             print(self.ner, ":", "tentseegvi")
            

# student1 = student("Bat", 75)
# student2 = student("Naraa", 45)

# student1.check_result()
# student2.check_result()




# 8-р дасгал. Оноо нэмэх

# class student:
#     def __init__(self, name , score):
#         self.name = name
#         self.score = score

#     def add_score(self):
#         self.score += 5

# student1 = student("Bat", 80)
# student1.add_score()

# print(student1.name)
# print(student1.score)



# 9-р дасгал. Нас нэмэх

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def birthday(self):
#         self.age += 1

# student1 = student("Saraa", 18)
# student1.birthday()
# print(student1.age)



# 10-р дасгал. Онооны үнэлгээ

# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_grade(self):
#         if 0 < self.score < 100:
#             if self.score > 90:
#                 print(self.name, "A")
#             elif self.score > 80:
#                 print(self.name, "B")
#             elif self.score > 70:
#                 print(self.name, "C")
#             elif self.score > 60:
#                 print(self.name, "D")
#             else:
#                 print(self.name, "F")
#         else:
#             print("buruu onoo")

# student1 = student("bat", 94)
# student2 = student("Saraa", 79)

# student1.get_grade()
# student2.get_grade()



# 11-р дасгал. Ирц бүртгэх

# class sdudent:
#     def __init__(self, name, irts):
#         self.name = name
#         self.irts = irts
#     def show_attendance(self):
#         self.irts += 0
# sdudent1 = sdudent("bat", 2)
# sdudent1.show_attendance()
# print(sdudent1.name, ":", sdudent1.irts)




# 12-р дасгал. Хичээлд тэнцэх эсэх

# class student:
#     def __init__(self, name, score, irts):
#         self.name = name
#         self.score = score
#         self.irts = irts

#     def check_result(self):
#         if self.score >= 60 and self.irts >= 80:
#             print(self.name,":" "Хичээлд тэнцсэн")
#         else:
#             print(self.name,":" "Хичээлд тэнцээгүй")

# student1 = student("bat", 70, 79)
# student1.check_result()



# 13-р дасгал. Сурагчийн онооны жагсаалт

# class student:
#     def __init__(self, name, scores):
#         self.name = name
#         self.score = scores

#     def show_scores(self):
#         print(self.score)

#     def add_score(self, score):
#         self.score.append(score)

#     def average(self):
#         if self.score:
#             print(sum(self.score) / len(self.score))
#         else:
#             print("onoo bhgui")

# student1 = student("Бат", [80, 90, 70])

# student1.show_scores()
# student1.add_score(100)
# student1.show_scores()
# student1.average()



# 14-р дасгал. Сурагчийн мэдээлэл шинэчлэх

# class student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def show_info(self):
#         print(self.name, self.grade)

#     def change_name(self, new_name):
#         self.name = new_name

#     def change_grade(self, new_grade):
#         self.grade = new_grade

# student1 = student("Bat", "12B")

# student1.show_info()
# student1.change_name("dorj")
# student1.change_grade("12A")

# print(student1.name, student1.grade)



# 15-р дасгал. Шалгалтын бүртгэлийн систем

# class student:
#     def __init__(self, name, grade, score):
#         self.name = name
#         self.grade = grade
#         self.score = score

#     def show_info(self):
#         print(self.name, self.grade, self.score)

#     def add_score(self, score):
#         self.score.append(score)

#     def check_result(self):
#         if self.score >= 60:
#             print("tentssen")
#         else:
#             print("tentseegvi")

#     def average(self):
#         if self.score:
#             print(sum(self.score) / len(self.score))
#         else:
#             print("onoo bhgu")

# student1 = student("Bat", "12A", [60, 55])
# student1.add_score(5)
# student1.check_result()
# student1.average()

# print(student1.name, student1.grade, student1.score)




# 1-р дасгал. Утасны цэнэг 🔋

# class phone:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery

#     def use_phone(self):
#         self.battery = (self.battery - 10)

#     def show_battery(self):
#         print(self.battery)

#     def charge(self):
#         self.battery = (self.battery + 20)

#     def show_battery(self):
#         print(f"Цэнэг: {self.battery}%")

# phone1 = phone("iphone", 80)

# phone1.use_phone()
# phone1.show_battery()

# phone1.charge()
# phone1.show_battery()



# 2-р дасгал. Дэлгүүрийн бүтээгдэхүүн 🛒

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def sell(self, amount):
#         if amount <= 0:
#             print("zarah baraa 0s ih bh hergte")
#         elif amount <= self.quantity:
#             self.quantity -= amount
#             print(f" vldsn baraa: {self.quantity} shirheg")
#         else:
#             print("baraa hvreltsehgvi bna")

#     def show_total(self):
#         print(f" niit vne: {self.price * self.quantity}₮")


# product1 = Product("mouse", 30000, 10)

# product1.sell(3)
# product1.show_total()



# 3-р дасгал. Тамирчны оноо 🏐

# class athlete:
#     def __init__(self, name, points):
#         self.name = name
#         self.points = points

#     def add_points(self, points):
#         self.points = self.points + points

#     def lose_points(self, points):
#         self.points = self.points - points

#     def show_points(self):
#         print(f"onoo: {self.points}")

# athlete1 = athlete("Bat", 20)

# athlete1.add_points(15)
# athlete1.lose_points(5)
# athlete1.show_points()



# 4-р дасгал. Киноны мэдээлэл 🎬

# class movie:
#     def __init__(self, title, rating, views):
#         self.title = title
#         self.rating = rating
#         self.views = views

#     def add_view(self, views):
#         print(f"views umnu: {self.views}")
#         print(f"views daraa: {self.views + views}")

#     def update_rating(self, rating):
#         print(f"rating umnu: {self.rating}")
#         print(f"rating daraa: {self.rating + rating}")

#     def show_info(self):
#         print(f"kino: {self.title}")
#         print(f"vnelgee: {self.rating}")
#         print(f"vzelt: {self.views}")

# movie1 = movie("titanic", 8, 1000)

# movie1.add_view(50)
# movie1.update_rating(2)
# movie1.show_info()



