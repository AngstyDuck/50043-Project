import pyspark
import numpy as np
from pyspark.sql import Row
from pyspark.sql import SQLContext
from pyspark import SparkConf, SparkContext, SparkFiles
from pyspark.sql.functions import *
from pprint import pprint

conf = SparkConf().setAppName("Analysis").set("spark.executor.heartbeatInterval$

sc = SparkContext.getOrCreate(conf)
sqlContext = SQLContext(sc)

sql_df = sqlContext.read.csv("/input/mysql.csv", header=False, inferSchema=True$
mongo_df = sqlContext.read.json("/input/mongo.json")

# SQL PROCESSING

'''
sql_asin = [(asin, len(review), review(str))]
sql_dict_len = {asin: int(total string length)}
sql_dict_review = {asin: [review1, review2, review3 ....]}
'''


sql_asin = sql_df.rdd.map(lambda x: (x[0], len(x[1]), x[1])).take(sql_df.count())

sql_dict_len = dict()

for i in sql_asin:
    sql_dict_len[i[0]] = []
    sql_dict_review[i[0]] = []

for i in sql_asin:
    sql_dict_len[i[0]].append(i[1])
    sql_dict_review[i[0]].append(i[2])

for i in sql_dict_len:
    sql_dict_len[i] = np.sum(sql_dict_len[i])

# END OF SQL PROCESSING

# MONGO PROCESSING

'''
mongo_asin = [(asin, price),....]
'''

mongo_asin = mongo_df.rdd.map(lambda x : (x[0], x[1])).take(mongo_df.count())

mongo_dict_price = {tup[0]: tup[1] for tup in mongo_asin}


#END OF MONGO PROCESSING

import copy

sql_dict_len_zero = copy.copy(sql_dict_len)

for i in mongo_dict_price:
    if i not in sql_dict_len_zero:
        sql_dict_len_zero[i] = 0

for i in sql_dict_len_zero:
    if i not in mongo_dict_price:
        mongo_dict_price[i] = 0.0

len_as_zero , len_as_none, price_as_zero, price_as_none = [],[],[],[]


for i in sql_dict_len_zero:
    len_as_zero.append(sql_dict_len_zero[i])
    price_as_zero.append(mongo_dict_price[i])

import math

# CALCULATING PEARSON CORRELATION
print('STARTING PEARSON CORRELATION CALCULATIONS')

x = len_as_zero
rddX = sc.parallelize(x)

xBar = rddX.reduce(lambda a,b: a+b)/len(x)

y = price_as_zero
rddy = sc.parallelize(y)


# (x-mean of x), (y-mean of y)
term1 = rddX.map(lambda a: a-xBar)
term2 = rddy.map(lambda a: a-yBar)

term1Sq = rddX.map(lambda a: (a-xBar)**2)
term2Sq = rddy.map(lambda a: (a-yBar)**2)

term1_arr = np.array(term1.collect())
term2_arr = np.array(term2.collect())

xy = np.multiply(term1_arr, term2_arr)

ddXY = sc.parallelize(xy)

numerator = rddXY.reduce(lambda a,b: a+b)

sumTerm1Sq = term1Sq.reduce(lambda a,b:a+b)

sumTerm2Sq = term2Sq.reduce(lambda a,b:a+b)


denominator = math.sqrt(sumTerm1Sq*sumTerm2Sq)

result = (numerator/denominator)
with open("pearson.txt", "w") as text_file:
    text_file.write(f'Pearson Coefficient Result = {result}')
print(f'Pearson Coefficent Result = {result}')
print(f'FINISHED CALCULATING PEARSON COEFFICIENT')
#END OF PEARSON COEFFICIENT CALCULATIONS

# CALCULATIONS OF TF-IDF
print('STARTING TF-IDF CALCULATIONS')


import math

inp = docList

def computeTF(wordDict, bow):
    tfDict ={}
    bowCount = len(bow)
    for word , count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return(tfDict)

def computeIDF(docList):
    idfDict={}
    N= len(docList)
    #idfDict = dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word,val in doc.items():
            if word not in idfDict.keys():
                idfDict[word] = 1
            else:
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word]= math.log10(N/ float(val))

    return(idfDict)

def computeTFIDF(tfBow,idfs):
    tfidf={}
    for word,val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return(tfidf)

def termCount(review):
    wordDict={}
    ls = review.split(" ")
    for i in ls:
        i = i.strip(".,:"+'"').lower()
        if i not in wordDict.keys():
            wordDict[i]=1
        else:
            wordDict[i]+=1
    return(wordDict)

def main(docList):
    dictls=[]
    for doc in docList:
        wordDict = termCount(doc)
        tf = computeTF(wordDict,doc)
        dictls.append(tf)
    idf = computeIDF(dictls)

    dic = {}
    for i in range(len(dictls)):
        dic[i] = computeTFIDF(dictls[i],idf)

    return(dic)

# MAPPING AND REDUCING FOR TFIDF

review = sc.parallelize([sql_dict_review[i] for i in sql_dict_review], numSlice$
tfidf = review.map(main)

tfidf_result = tfidf.collect()
print('Writing to tfidf.txt')
with open("tfidf.txt", "w") as text_file:
    text_file.write(tfidf_result)
pprint(tfidf_result)

print('FINISHED CALCULATING TF-IDF')
