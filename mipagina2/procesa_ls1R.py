# ls -1R /Users/santosg/ubuntu20_Servidor_feb0621/LIBROS_TODOS_mar2021/PPP_libros > ls1R.txt

from os import remove
import shutil
import os.path as path
import os

prefijo = 'AAA_libros'
file_in = "ls1R.txt"
file_out = prefijo+'.html'

PAT='/Users/santosg/ubuntu20_Servidor_feb0621/LIBROS_TODOS_mar2021/AAA_libros/'
PAT=''

if (path.exists(file_out)):
   remove(file_out)

f = open(file_in, "r")
dir = f.read()
f.close()

print(type(dir))

palabras = dir.split('\n')
print(palabras)
print(type(palabras))

npal = len(palabras)

fw = open(file_out, "a")

fw.write("<html>"+'\n')
fw.write("<head>"+'\n')
fw.write("<title>  prueba </title>"+'\n')

fw.write("</head>"+'\n')
fw.write("<body>"+'\n')

i = 0

while i < npal:
   pal = palabras[i]
   lp = len(pal)
   cc = pal[0:1]
   if cc == '/':
      pat = pal[0:(lp-1)]
      break
   else:
      i = i+1

print('pat:'+pat)

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
         w2 = str(k)+' --- ' +'<a href=' + PAT + w + '>'+ pal + '</a>'
         k = k+1
         fw.write(w2+'\n')
         fw.write('<p> -- </p>')
   i = i+1

fw.write("</body>"+'\n')
fw.write("</html>"+'\n')

fw.close()

#pat = '/Volumes/VOL01/'+file_out

#shutil.move(file_out, pat)
