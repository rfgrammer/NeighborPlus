# # IF statements
# x = int(input("Please enter an integer:"))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x ==1:
#     print('Single')
# else:
#     print('More')
#
# # FOR statements
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#
# for w in words[:]:
#     if len(w) > 6:
#         words.insert(0, w)
# print(words)

# # RANGE statements
# for i in range(5):
#     print(i)
#
# for i in range(5, 10):
#     print(i)
#
# for i in range(0, 10, 3):
#     print(i)

# a = ['Marry', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
#
# for j in range(len(a)):
#     print("Count={0}, Value={1}".format(j, a[j]))
#
# for k, item in enumerate(a, 1):
#     print("Count={0}, Value={1}".format(k, item))

# BREAK statements
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print('{0} equals {1} * {2}'.format(n, x, n//x))
#             break
#     else:
#         print(n, 'is a prime number')

# # CONTINUE statements
# for num in range(0, 10):
#     if num % 2 == 0:
#         print('Found an even number : {0}'.format(num))
#         continue
#     print('Found an odd number : {0}'.format(num))
#
# # PASS statements
# while True:
#     pass
#
# class MyEmptyClass:
#     pass
#
# FUNCTION statements
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

f = fib
f(2000)
print(f(0))

# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result
#
# f100 = fib2(100)
# print(f100)