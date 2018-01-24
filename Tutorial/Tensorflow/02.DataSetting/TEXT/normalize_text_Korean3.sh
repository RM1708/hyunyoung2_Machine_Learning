#!/usr/bin/env bash 


# Author: hyunyoung2(github id)
# This shell script is for nomarlizing wikimedia's korean language.
# This version is basic version from Fasttext's get-wikimedia.sh
# This normalization mean removing a phrase beginning with "(" and endig with ")".

DATE=$(date +%Y%m%d)

# The location of directory
ROOT="data/wikimedia/${DATE}"
NORMALIZATION="${ROOT}/normalization/${DATE}"

FILENAME="wiki_00_09"
# \#

sed -e "s/‘/'/g" -e "s/’/'/g" -e "s/′/'/g" -e "s/“/\"/g" -e "s/”/\"/g" -e "s/\`/ \` /g" \
    -e 's/([^)]*)//g' \
    -e 's/, ,/,/g' -e 's/(,/(/g' -e 's/( ,/(/g' -e 's/,)/)/g' -e 's/, )/)/g' -e 's/(=/(/g' -e 's/=)/)/g' \
    -e 's/( )//g' -e 's/()//g' -e 's/(/ ( /g' -e 's/)/ ) /g' \
    -e "s/''//g" -e 's/""//g' -e "s/'//g " -e 's/"//g' \
    -e 's/\. / \. /g' -e 's/다\./다 \. /g' -e 's/오\./오 \. /g' -e 's/, / , /g' -e 's/…/ … /g' -e 's/·/ · /g' -e 's/•/ • /g' \
    -e 's/\-\-/ \-\- /g' -e 's/-/ - /g' -e 's/=/ = /g' -e 's/\;/ \; /g' -e 's/\:/ \: /g' \
    -e 's/\!/ \! /g' -e 's/\?/ \? /g' -e 's/*/ /g' -e 's/|/ /g' -e 's/\// \/ /g' \
    -e 's/<br \/>/ /g' \
    -e 's/«//g' -e 's/»//g' -e 's/\《//g' -e 's/\》//g' -e 's/\[//g' -e 's/\]//g' -e 's/ </ /g' -e 's/>//g' \
    -e 's/≪//g' -e 's/≫//g' -e 's/『//g' -e 's/』//g' -e 's/〈//g' -e 's/〉//g' $FILENAME > wiki_00_09_normalized_with_regular_expression

#    -e 's/«/ « /g' -e 's/»/ » /g' -e 's/《/ 《  /g' -e '/》/ 《  /g' $FILENAME > only_wiki_00_normalized 
