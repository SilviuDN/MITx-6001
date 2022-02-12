# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 12:50:26 2022

@author: Silviu
"""

#row 22 needed


lyrics = [1,2,3,4,2,1,3,3,3,4,4,4,5,5,5,5]

def lyricsToFrequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

print ( lyricsToFrequencies( lyrics ) )

def mostCommonWords( freqs ):
    if len(freqs) == 0: return ([],0)
    values = freqs.values()
    mostFreq = max(values)
    mostFrequentWords = []
    
    for k in freqs:
        if freqs[k] == mostFreq:
            mostFrequentWords.append(k)
    return (mostFrequentWords, mostFreq)

print( mostCommonWords( lyricsToFrequencies( lyrics ) ))

def commonWords( freqs, minTimes ):
    res = []
    done = False
    while not done:
        temp = mostCommonWords(freqs)
        if temp[1] >= minTimes:
            res.append( temp )
            for commonWord in temp[0]:
                del(freqs[commonWord])
        else: done = True
    return res

print( commonWords( lyricsToFrequencies( lyrics ), 2 ) )
        