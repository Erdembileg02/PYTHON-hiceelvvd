# lst = [5,10,15,20,25,30]

# target = int(input())
# left = 0
# right = len(lst)-1
# while left <= right:
#     mid = (right + left) // 2
#     if lst[mid] == target:
#         print("olloo")
#         break
#     elif lst[mid] < target:
#         left = mid + 1
#     else:
#         right = mid -1


# 🟢 Level 1 — Хялбар

# 1. Тоо хайх

# numbers = [3, 7, 12, 18, 25, 31, 40]

# target= int(input("too: "))
# left = 0
# right = len(numbers) -1
# while left <= right:
#     mid = (right + left) // 2
#     if numbers[mid] == target:
#         print("found")
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid -1


# 2. Индекс олох

# numbers = [5, 10, 15, 20, 25, 30]

# target = int(input("too: "))
# left = 0
# right = len(numbers) - 1
# result = -1

# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         result = mid
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(result)



# 3. Эхний элементийг хайх

# numbers = [4, 9, 14, 19, 24, 29, 34]

# target= int(input("too: "))
# left = 0
# right = len(numbers) -1
# while left <= right:
#     mid = (right + left) // 2
#     if numbers[mid] == target:
#         print(target)    
#         print(mid)
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid -1



# 4. Сүүлийн элементийг хайх

# lst = [6, 12, 18, 24, 30, 36, 42]

# target = int(input())
# left = 0
# right = len(lst)-1
# while left <= right:
#     mid = (right + left) // 2
#     if lst[mid] == target:
#         print(right)
#         break
#     elif lst[mid] < target:
#         left = mid + 1
#     else:
#         right = mid -1


# 5. Байхгүй тоо хайх

# lst = [10, 20, 30, 40, 50, 60]

# target = int(input())
# left = 0
# right = len(lst)-1
# while left <= right:
#     mid = (right + left) // 2
#     if lst[mid] == target:
#         print("olloo")
#         break
#     elif lst[mid] < target:
#         left = mid + 1
#     else:
#         right = mid -1
# print("haij bui too bhgu")


# 6. Хайлтын алхам тоолох

# def search():

#     count = 0
#     left = 0
#     right = len(score)-1
#     while left <= right:
#         mid = (right + left) // 2
#         if score[mid] == target:
#             print("olloo")
#             count += 1
#             break
#         elif score[mid] < target:
#             left = mid + 1
#             count += 1
#         else:
#             right = mid -1
#             count += 1
#     print(count)
        
# score = list(map(int, input().split()))
# target = int(input())
# (search())



# 7. Сурагчийн оноо хайх

# def search():

#     left = 0
#     right = len(scores) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if scores[mid] == target:
#             print("olloo")
#             print(mid)
#             break
#         elif scores[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
# scores = list(map(int, input().split()))
# target = int(input("too: "))
# search()


# 8. Барааны код хайх

# def search():

#     left = 0
#     right = len(scores) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if scores[mid] == target:
#             print("baraa bvrtgeltei")
#             break
#         elif scores[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     else:
#         print("baraa oldsngvi")
# scores = list(map(int, input().split()))
# target = int(input("too: "))
# search()



# 9. Номын дугаар хайх

# def search():

#     left = 0
#     right = len(scores) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if scores[mid] == target:
#             print("baraa bvrtgeltei")
#             break
#         elif scores[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     else:
#         print("baraa oldsngvi")
# scores = list(map(int, input().split()))
# target = int(input("too: "))
# search()


# 10. Тооны байрлалыг тодорхойлох

# def search():

#     count = 0
#     left = 0
#     right = len(scores) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if scores[mid] == target:
#             print(mid)
#             print(left, right, mid)
#             count += 1
#             break
#         elif scores[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     else:
#         print("oldsngvi")
#     print(count)
# scores = list(map(int, input().split()))
# target = int(input("too: "))
# search()



# 11. Хамгийн эхний давхардсан тооны индекс


# def search():

#     left = 0
#     right = len(score) -1
#     while left <= right:
#         mid = (right + left) // 2
#         if score[mid] == target:
#             print("olloo","\n", mid)
#             break
#         elif score[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
# score = list(map(int, input("too: ").split()))
# target = int(input("target: "))
# search()








# prices = {
#     "талх": 2500, 
#     "сүү": 3200, 
#     "өндөг": 450, 
#     "ус": 1000, 
#     "алим": 1800
#     }

# while True:
#     baraa = input("baraa: ")
#     shirheg = int(input("pcs: "))
#     for key, value in prices.items():
#         if baraa in prices:
#             print(baraa, value * shirheg)   
#             break
       
            
