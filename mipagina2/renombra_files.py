#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import remove
import shutil
import os.path as path
import os
import sys
import funciones

for elements in sys.argv:
    print(elements)

direc = '/Users/santosg/Desktop/Libro_biblio_unam/'

ss = os.system('ls -1R ' + direc + ' > temporal.txt')

f = open('temporal.txt', "r")
palabras = f.read()
f.close()

#print(type(dir))

palabras = palabras.split('\n')

print(palabras)
print(type(palabras))

for file in palabras:
  print(file)
  funciones.renombra_archivo(direc,file)



