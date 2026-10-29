# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = [8, 3, 5, 4, 7, 6, 1, 2]

# print(merge_sort(numbers))



# 1. Тоонуудыг өсөхөөр эрэмбэлэх


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# arr = [38, 27, 43, 3, 9, 82, 10]

# print(merge_sort(arr))



# 2. Буурах дарааллаар эрэмбэлэх


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# arr = [38, 27, 43, 3, 9, 82, 10]

# print(merge_sort(arr))



# 3. Давхардсан тоонуудыг эрэмбэлэх


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# arr = list(map(int, input("too: ").split()))

# print(merge_sort(arr))



# 4. Сөрөг тоонуудыг эрэмбэлэх


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# arr = list(map(int, input("too: ").split()))

# print(merge_sort(arr))



# 5. Тэгш ба сондгой тоонуудтай массив


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] % 2 == 0 <= right[j] % 2 != 0:
#             result.append(left[i])
#             i += 1
#         elif right[j] % 2 == 0 and left[i] % 2 != 0:
#             result.append(right[j])
#             j += 1
#         elif left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# arr = list(map(int, input("too: ").split()))

# print(merge_sort(arr))



# 6. Хоёр эрэмбэлэгдсэн массивыг нэгтгэх


# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# a = list(map(int, input("too: ").split()))
# b = list(map(int, input("too: ").split()))

# numbers = a + b

# print(merge_sort(numbers))




# 7. Хамгийн бага 3 тоог олох


# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# numbers = list(map(int, input("too: ").split()))

# print(merge_sort(numbers)[:3])




# 8. Merge Sort-ийн ажиллагааг тооцоолох


# def merge_sort(numbers):

#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = list(map(int, input("too: ").split()))

# print(merge_sort(numbers))




# 9. Хамгийн их 2 тоог олох


# def merge_sort(numbers):

#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = list(map(int, input("too: ").split()))

# print(merge_sort(numbers)[3:])



# 10. Нэрсийг цагаан толгойн дарааллаар эрэмбэлэх


# def merge_sort(people):

#     if len(people) <= 1:
#         return people

#     mid = len(people) // 2

#     left = people[:mid]
#     right = people[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# people = input("ners: ").split()

# print(merge_sort(people))





# 11. Оноогоор сурагчдыг эрэмбэлэх

# def merge_sort(students):

#     if len(students) <= 1:
#         return students

#     mid = len(students) // 2

#     left = students[:mid]
#     right = students[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i][1] > right[j][1] or (left[i][1] == right[j][1] and left[j] <= right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# n = int(input("suragchdiin too: "))
# students = []

# for i in range(n):
#     names = input("ner: ")
#     scores = int(input("onoo: "))
#     students.append((names, scores))


# print(merge_sort(students))




# 12. Үгсийг уртаар нь эрэмбэлэх


# def merge_sort(ners):

#     if len(ners) <= 1:
#         return ners

#     mid = len(ners) // 2

#     left = ners[:mid]
#     right = ners[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if len(left[i]) < len(right[j]) or (len(left[i]) == len(right[j]) and left[j] <= right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# ners = input("ners: ").split()

# print(merge_sort(ners))




# 13. Эрэмбэлээд Binary Search-ээр хайх


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2

#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# scores = list(map(int, input("too: ").split()))
# target = int(input("haih too: "))
# sorted_scores = merge_sort(scores)
# index = binary_search(sorted_scores, target)

# if index != -1:
#     print(f"{target} утга {index}-р индексд байна.")
# else:
#     print("утга олдсонгүй")




# 14. Анаграм эсэхийг шалгах

