#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import remove
import shutil
import os.path as path
import os
import sys

ne = len(sys.argv)
print(ne)

if ne == 3:
 pat = sys.argv[1]
 file = sys.argv[2]

 filein = file.replace(' ','\ ')
 filein = filein.replace('(', '\(')
 filein = filein.replace(')', '\)')
 fileon = file.replace(' ', '')
 fileon = fileon.replace('(', '')
 fileon = fileon.replace(')', '')
 
 comando = 'mv ' + pat+filein + ' ' + pat+fileon
 print(comando)
 ss = os.system(comando)
 print(ss)
else:
 print('falta informacion: pat, filin, filon')





