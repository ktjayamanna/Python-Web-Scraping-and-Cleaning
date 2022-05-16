# -*- coding: utf-8 -*-
"""
Description: This is the sixth step of the cleaning process.
Created on Wed Dec 23 22:26:23 2020
@author: kjayamanna
"""
import json
import re
#%% Change the Json file name here.
with open('check6v4.json') as f:
    quotes1 = json.load(f);
#%% Open the JSON file called "comprehensiveDictionary.json" to make a list of characters we wish to replace.
with open('comprehensiveDictionary.json') as f:
    referenceList = json.load(f);
#%%
for i in range(len(quotes1)):
    checkArticle = quotes1[i]["Page_Article"]   
#%
    for c in range(len(referenceList)):
        checkArticle = re.sub(referenceList[c][0], referenceList[c][1], checkArticle)
        quotes1[i]["Page_Article"] = checkArticle

#%% Write it back to a JSON file.
with open("check6v5.json", "w") as outfile:
    json.dump(quotes1, outfile)
    

            
    








