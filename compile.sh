#!/bin/bash
set -Ceuo pipefail

# error handle
if [[ $# == 0 ]]; then
  echo -e "missing project name; e.g \"001-Jacobi\", ..."
  exit 10
elif [[ ! -f ./src/$1.cpp ]]; then
  echo -e "project \"$1\" does not exist; please check the directory ./src/..."
  exit 11  
fi

# compile
g++ -c ./include/iter.cpp -o ./include/iter.o
g++ -c ./src/$1.cpp -o ./src/$1.o -fopenmp
g++ -o ./bin/$1 ./src/$1.o ./include/iter.o -fopenmp