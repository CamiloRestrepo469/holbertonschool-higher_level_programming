#!/usr/bin/python3
for i in range(97, 123):
    letra = chr(i)
    if letra.find('e') != -1:
        continue
    if letra.find('q') != -1:
        continue
    print(letra, end='')
