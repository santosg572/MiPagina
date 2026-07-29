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


   if (path.exists(file_out)):
      remove(file_out)

   f = open(file_in, "r")
   dir = f.read()
   f.close()


   palabras = dir.split('\n')

   npal = len(palabras)

   fw = open(file_out, "a")

   fw.write("<html>"+'\n')
   fw.write("<head>"+'\n')
   fw.write("<title>  prueba </title>"+'\n')

   fw.write("</head>"+'\n')
   fw.write("<body>"+'\n')

   k=1
   
   for pal in palabras:
      if len(pal) > 0:
         dd = pal[0] 
#         print('pal - '+pal)
         if dd == '/':
            np = len(pal)
            pat = pal[:(np-1)]
#            print('pat new - ', pat)
            w = '<p>' +  pat  + '</p>'+'\n'
            fw.write(w)
         else:
            file = pat+'/'+pal
            nf = len(file)
            pref = file[nf-3:]
#            print('pef - '+pref)
 #           print('file - '+file)
            if pref in ['pdf', 'PDF']:
               w2 = str(k)+' --- ' +'<a href=' + file + '>'+ pal[1:] + '</a>'
               k = k+1
               fw.write(w2)
               fw.write('<hr>')
            elif pref in ['png', 'PNG', 'jpg', 'JPG']:
               w = '<img src="' + file + '" width="90%">'+'\n'
               fw.write(w)
            else:
               print('pef - '+pref)
               print('xxx - ', file)


   fw.write("</body>"+'\n')
   fw.write("</html>"+'\n')

   fw.close()
else:
 

   pat0 = pal[0:len(pal)-1]
   pat = pat0 + '/'
   print(pat)

   for i in range(n+1, len(palabras)):
      pal = palabras[i]
      if len(pal) > 1:
         if pal[0] == '/':
            pat0 = pal[0:len(pal)-1]
            pat = pat0 + '/'
            print(pat)
         else:
            dpal = pat + pal
            if not(os.path.isdir(dpal)) and not(pat0 in patno):
               w = '<p>' +  dpal + '</p>'+'\n'
               fw.write(w)


#   pat = '/Volumes/VOL01/'+file_out

#   shutil.move(file_out, pat)
#else:
   print('error')
   print('''
         Se corre de la siguiente manera:

         python3 crea_html_dir.py pat fileout
''')

