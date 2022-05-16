# -*- coding: utf-8 -*-
"""
Description: This is the second stage of the cleaning process.
Created on Tue Feb  2 09:59:09 2021
@author: ktjayamanna
"""
#%%
import re
import json
import hashlib
import matplotlib.pyplot as plt
import statistics as st
import numpy as np
#%%
plt.close('all')
#%% Change the Json file name here.
with open('check4v1.json') as f:
    quotes1 = json.load(f);

#%% This pattern helps us to narrow down the dirty articles
rogueArticles = []
pattern1 = re.compile(r'[\{\}]')
#%% Append all the dirty articles into rogueArticle list
for i in range(len(quotes1)):
    j = quotes1[i]['Page_Article']
    if(len(re.findall(pattern1, j)) > 0 and i not in rogueArticles):
        rogueArticles.append(i)
              
#%% 
# =============================================================================
# Here we breakdown every article into it's smallest form; newline seperated isles.
# This helps us identify more specifically where the code snippets are located.
# And also it's easier to get rid of them.
# =============================================================================
tools = ['{', '}', ';:', 'jQuery', 'JQuery', '/*', '*/', '.replace', '=']
snippets = []
for i in range(len(rogueArticles)):
    temp = quotes1[rogueArticles[i]]['Page_Article'].split('\n')
    for k in temp:
        #Filter out the good stuff inside paragraph breaks
        if (len(k)> 0 and k.find("p>") == -1):
            for l in tools:
                if((l in k) and (k not in snippets)):
                    snippets.append(k)
#%%
#replacements keeps all the cleaned articles just in case if we need to check. 
replacements = []
for i in rogueArticles:
    temp2 = quotes1[i]['Page_Article']
    for j in snippets:
     temp2 = temp2.replace(j, "")   
    quotes1[i]['Page_Article'] = temp2
    replacements.append(temp2)  
#%% 
# =============================================================================
# Need to search again to locate the remaining snippets that weren't caught before.
# This time, we'll delete the entire article, 
# because their content has less value (boilerplate).
# =============================================================================
postSubCheck = []   
#%% we'll throw away 43 articles
for i in range(len(quotes1)):
    j = quotes1[i]['Page_Article']
    if(len(re.findall(pattern1, j)) > 0 and i not in postSubCheck):
        quotes1[i]['Page_Article'] = 'Content was Deleted by Kaveen Jayamanna due to massive amount of Code Snippets and Boilerplate'
        postSubCheck.append(i)

#%% Write back to the JSON format
with open("check4v2.json", "w") as outfile:  
    json.dump(quotes1, outfile) 
                    


        

        
    

    
