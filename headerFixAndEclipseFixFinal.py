# -*- coding: utf-8 -*-
"""
Description: This the first step of the cleaning process.
Created on Sat Mar  6 11:04:58 2021

@author: kjayamanna
"""
import json
import re
import truecase
#%% Change the Json file name here.
with open('check4.json') as f:
    quotes1 = json.load(f);

for index in range(len(quotes1)):
    article = quotes1[index]['Page_Article']
    # %% Fix the Headers
    tools = [".", "!", "…", "\\", "?", "”", ")", "}", "{",">", ";", ":", "»", "0", "1", "2", "3", "4","5","6","7","8","9"]
    ends = []
    headerListCleaned = []
    headerList = []
    splitArticle = article.split("\n ")
    # Fix the case of the words
    for i in splitArticle:
        if(len(i.strip())>0):
            if ((len(i) < 250)) and ((i.strip()[-1]) not in tools) and (not (i.isspace())):
                ends.append(i[-1])
                headerList.append(i)
                headerListCleaned.append(truecase.get_true_case(i))
    # Replace the updated headers
    for i in headerList:
        article = article.replace(i, headerListCleaned[headerList.index(i)] + ": ")
    #%%
    # Fix the eclipses
    substitution = " "
    pattern1 = re.compile(r"…\.")
    substitution = pattern1.sub(r'.... ', article)
    
    pattern2 = re.compile(r'…\s')
    substitution = pattern2.sub(r'...', substitution)
    
    pattern3 = re.compile(r'. . . . ')
    substitution = pattern3.sub(r'.... ', substitution)

    pattern4 = '…'
    substitution = re.sub(pattern4,r'...', substitution)
    #Restore the article
    quotes1[index]['Page_Article'] = substitution

#%% Write back to the JSON format
with open("check4v1.json", "w") as outfile:  
    json.dump(quotes1, outfile) 

