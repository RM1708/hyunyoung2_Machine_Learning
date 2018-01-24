# TEXT 

In here, I will deal with how to get text for Machine learning using wikipedia. 

In Particular,about wikipedia text of Korean. 

## TOC

 01. [wikimedia extractor](https://github.com/hyunyoung2/hyunyoung2_Machine_Learning/blob/master/Tutorial/Tensorflow/02.DataSetting/TEXT/01.Wikimedia_Extractor.ipynb)


## FILE 

 Normalize_text_\*\*\*.sh mean normalizing text 

### How to Download wikipedia 

 First, run get-wikipedia.sh
 
```shell
# hyunyoung2 @ hyunyoung2-desktop in ~/the-path-of-git-clone on git:master o [14:16:18] 
$ ./get-wikimedia.sh 
```

 This command contains git clone of [wikiextractor](https://github.com/attardi/wikiextractor)
 
 After the running of the command, you have to choose format you want, it is plaintext or json:

```shell
.......
git clont wikiextractor is saved indata/wikimedia/20180124/parsing

data/wikimedia/20180124/raw_wiki
Choose what type of text(e.g. j: json, p: plaintext(basic setting of wikiextrator), etc.): 
```

When you get message above, you have to choose p(plaintext) or j(json), if json, press j(lower letter), if not press p(lower letter)

 In the case of **plaintext**
 
```
 <doc id="" revid="" url="" title="">
        ...
        </doc>
```
 
  In the case of **json** 
  
```
{"id": "", "revid": "", "url":"", "title": "", "text": "..."}
```

the location of each file. 

plaintext:

> data/wikimeia/DATE(when you download the wikimedia)/raw_wiki/plaintxt

json

> data/wikimeia/DATE(when you download the wikimedia)/raw_wiki/json

According to [wikiextractor](https://github.com/attardi/wikiextractor), the resulting files such as plaintext or json is divided into around 100M bytes.


# Reference

