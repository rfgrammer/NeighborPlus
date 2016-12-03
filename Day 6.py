#
# hello = 'hello, world\n'
#
# hellos = repr(hello)
# print('hello: ', hello)
# print('hellos:', hellos)
#
#
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end='')
#     print(repr(x*x*x).rjust(4))
#
# for x in range(1, 11):
#     print('{0:2d}{1:3d}{2:4d}'.format(x, x*x, x*x*x))
#
# print()
# print('12'.zfill(5))
#
#
# print('first : {0}, second: {1}'.format('first', 'second'))

filename = 'workfile'
f = open(filename, 'w')
f.writelines('This is the first string...\n')
f.writelines('This is the second string...\n')
f.close()

f = open(filename, 'r')
# print(f.readlines())
# f.close()

# for line in f:
#     print(line)

print(list(f))


with open(filename, 'r') as f:
    read_data = f.read()

import json
f = open('json', 'r')
fw = open('mytext.txt', 'w')
json.dump(f, fw)

