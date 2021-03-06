# -*- coding: utf-8 -*-
"""
Description: This is the Third Step of our cleaning process.
Created on Mon Jan 25 22:55:51 2021

@author: kaveen
"""
import json
import hashlib
import matplotlib.pyplot as plt
#%%
plt.close('all')
#%% Change the Json file name here.
with open('check4v2.json') as f:
    quotes1 = json.load(f);    
#%%
#This keeps all the potential boiler texts in the top of an article.
boiler = []
#This keeps all the md5 checksums of the text isles.
md5 = []
#This limits how many text isles we consider. (In this case, it's top 3)
topThreshold = 3
# We only delete the strings that surpass (repeatThreshold +1) amount.
#So, in this case if a string appears more than 22 times throughout the json
#file, we delete that string.
repeatThreshold = 21

#%%
for i in range (len(quotes1)):
    #This counts how many text isles the algo has found so far...
    topCount = 0
    #Temperarily break the article into text isles.
    lineBreakers = quotes1[i]['Page_Article'].split('\n')
    for j in range(0,len(lineBreakers)):
        #Take the checksum
        tempcheck = hashlib.md5(lineBreakers[j].rstrip().strip().encode('UTF-8')).hexdigest()
        if(len(lineBreakers[j].rstrip().strip()) > 0):
            topCount = topCount + 1
            if(tempcheck not in md5 ):
                #Append to the checksum list in the very first 
                # time you run into a text isle.
                md5.append(tempcheck)
                #Break if topThreshold exceeds.
                if(topCount >= topThreshold ):
                    break
            else:
                #if the string is already in the checksum list, add it to the 
                #potential boilerplate list.
                boiler.append(lineBreakers[j])
                #Break if topThreshold exceeds.
                if(topCount >= topThreshold ):
                    break
            
#%% This section is only for graphing purposes.
# This list keeps the frequency of each element in the potential boiler plate list.
freq = []
# This is a dictionary that keeps both boilerplate and the frequency at the 
# same place. This is not a essential variable. Just for convinience. 
repeats = {}
# Keeps all the unique boilerplate texts. 
# This is not a essential variable. Just for convinience. 
uniques = []
for i in boiler:
    if(i not in uniques):
        uniques.append(i)
        repeats[i] = boiler.count(i)
    freq.append(boiler.count(i))
#%% Filter out the low frequency strings.
# This keeps all the high Frequency Strings.
filteredFreq = []
for i in range(len(boiler)):
    if(freq[i] > repeatThreshold):
        # repeats[boiler[i]] = freq[i]
        filteredFreq.append(boiler[i])
#%% The Original Graph
plt.figure()
plt.hist(repeats.values(), bins=200)
plt.title("Histogram for Boilerplate Extraction in the Top 3 text Isles")
plt.xlabel("How many times a Unique String Showed up in Check3 (Frequency)")
plt.ylabel("How Common the Frequency is ")
#%% A Zoomed in Version
plt.figure()
plt.hist(repeats.values(), bins=200)
plt.title("Histogram for Boilerplate Extraction in the Top 3 text Isles(Zoomed In) ")
plt.xlabel("How many times a Unique String Showed up in Check3 (Frequency)")
plt.xlim(0,100)
plt.ylabel("How Common the Frequency is ")
plt.ylim(0,80)
#%% 
# =============================================================================
# Decide the parameters from the graphs above. 
# Then make the final list that includes boilerplate texts to be deleted.
# =============================================================================
#%%
#This list includes the final boilerplate texts.
finalBoilerPlate = []
#If you need to keep any high frequency strings which will be deleted, 
#put them here.
excludeList = ['Content was Deleted by Kaveen Jayamanna due to massive amount of Code Snippets and Boilerplate']
for i in filteredFreq:
    if(i not in excludeList and i not in finalBoilerPlate):
        finalBoilerPlate.append(i)
        
#%% Find and replace Boilerplate in the JSON file.
for i in range(len(quotes1)):
    for j in finalBoilerPlate:
        if(j.find("p>") == -1):
            quotes1[i]['Page_Article'] = quotes1[i]['Page_Article'].replace(j.rstrip().strip(), "")
#%% Write back to the JSON format
with open("check4v3.json", "w") as outfile:  
    json.dump(quotes1, outfile) 
# =============================================================================
# Note: If you re-run the code through the output, you will see a different
#       boilerplate potentials list because this code will be looking for the 
#       next "Top 3".
# =============================================================================
        
        


