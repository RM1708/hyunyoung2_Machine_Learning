#!/usr/bin/evn bash 

# Author: hyunyoung2(github id)
# This shell script is for nomarlizing wikimedia's korean language.
# This version is basic version from Fasttext's get-wikimedia.sh


DATE=$(date +%Y%m%d)

# The location of directory
ROOT="data/wikimedia/${DATE}"
NORMALIZATION="${ROOT}/normalization/${DATE}"

FILENAME=""

sed -e "s/’/'/g" -e "s/′/'/g" -e "s/''/ /g" -e "s/'/ ' /g" -e "s/“/\"/g" -e "s/”/\"/g" \
        -e 's/"/ " /g' -e 's/\./ \. /g' -e 's/<br \/>/ /g' -e 's/, / , /g' -e 's/(/ ( /g' -e 's/)/ ) /g' -e 's/\!/ \! /g' \
        -e 's/\?/ \? /g' -e 's/\;/ /g' -e 's/\:/ /g' -e 's/-/ - /g' -e 's/=/ /g' -e 's/=/ /g' -e 's/*/ /g' -e 's/|/ /g' \
        -e 's/«/ /g' $FILENAME | tr 0-9 " " 

