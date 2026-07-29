
import os
import sys

n = len(sys.argv)
if n > 1:
   os.system('ls -1R > ls1R.txt')
else:
   print('faltan algumentos')

