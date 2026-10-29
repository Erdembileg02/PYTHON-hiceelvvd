# ============================================================
# HICHEEL 1 — 09. Жагсаалт болон алгоритмын бодлогууд
# ============================================================


# nums = list(map(int, input().split()))

# nums.sort()

# print(nums[-2])


#task 2

# nums = list(map(int, input().split()))
# result = []

# for i in nums:
#     if i not in result:
#         result.append(i)

# print(result)

# text = input()

# reverse = ""

# for i in range(len(text)-1, -1, -1):
#     reverse += text[i]

# if text == reverse:
#     print("YES")
# else:
#     print("NO")

#task 4

# words = input().split()

# longest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print(longest)

#task 5

# text = input().lower()
# vowels = "аэиоуөү"
# count = 0

# for ch in text:
#     if ch  in vowels:
#         count += 1

# print(count)

#task 6

# n = int(input())
# total = 0

# for i in range(1, n + 1):
#         total += i

# print(total)

#task 7

# n = int(input())
# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit
#     n // 10

# print(total)

#task 8

# n = int(input())
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse + digit
#     n //= 10

# print(reverse)




# 1 Хоёр дахь хамгийн их тоо

# nums = [7, 3, 9, 9, 2, 5, 7, 8]

# nums.sort()
# a = set(nums)
# b = list(a)
# print(b[-2])

# 2 Хоёр дахь хамгийн бага тоо

# nums = [7, 3, 9, 9, 2, 5, 7, 8]

# nums = [7, 3, 9, 9, 2, 5, 7, 8]
# nums.sort()
# a = set(nums)
# b = list(a)
# print(b[1])


# 3 Хамгийн урт дараалсан сондгой хэсэг

# nums = [2, 1, 3, 5, 4, 7, 9, 11, 6]

# a = 0
# b = 0
# for n in nums:
#     if n % 2 == 1:
#         b += 1
#         a = max(a, b)
#     else:
#         b = 0
# print(a)



# 4 Хамгийн урт өсөх дараалал

# nums = [1, 2, 4, 2, 3, 5, 7, 1]
# a = 0
# b = 0
# for n in nums:
#     if n % 2 == 1:
#         b += 1
#         a = max(a, b)
#     else:
#         b = 0
# print(a)



#5 Хамгийн олон давтагдсан тоо
# nums= [1, 2, 4, 2, 3, 5, 7, 1]
# count ={}
# for n in nums:
#     count[n]= count.get(n, 0) + 1
# m = max(count.values())
# print(min(n for n, c in count.items()if c == m))


#6 Давтамжийн хамгийн бага

# nums= [1, 2, 4, 2, 3, 5, 7, 1]
# count ={}
# for n in nums:
#     count[n]= count.get(n, 0) + 1
# m = min(count.values())
# print(min(n for n, c in count.items()if c == m))


#7 Хоёр list-ийн нийтлэг элемент

# a = [1, 2, 3, 4, 5]
# b = [3, 5, 7, 8, 1]
# print(sorted(set(a)&set(b)))


#8 Нийлбэр нь хамгийн их хос

# nums =[4, 7, 2, 9, 5]
# s = sorted(nums, reverse=True)
# print(s[0], s[1])
