#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import remove
import shutil
import os.path as path
import os
import sys

import funciones

if len(sys.argv) >  2:
   pat =  sys.argv[1]
   funciones.Saca_lista_direc(pat)
   file_in = "tempo.txt"
   file_out = sys.argv[2]

   funciones.Saca_lista_direc(pat)

   file_in = "tempo.txt"

   f = open(file_in, "r")
   arti = f.read()
   f.close()

   arti = arti.split('\n')

   fw = open(file_out, "a")

   fw.write("<html>"+'\n')
   fw.write("<head>"+'\n')
   fw.write("<title>  ARTICULOS </title>"+'\n')

   fw.write("</head>"+'\n')
   fw.write("<body>"+'\n')

   reg = 1
   for pal in arti:
      dpal = pat+pal
      w = str(reg)+' - <a href='+ dpal + '>'+pal+'</a>'
      fw.write(w)
      fw.write('<hr>')
      reg = reg+1

   fw.write("</body>"+'\n')
   fw.write("</html>"+'\n')

   fw.close()
else:
   print('ERROR')


