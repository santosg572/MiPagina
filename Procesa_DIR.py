import os
import subprocess

pat='/Volumes/PASCAL/LIBROS_TODOS_mar2021_N/'
res = subprocess.check_output(['ls', pat])
res = str(res)
print(res)
res = res.replace('\n', ' ')
print(type(res))
print(res)

#os.system('python3 ./crea_html_dir.py /Users/santosg/Desktop/Libros_sep0320 Libros_sep0320.html')

