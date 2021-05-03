import sys
from os import remove
import shutil
import os.path as path
import os
import funciones


if len(sys.argv) >  2:
   pat =  sys.argv[1]
   file_in = "tempo.txt"
   file_out = sys.argv[2]
   file_in = "tempo.txt"
   file_out = file_out+'.html'
   
   fw = funciones.CreaFolder_Checa(file_out)

   funciones.Saca_lista_direc(pat)
   funciones.Renombra_archivos(pat)

   f = open(file_in, "r")
   dir = f.read()
   f.close()

   palabras = dir.split('\n')

   npal = len(palabras)

   fw.write("<html>"+'\n')
   fw.write("<head>"+'\n')
   fw.write("<title>  prueba </title>"+'\n')

   fw.write("</head>"+'\n')
   fw.write("<body>"+'\n')

   i = 0

   print(npal)
   while i < npal:
      pal = palabras[i]
      lp = len(pal)
      cc = pal[0:1]
      if cc == '/':
         pat = pal[0:(lp-1)]
         break
      else:
         i = i+1

   print(i)
   if (i == npal):
      i=0
   k = 1
   while i < npal:
      pal = palabras[i]
      lp = len(pal)
      cc = pal[0:1]
      if cc == '/':
         pat = pal[0:(lp-1)]
         print('pat:'+pat)
      else:
         if lp > 0:
            w = pat+'/'+pal
            print(w+'\n')
            w2 = str(k)+' --- ' +'<a href=' + w + '>'+ pal + '</a>'
            k = k+1
            fw.write(w2+'\n')
            fw.write('<p> -- </p>')
      i = i+1

   fw.write("</body>"+'\n')
   fw.write("</html>"+'\n')

   fw.close()
else:
   print('ERROR')

