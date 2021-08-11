#!/bin/bash

search_extension=".py"
for py_file in  main_*.py
do
  echo $py_file
  #python $py_file >> $py_file.txt
  f=${py_file%$search_extension*}
  python $py_file >> $f.txt
  echo $f.txt
done
