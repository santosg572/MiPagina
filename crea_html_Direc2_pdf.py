from os import remove
import shutil
import os.path as path
import os
import sys
import funciones

print(len(sys.argv))

if len(sys.argv) >  2:
   pat =  sys.argv[1]
   funciones.Saca_lista_direc(pat)
   file_in = "tempo.txt"
   file_out = sys.argv[2]


   if (path.exists(file_out)):
      remove(file_out)

   f = open(file_in, "r")
   dir = f.read()
   f.close()

   palabras = dir.split('\n')

   npal = len(palabras)
   n=1
   for pal in palabras:
      if len(pal) > 0:
         dd = pal[0] 
         if dd == '/':
            break
         else:
            n = n+1

   fw = open(file_out, "a")

   fw.write("<html>"+'\n')
   fw.write("<head>"+'\n')
   fw.write("<title>  prueba </title>"+'\n')

   fw.write("</head>"+'\n')
   fw.write("<body>"+'\n')

   pat = pal[0:len(pal)-1]+'/'
   print(pat)
   k = 1
   for i in range(n+1, len(palabras)):
      pal = palabras[i]
      if len(pal) > 1:
         if pal[0] == '/':
            pat = pal[0:len(pal)-1] + '/'
            print(pat)
         else:
            dpal = pat + pal
            if not(os.path.isdir(dpal)):
               w = dpal 
               w2 = str(k)+' --- ' +'<a href=' + dpal + '>'+ pal + '</a>'
               k = k+1
               fw.write(w2)
               fw.write('<hr>')

   fw.write("</body>"+'\n')
   fw.write("</html>"+'\n')

   fw.close()

else:
   print('error')
   print(''' Este corre como:
             python3 crea_html_Direc2_pdf.py pat dileout''')


