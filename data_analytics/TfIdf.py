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

main(inp)