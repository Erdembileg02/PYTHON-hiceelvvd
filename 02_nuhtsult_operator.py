# ============================================================
# HICHEEL 1 — 02. Нөхцөлт оператор (if / elif / else)
# ============================================================



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

