# selection sort == Big O (n2)


# numbers = [5, 3, 8, 1, 2]

# for i in range(len(numbers) -1):
#     min_index = i

#     for j in range(i + 1, len(numbers)):
#         if numbers[j] < numbers[min_index]:
#             min_index = j

#     temp = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = temp

# print(numbers)


# I. Суурь бодлогууд

# 1. Өсөхөөр эрэмбэлэх

# arr = list(map(int,input("too: ").split()))

# for i in range(len(arr) -1):
#     min_index = i

#     for j in range( i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j

#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp

# print(arr)


# 2. Хамгийн бага 3 тоог эрэмбэлэх

# arr = list(map(int, input("too: ").split()))

# for i in range(len(arr)-3):
#     min_index = i

#     for j in range( i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j

#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp

# print(arr)


# 3. Буурахаар эрэмбэлэх

# arr = list(map(int, input("too: ").split()))

# for i in range(len(arr) -1):
#     min_index = i

#     for j in range(i + 1, len(arr)):
#         if arr[j] > arr[min_index]:
#             min_index = j

#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp

# print(arr)


# 4. Сөрөг тоотой жагсаалт

# arr = list(map(int, input("too: ").split()))

# for i in range(len(arr) -1):
#     min_index = i

#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j

#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp

# print(arr)


# 5. Давхардлыг арилгаж эрэмбэлэх

# arr = list(map(int, input("too: ").split()))

# for i in range(len(arr) -1):
#     min_index = i

#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j

#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp

# print(set(arr))

# 6. Хамгийн бага утгыг эхэнд байрлуулах

# arr = list(map(int, input("too: ").split()))

# swapped = False

# for i in range(len(arr) -1):
#     min_index = i
    
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
        

#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
#     swapped = True
#     break

# print(arr)


# 7. Нэг алхмын үр дүн

# arr = list(map(int, input("too: ").split()))

# swapped = False

# for i in range(len(arr) -1):
#     min_index = i

#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j


#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
#     swapped = True
#     break    
    
# print(arr)


# 8. Эхний хоёр алхмын үр дүн

# arr = list(map(int, input("too: ").split()))

# count = 0


# for i in range(len(arr) -1):
#     min_index = i
#     count += 1

#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j

#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp

#     if count == 2:
#         print(count, arr)
#         break


# 9. Хэдэн удаа солигдох вэ?

# arr = list(map(int, input("too: ").split()))

# count = 0

# for i in range(len(arr) -1):
#     min_index = i
#     count += 1

#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j

#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp

#     print(count, arr)
        


# 10. Аль жагсаалт эрэмбэлэгдсэн бэ?

# a = list(map(int, input("too: ").split()))
# b = list(map(int, input("too: ").split()))
# c = list(map(int, input("too: ").split()))

# def is_sorted(lst):
#     return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# lists = {"a": a, "b": b, "c": c}

# for name, lst in lists.items():
#     print(name, lst, "->", "эрэмбэлэгдсэн" if is_sorted(lst) else "эрэмбэлэгдээгүй")


# 11. Selection Sort функц

# def selection_sort(arr):

#     for i in range(len(arr) -1):
#         min_index = i

#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#     return arr
# numbers = [5, 3, 8, 1, 2]
# print(selection_sort(numbers))


# 12. Буурах дарааллын функц


# def selection_sort_desc(arr):

#     for i in range(len(arr) -1):
#         min_index = i

#         for j in range(i + 1, len(arr)):
#             if arr[j] > arr[min_index]:
#                 min_index = j

#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#     return arr
# numbers = [5, 3, 8, 1, 2]
# print(selection_sort_desc(numbers))


# 13. Хамгийн бага элементийн индекс


# arr = list(map(int, input("too: ").split()))

# min_index = 0

# for i in range( 1, len(arr)):
#     if arr[i] < arr[min_index]:
#         min_index = i

# print(min_index)


# 14. Эрэмбэлэх явцыг харуулах

# arr = list(map(int, input("too: ").split()))

# for i in range(len(arr) -1):
#     min_index = i

#     for j in range( i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j

#     temp = arr[i] 
#     arr[i] = arr [min_index]
#     arr[min_index] = temp
    
#     print(arr)



# 15. Bubble Sort ба Selection Sort

# def bubble_sort(num):
#     for i in range(len(num) -1):
#         for j in range(len(num) -1 -i):
#             if num[j] > num[j + 1]:
#                 temp = num[j]
#                 num[j] = num[j + 1]
#                 num[j + 1] = temp
#     return num
# num = list(map(int, input("too: ").split()))
# print(bubble_sort(num))

# def selection_sort(arr):

#     for i in range(len(arr) -1):
#         mid_index = i

#         for j in range( i + 1, len(arr)):
#             if arr[j] < arr[mid_index]:
#                 mid_index = j

#         temp = arr[i]
#         arr[i] = arr[mid_index]
#         arr[mid_index] = temp
#     return arr

# arr = list(map(int, input("too: ").split()))
# print(selection_sort(arr))

# if bubble_sort(num) == selection_sort(arr):
#     print("adil")
# else:
#     print("uur")