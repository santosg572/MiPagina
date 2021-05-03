#!/bin/bash

#folder="BBB_libros"
folder="MMM_libros"
#folder="PPP_libros"
#folder="RRR_libros"
pat="/Users/santosg/ubuntu20_Servidor_feb0621/LIBROS_TODOS_abr0121/"$folder

python3 crea_html_Direc2_pdf.py $pat $folder.html


