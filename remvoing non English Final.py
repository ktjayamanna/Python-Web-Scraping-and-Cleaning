# -*- coding: utf-8 -*-
"""
Description: This is the fifth step in our cleaning process: Cleaning non-eng
Created on Sat Mar  6 15:45:27 2021

@author: kjayamanna
"""
import json
import pycld2 as cld2
import matplotlib.pyplot as plt
import re

# =============================================================================
# isReliable: bool
#     True if the detection is high confidence.

# textBytesFound: int
#     Total number of bytes of text detected.

# details: tuple
#     Tuple of up to three detected languages, where each is
#     tuple is (languageName, languageCode, percent, score).  percent is
#     what percentage of the original text was detected as this language
#     and score is the confidence score for that language.

# vectors: tuple
#     Vectors indicating which language was detected in which byte range.
# =============================================================================
#%% Change the Json file name here.
with open('check4v4.json') as f:
    quotes1 = json.load(f); 
#%%
#This list keeps any article that has any language other than Eng.
#So, it could be just English + more languages or just non-English.
detectList = []
for i in range(len(quotes1)):
    try:
        article = quotes1[i]['Page_Article']
        isReliable, _, detected_language = cld2.detect(article,  returnVectors=False)
        for j in range(len(detected_language)):
            if(detected_language[j][0] != 'ENGLISH' and detected_language[j][0] != 'Unknown'):
                detectList.append((i,isReliable, detected_language))
                break;
    except:
        pass
    
#%%
#NonEnglish does not contain any English. This can be directly classified as
#to be deleted.
nonEngList = []
#Keep the JSON file's indices here.
nonEnglishIdx = []
flag = False
for detected_language in detectList:
    for j in detected_language[2]:
        if(j[0] == "ENGLISH"):
            flag = True
            break
    if (flag == False):
        nonEngList.append(detected_language)
        nonEnglishIdx.append(detected_language[0])
    flag = False
#%%
#Now, engList contains English + NonEnglish Articles.
engList = [i for i in detectList if i not in nonEngList]
#%% This make sure that there are no pure English articles here. 
#Not necessary
# flag = False
# pureEng = []
# for t in detectList:
#     for j in t[2]:
#         if(j[0] == "ENGLISH"):
#             flag = True
#         elif(j[0] != "Unknown"):
#             print(j[0])
#             flag = False
#             break
#     if(flag == True):
#         pureEng.append(t)
#     flag = False
#%%
#Filter out the Mixed articles with More than 50% of the article is English.
predomEng = []
for i in engList:
    for j in i[2]:
        if(j[0] == "ENGLISH" and j[2] > 50):
            predomEng.append(i)
# I manually inspected predomEng list and they don't contain any significant
# amount of Non-English. There's only a few articles that has a percentage between 50%-90%. So, it's safe to 
# keep them. Don't delete them.            
#And here we keep mixed articles with less than 50% of the article is English
checkMe = [i for i in engList if i not in predomEng]
#Keep the JSON file's indices here.
checkMeIdx = []
for i in checkMe:
    checkMeIdx.append(i[0])
#%% 
#Now get the percentage scores of mixed articles that have less than 50% English in it.
engLowPercentages = []
for m in checkMe:
    for p in m[2]:
        if(p[0] == "ENGLISH"):
            engLowPercentages.append(p[2])
#%%
#Plot it to see what is the percentage of the majority of the articles.
plt.figure()
plt.hist(engLowPercentages, bins=200)
#%% Pick a threshold and check all the articles in EngLowList manually.
engLowList = []
for m in checkMe:
    for p in m[2]:
        if(p[0] == "ENGLISH" and p[2] < 15):
            engLowList.append(m)
#%%
# =============================================================================
# It seems that the mixed language list called checkMe doesn't have valuable 
# English texts. So, following lists are determined to be deleted. 
# nonEngList, checkMe
# =============================================================================
#%%
for i in nonEnglishIdx:
    quotes1[i]["Page_Article"] = "Deleted because of Non-English"

for i in checkMeIdx:
    quotes1[i]["Page_Article"] = "Deleted because of Non-English"

#%% Write back to the JSON format
with open("check4v5.json", "w") as outfile:  
    json.dump(quotes1, outfile) 