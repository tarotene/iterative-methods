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

# execute
if [[ -f ./res/$1-result.txt ]]; then
  rm ./res/$1-result.txt
fi
./bin/$1 > ./res/$1-result.txt