final answer:
so the output json files froutput.json--france,deoutput.json--Germany,itoutput.json -italy,esoutput.json--spain
total data available after scraping are 46+41+5+2  = 94 json objects which are titles as of now

How i arrived at this?
Answer:

GIVEN
relu
https://www.amazon.%7Bcountry%7D/dp/%7Basin%7D
"https://www.amazon.{country}/dp/{asin}"

https://www.amazon.com/dp/{asin}
000101742X --valid


since
ASIN stands for Amazon Standard Identification Number and is a unique set of 10 digit numbers assigned to every Amazon item.

MY APPROACH

connected the given spreadsheet to phpmyadmin mysql - 7:00 AM

got the distinct country codes as
query

select distinct country from reluwork;
fr --france   --46
de --germany  --41
it -- italy    --5
es -- spain     --2

DATA CLEANING

SELECT DISTINCT(Asin) ,country FROM `reluwork` WHERE LENGTH(Asin)=10 and country='de' ;
this returned 41 rows

SELECT DISTINCT(Asin) ,country FROM `reluwork` WHERE LENGTH(Asin)=10 and country='it' ;
this returned 5 rows


SELECT DISTINCT(Asin) ,country FROM `reluwork` WHERE LENGTH(Asin)=10 and country='es' ;
this returned 2 rows


SELECT DISTINCT(Asin) ,country FROM `reluwork` WHERE LENGTH(Asin)=10 and country='fr' ;
this returned 46 rows

exported all the above results to json format as it.json(itlay),de.json(germany),fr.json(france),es.json(spain)

pip install scrapy
scrapy startproject yashas
cd yashas
scrapy genspider amazon amazon.com

Here the main logic is available at spiders --> 
scraping italy items only titles

scrapy crawl amazon -o itoutput.json
starttime -- 2022-07-22 22:31:23
endtime  -- 2022-07-22 22:32:17

after changing country code respectively
scrapy crawl amazon -o froutput.json
starttime -- 23:17:26
endtime -- 23:20:39

scrapy crawl amazon -o deoutput.json
starttime -- 23:33:03
endtime -- 23:33:52

scrapy crawl amazon -o esoutput.json
starttime -- 23:41:31
endtime -- 23:42:27

so the output json files froutput.json--france,deoutput.json--Germany,itoutput.json -italy,esoutput.json--spain
total data available after scraping are 46+41+5+2  = 94 json objects which are titles as of now

reason for late submission college 6th semester final exam ongoing and will end on August-19-2022 

but happy about getting to use scrapy 
i will try to work on this and im willing to improve my skills
