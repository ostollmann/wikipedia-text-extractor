#!/bin/bash

set -e

n="0"
cat $1 | 
while read a; do
    n=$[$n+1]
    fn=$(basename $a)
    python wiki_extractor.py "$a" "wiki_text/$fn.txt"
done