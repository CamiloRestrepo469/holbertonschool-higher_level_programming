#!/usr/bin/python3
# for code in range(97, 123):
#     if code != 101 and code != 113:
#         print(chr(code), end='')

for i in range(97, 123):
    letra = chr(i)
    if letra.find('e') != -1:
        continue
    if letra.find('q') != -1:
        continue
    print(letra, end='')
