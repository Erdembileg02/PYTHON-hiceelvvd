# ============================================================
# HICHEEL 1 — 11. Функц
# ============================================================



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
