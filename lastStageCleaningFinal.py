# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:08:23 2021

@author: kjayamanna
Description: Further cleaning.(This is the last stage, any website specific problems will be solved here.)
"""
import json
import pycld2 as cld2
import matplotlib.pyplot as plt
import re

#%% Change the Json file name here.
with open('check4v5.json') as f:
    quotes1 = json.load(f); 
#%%
tempList = []
pattern1 = 'Subscribe to The Defender - It’s Free!'
pattern2 = 'validation purposes and should be left unchanged.'
pattern3 = '\*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS\.'
pattern4 = 'Placeholders.enable\(\);'
pattern5 = '<p>Suggest a Correction</p>'
for j in range(len(quotes1)):
    quotes1[j]['Page_Article'] = re.sub(pattern3, "", quotes1[j]['Page_Article'])
    quotes1[j]['Page_Article'] = re.sub(pattern4, "", quotes1[j]['Page_Article'])
    quotes1[j]['Page_Article'] = re.sub(pattern5, "", quotes1[j]['Page_Article'])
    article = quotes1[j]['Page_Article']
    size = len([m.start() for m in re.finditer(pattern1, article)])
    for a in range(size):
        article = quotes1[j]['Page_Article']
        pat1 = article.find(pattern1)
        pat2 = article.find(pattern2)
        if(pat1 != -1):
            tempList.append((j, pat1,pat2))
            quotes1[j]['Page_Article'] = quotes1[j]['Page_Article'].replace(article[pat1:pat2+len(pattern2)],"")

        

#%% Write back to the JSON format
with open("check4v6.json", "w") as outfile:  
    json.dump(quotes1, outfile) 