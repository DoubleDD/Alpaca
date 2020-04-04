#!/bin/bash

source_file=$1
target_file=$2

python -m PyQt5.uic.pyuic $source_file -o $target_file
