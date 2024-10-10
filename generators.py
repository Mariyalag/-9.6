
def all_variants(text):
    n = len(text)
    for start in range(n):
        for fin in range(start + 1, n + 1):
            yield text[start:fin]


a = all_variants("abc")
for i in a:
    print(i)








# прмер 1 - создание простого генератора

# def func_generator(n):
#     i =0
#     while i != n:
#         yield i
#         i += 1
#
# obj = func_generator(10)
# print(obj)
#
# for i in obj:
#     print(i)

# пример 2 - создание ф фибоначии
# def fibonacci_v1(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result

# def fibonacci_v2(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# fib_1 = fibonacci_v1(n=10)
# print(fib_1)
# for value in fib_1:
#     print(value)
#
# fib_2 = fibonacci_v2(n=10)
# print(fib_2)
# for value in fib_2:
#     print(value)

# пример 3 - бесконечный список значений
# def fibonacci_v3():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# for value in fibonacci_v3():
#     print(value)
#     if value > 10 ** 6:
#         break

# пример 4

# import time
#
# start = time.time()

# def read_large_file(file_path):
#     with open(file_path, "r", encoding='utf-8') as file:
#         for line in file:
#             yield line.strip()
#
# for line in read_large_file("large_file.txt"):
#     print(line)
#
# fin = time.time()
# print((fin-start) * 1000)