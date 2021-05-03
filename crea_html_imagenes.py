#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import remove
import shutil
import os.path as path
import os
import funciones
import sys

if len(sys.argv) >  2:
   pat =  sys.argv[1]
   funciones.Saca_lista_direc(pat)
   file_in = "tempo.txt"
   file_out = sys.argv[2]


   funciones.Saca_lista_direc(pat)
   funciones.Renombra_archivos(pat)


   fw = CreaFolder_Checa(file_out)

   f = open('tempo.txt', "r")
   dir = f.read()
   f.close()

   palabras = dir.split('\n')

   npal = len(palabras)

   fw.write("<html>"+'\n')
   fw.write("<head>"+'\n')
   fw.write("<title>  prueba </title>"+'\n')

   fw.write("</head>"+'\n')
   fw.write("<body>"+'\n')

   palabras.sort()

   print(palabras)

   for pal in palabras:
      dpal = pat+'/'+pal
      w = '<img src="' + dpal + '" width="90%">'+'\n'
      fw.write(w)

   fw.write("</body>"+'\n')
   fw.write("</html>"+'\n')

   fw.close()
else:
   print(' ERROR')


