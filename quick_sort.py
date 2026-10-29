# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [8, 3, 1, 7, 0, 10, 2]

# print(quick_sort(numbers))



# 1. Өсөх дарааллаар эрэмбэлэх

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)

# numbers = [8, 3, 1, 7, 4]

# print(quick_sort(numbers))



# 2. Буурах дарааллаар эрэмбэлэх

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num > pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)

# numbers = [5, 2, 9, 1, 7]

# print(quick_sort(numbers))



# 3. Давхардсан тоонуудыг эрэмбэлэх

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)

# numbers = [4, 2, 4, 1, 2, 3, 1]

# print(quick_sort(numbers))



# 4. Сөрөг болон эерэг тоог эрэмбэлэх

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)

# numbers = [3, -5, 0, 8, -2, 1]

# print(quick_sort(numbers))



# 5. Хамгийн бага 3 тоог олох

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)



# numbers = [9, 2, 7, 1, 5, 3]

# print(quick_sort(numbers)[:3])



# 6. Хамгийн их 2 тоог олох

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)



# numbers = [4, 9, 1, 7, 3, 8]

# print(quick_sort(numbers)[4:])



# 7. Оюутнуудыг оноогоор эрэмбэлэх

# def quick_sort(stundent):
#     if len(stundent) <= 1:
#         return stundent

#     pivot = stundent[len(stundent) // 2]

#     left = []
#     middle = []
#     right = []

#     for i in stundent:
#         if i[1] < pivot[1]:
#             left.append(i)
#         elif i[1] > pivot[1]:
#             right.append(i)
#         else:
#             middle.append(i)

#     return quick_sort(left) + middle + quick_sort(right)



# stundent = [("Bat", 85), ("Bold", 70), ("Saraa", 95), ("Anu", 60)]

# print(quick_sort(stundent))



# 8. Үгийн уртаар эрэмбэлэх

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for i in arr:
#         if len(i) < len(pivot):
#             left.append(i)
#         elif len(i) > len(pivot):
#             right.append(i)
#         else:
#             middle.append(i)

#     return quick_sort(left) + middle + quick_sort(right)

# fruits = ["banana", "cat", "apple", "hi", "dog"]

# print(quick_sort(fruits))



# 9. Медиан олох

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []


#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# def median(arr):
#     if not arr:
#         raise ValueError("Массив хоосон байна")

#     sorted_arr = quick_sort(arr)
#     n = len(sorted_arr)
#     mid = n // 2

#     if n % 2 == 1:
#         return sorted_arr[mid]
#     else:
#         return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2


# print(f"{median([8, 2, 6, 4]):g}")



# 10. Хоёр массивыг нэгтгэж эрэмбэлэх

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []


#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)

# a = [8, 3, 5]
# b = [2, 9, 1]

# c = a + b
# result = quick_sort(c)

# print(result)
