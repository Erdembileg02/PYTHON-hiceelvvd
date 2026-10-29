# ============================================================
# HICHEEL 1 — 10. Хоёр хэмжээст жагсаалт (nested list)
# ============================================================



# m = [
#       [1,2,3],
#       [4,5,6],
#       [7,8,9]
    # ]
# for i in range(0,len(m)):
#     for j in m[i]:
#         print(j, end="")
#     print()


# I. Index ашиглах — Амархан

# 1. 6 тоог хэвлэ

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# for i in nums:
#     print(i)


# 2. "Bold" нэрийг хэвлэ

# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]

# a = students[2][0]
# print(a)


# 3. 2 дахь мөрийг хэвлэ

# nums = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]

# a = nums[1]
# print(a)


# 4. 70 тоог хэвлэ

# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# a = nums[2][0]
# print(a)


# 5. Хамгийн эхний утгыг хэвлэ

# nums = [
#     [5, 10],
#     [15, 20]
# ]

# a = nums[0][0]
# print(a)


# 6. Хамгийн сүүлийн утгыг хэвлэ

# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# a = nums[2][1]
# print(a)


# II. Nested loop — Суурь


# 7. Бүх мөрийг хэвлэ

# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

# for i in nums:
#     print(i)


# 8. Бүх тоог хэвлэ

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# for i in range(len(nums)):
#     for j in nums[i]:
#         print(j)


# 9. Бүх тоог нэг мөрөнд хэвлэ

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# for i in range(len(nums)):
#     for j in nums[i]:
#         print(j, end=" ")


# 10. 10-аас их тоонуудыг хэвлэ

# nums = [
#     [3, 12, 5],
#     [20, 7, 15]
# ]

# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j > 10:
#             print(j, end=" ")


# III. Count ба Sum — Дунд


# 11. Нийт хэдэн тоо байгааг ол

# nums = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         count+=1
# print(count)


# 12. Бүх тооны нийлбэрийг ол

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         count += j
# print(count)


# 13. Тэгш тоонуудыг хэвлэ

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j % 2 == 0:
#             print(j, end = " ")


# 14. Сондгой тоонуудын тоог ол

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j % 2 != 0:
#             print(j, end = " ")


# 15. Тэгш тоонуудын нийлбэрийг ол

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j % 2 == 0:
#             count += j
# print(count, end = " ")


# 16. Эерэг тоонуудын тоог ол

# nums = [
#     [-3, 5, 0],
#     [7, -2, 8],
#     [-1, 4, 0]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j > 0:
#             count += 1
# print(count)


# 17. Сөрөг тоонуудын нийлбэрийг ол

# nums = [
#     [-2, 3, -5],
#     [4, -1, 6]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j <0:
#             count += j
# print(count)


# IV. Min / Max — Дунд


# 18. Хамгийн их тоог ол

# nums = [
#     [4, 8, 2],
#     [10, 3, 7],
#     [1, 6, 5]
# ]

# a = nums[1]
# print(max(a))

# 19. Хамгийн бага тоог ол

# nums = [
#     [7, 2, 9],
#     [4, -3, 6],
#     [8, 1, 5]
# ]

# a = []
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         a.append(j)
#         b = min(a)
# print(b)


# 20. Мөр бүрийн нийлбэрийг ол

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# count = 0
# for i in nums:
#         count = sum(i)
#         print(count)


# 21. Мөр бүрийн хамгийн их тоог ол

# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]


# count = 0
# for i in nums:
#         count = max(i)
#         print(count)


# 22. Мөр бүрийн хамгийн бага тоог ол

# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]


# count = 0
# for i in nums:
#         count = min(i)
#         print(count)



# V. Хайлт ба нөхцөл — Дунд/Хэцүү


# 23. 7 тоо байгаа эсэхийг шалга

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# if 7 in sum(nums, []):
#     print("YES")
# else:
#     print("NO")

# 24. Өгөгдсөн тоо хэдэн удаа байгааг ол

# nums = [
#     [1, 2, 3],
#     [2, 4, 2],
#     [5, 2, 6]
# ]

# target = 2

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if j == target:
#             count += 1
# print(count)


# 25. 5-аас их тоонуудын нийлбэрийг ол

# nums = [
#     [1, 7, 3],
#     [9, 2, 6],
#     [4, 8, 5]
# ]

# count = 0
# for i in range(0, len(nums)):
#     for j in nums[i]:
#         if 5 < j:
#             count += j
# print(count)


# 26. Хамгийн их нийлбэртэй мөрийг ол

# nums = [
#     [1, 2, 3],
#     [10, 20, 30],
#     [4, 5, 6]
# ]

# a = []
# count = 0
# for i in nums:
#     count = sum(i)
#     a.append(count)
# print(nums[a.index(max(a))])


# VI. Сурагчийн өгөгдөл — Хэцүү


# 27. Сурагч бүрийн нэр ба насыг хэвлэ

# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]

# for student in students:
#     print(student[0], student[1])


# 28. 18-аас дээш настай сурагчдыг хэвлэ

# students = [
#     ["Bat", 17],
#     ["Sara", 19],
#     ["Bold", 20],
#     ["Anu", 16]
# ]

# for key, value in students:
#     if value > 18:
#         print(key, value)



