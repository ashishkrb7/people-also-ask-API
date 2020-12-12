
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "./..")).replace("\\","/")

# import libraries
import pandas as pd
import numpy as np
import json
import string
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
from nltk.tokenize import sent_tokenize

config=json.load(open(path+"/src/config.json","r"))

# methods
def sent_token(data):
    """ tokenize the sentenses and put word limit restriction """
    x=sent_tokenize(data)
    y=[x[i] for i in range(len(x)) if len(x[i].split()) > config["WordRestriction"]]
    return y

def create_tokenizer_score(train,test):
    """ Function to create the  """
    tokenizer = TfidfVectorizer(ngram_range=(1,config["ngramLimit"]))
    train_tfidf = tokenizer.fit_transform(train)
    new_tfidf = tokenizer.transform(test)
    X = pd.DataFrame(cosine_similarity(new_tfidf, train_tfidf), columns=train.index)
    score = pd.melt(X,value_name='score') 
    return score

def find_score(train,test): 
    """ To classify the sentense based on threshold """ 
    y=create_tokenizer_score(train,test).score.max()    # score
    if (y>=config["threshold"]):
        x=True 
    else:
        x=False 
    return x,y

def remove_punctuation(s):
    """ Remove punctuation from sentence """
    return ''.join([i for i in s if i not in frozenset(string.punctuation)])

def  loadmodel(filename="Commitment"):
    """ To load the list"""
    pickle.load(open(path+"/model/"+filename+".pkl", 'rb'))

def dumptrain(train,filename):
    """ To pickle the list """
    pickle.dump(train,open(path+"/model/"+filename+'.pkl',"wb"))

def main (df,filename="Commitment"):
    """ main method to process the incore data and publish the result"""
    train=pd.Series(pickle.load(open(path+"/model/"+filename+".pkl","rb")))
    df=df[["_id","textBody"]]
    df.textBody=df.textBody.apply(lambda x:remove_punctuation(x))
    df[["result","score"]]=df.apply(lambda x:find_score(train,[x.textBody]),axis=1, result_type="expand")
    return df.to_json(orient="records")

