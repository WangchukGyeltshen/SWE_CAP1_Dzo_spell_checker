# Dzongkha Spell Checker

## Project Overview
Our objective for this assignment was to create a Dzongkha spell checker. Its purpose is to point out incorrect Dzongkha words in the article provided to us by comparing each word to the dictionary also provided by the Module Professor.

## Table of Contents
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Data Structures](#data-structures)
- [Algorithms](#algorithms)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Improvements](#future-improvements)
- [References](#references)

## Usage
To use the spell checker, a text file containing Dzongkha words is required. To check the spelling of the words in the text file, you need to input the file into the code:

    ```python
            with open("Inputfilehere.txt", encoding="utf-8") as file:
                content1 = file.read()
                word1 = extract_words(content1)


After running the code, it should provide the incorrect spellings of the words in the text file.

## Implementation Details
Firstly, during the conversion of the .docx file to the .txt file, I used a third-party library package called docx2txt, which I installed from the pip installer.

Secondly, in the final spell checker, I used set operations (difference) to find the words unique to each file. This allowed me to identify which words were incorrect in the input file as they weren't present in the dictionary file. I learned about set operations through AI.

## Data Structures
The main data structures used in the spell checker are:

Sets (word1, word2): Store unique words for comparison.
Strings (text, content1, content2): Handle the raw file content and Dzongkha words.
Lists (output of re.findall()): Temporarily store matched words before conversion to sets.
The main data structures used while converting the .docx files to .txt are:

Strings (dfile, tfile, doc): Store the file paths and text data extracted from the .docx file.
The main data structures used while cleaning the dictionary.txt file are:

Strings (content, cleaned_txt): Store the raw and cleaned text from the file.

## Algorithms
The key algorithms used in the spell checker are:

Regular Expression Matching Algorithm (re.findall()): Extracts Dzongkha words from the text based on Unicode patterns.
Set Difference Algorithm (word1.difference(word2)): Identifies words in word1 (input file) that are not in word2 (dictionary), indicating potential spelling errors.
File Algorithm (open(), read()): Reads text content from files for processing and comparison.
The main algorithms used in cleaning the file are:

File I/O Operations: Read the content of dictionary.txt and write the cleaned result to cleaned_file.txt.
Input: File reading (file.read())
Output: File writing (file.write(cleaned_txt))
Substitution (re.sub()): Removes all matched characters ([a-zA-Z0-9.,!?'"()-_]+ matches English letters, digits, and certain punctuation) from the input content, leaving non-English characters intact.
String: cleaned_txt: Stores the modified version of the input content after removing unwanted characters, which is later written to the output file.
## Challenges and Solutions
During the process of creating the spell checker, one of the main challenges I faced was finding out how to represent Dzongkha letters in Unicode. I received help from AI in this regard and discovered that Dzongkha letters can be represented using the Unicode range [\u0F00-\u0FFF]+.

Another challenge was comparing the words between the input text file and the dictionary file. I resolved this issue by utilizing set operations (difference).

Future Improvements
One problem I couldn't solve is that, unlike English, Dzongkha words aren't separated by spaces or punctuation, making it difficult to accurately identify individual words. Due to this issue, the spell checker may not provide the correct output of which words are incorrect. This is an area I could work on for future improvements.

## References
-[https://youtu.be/TqE4jBH4Me4?feature=shared](#Video1)
-[https://youtu.be/L2BDTy4bEcg?feature=shared](#Video2)
-[https://youtu.be/Mi3j54ZMxOc?feature=shared](#Video3)
-[https://youtu.be/LpZmZs2_BC4?feature=shared](#Video4)