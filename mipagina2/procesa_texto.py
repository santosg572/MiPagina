#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import remove
import shutil
import os.path as path
import os
import sys

for elements in sys.argv:
    print(elements)

file_in = 'texto.txt'

f = open(file_in, "r")
palabras = f.read()
f.close()

#print(type(dir))

palabras = palabras.replace('\n', ' ')
palabras = palabras.split(' ')

#print(palabras)
#print(type(palabras))

conjunto = set(palabras)

#print(conjunto)

lis_con = list(conjunto)
lis_con.sort()
print(lis_con)


na = len(sys.argv)
print(na)

for i in range(1,na):
    pal = sys.argv[i]
    nc = palabras.count(pal)
    print(pal+str(nc))
    for j in range(nc):
       inde = palabras.index(pal)
       print(palabras[inde-1:inde+2])



