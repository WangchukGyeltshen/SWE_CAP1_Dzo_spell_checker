################################
#https://github.com/WangchukGyeltshen/SWE_CAP1_Dzo_spell_checker

#Wangchuk Gyeltshen Zangpo
#Section A
#02240370
################################
#REFERENCES
#PROBLEM STATEMENT: You are tasked with a spell checker for the language. Your should read a text file (dzo.txd) that contains multiple spelling errors which will be provided by the tutor (refer Accessing Input File section)The program should identify and report these errors.
#https://youtu.be/TqE4jBH4Me4?feature=shared
#https://youtu.be/L2BDTy4bEcg?feature=shared
#https://youtu.be/Mi3j54ZMxOc?feature=shared
#https://youtu.be/LpZmZs2_BC4?feature=shared
################################
#SOLUTION
################################

import re


def extract_words(text):
    
    words= re.findall(r'[\u0F00-\u0FFF]+', text) #In this part I got help from AI as I didn't know how dzongkha characters were represented
    return set(words)  

#Reading the input file
with open("370.txt", encoding="utf-8") as file:
    content1 = file.read()
    word1 = extract_words(content1)

#Reading the dictionary file
with open("cleaned_dictionary_file.txt", encoding="utf-8") as file:
    content2 = file.read()
    word2 =extract_words(content2)

#Main spell checking function
File_comparison = word1.difference(word2)  

for word in File_comparison:
    print(f"The word '{word}' from 370.txt is incorrect.")