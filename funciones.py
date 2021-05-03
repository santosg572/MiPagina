from os import remove
import shutil
import os.path as path
import os
import sys

def CreaFolder_Checa(file=''):
   if (path.exists(file)):
      remove(file)
   fw = open(file, "w")
   return fw


def renombra_archivo(pat='', file=''):

   filein = file.replace(' ','\ ')
   filein = filein.replace('(', '\(')
   filein = filein.replace(')', '\)')
   fileon = file.replace(' ', '')
   fileon = fileon.replace('(', '')
   fileon = fileon.replace(')', '')
 
   comando = 'mv ' + pat+'/'+filein + ' ' + pat+'/'+fileon
#   print(comando)
   ss = os.system(comando)
   if not (os.path.isfile(pat+filein) * os.path.isfile(pat+fileon)):
      os.system('rm '+ pat+filein)



def Saca_lista_direc(pat=''):
   import os
   os.system('ls -1R '+ pat + ' > tempo.txt')


def Renombra_archivos(pat=''):
   f = open('tempo.txt', "r")
   palabras = f.read()
   f.close()

   palabras = palabras.split('\n')


   for file in palabras:
     renombra_archivo(pat,file)





