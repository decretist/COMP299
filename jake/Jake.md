
```
# Jake
# 12 February 2024

# list comprehensions 

def main():
    print("hello world")

    list_1 = ["gratian", "monk", "hildegard"]
    list_2 = ["canon", "gratian", "monk"]

    # list comprehensions
    print([word for word in list_1 if word not in list_2])

if __name__ == "__main__":
    main()    
```

# 19 February 2024

## cheatsheet for markdown format
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

## in virtual environment, installed:

+ tqdm
+ torch
+ pyyaml
+ json_minify
+ lxml

## errors
`AttributeError: module 'test.data.test_data' has no attribute 'Testing'`

## misc.

+ command + shift + v to see preview of markdown

## to-do

+ write text for creative collaborations poster (answer main questions)
https://docs.google.com/document/d/1aLTDgrbmGOcx2GIiBQpFKyux1MPevUX4_6qoxyoQkRU/edit
+ send update on friday

# 26 February 2024

## to-do

+ revise poster narrative section

+ read intro to regular expressions (see bookmarked article)

+ try to figure out what ".*?" means (in regular expression) (appears in decretist/Gratian -> sample -> auto -> dicta.py)

## notes on second recension (library copy)

+ third section "doesn't have to do w/ gratian"
+ some popes falsely quoted (inaccurate/forged?)

+ harp-like symbol used to signify gratian

# 4 March 2024

## to-do

+ put poster text in Jake.md (here)

+ run lemmatize.py
+ make sure doing this in python 3.8 virtual environment

+ will end up w/ 4 files in corpora -> final_lemmas
+ Gratian0, Gratian1, Gratian2, dePen: these are lemmatized versions of the text (in final_lemmas folder)

+ (see list comprehensions examples from last meeting)

+ list comprehensions (gives list of every word that's in one list + not other)
+ goal: create list of lemmas that are in Gratian2 and NOT in Gratian1

# 11 March 2024

## narrative section for (hypothetical) poster

A Computational Analysis of Gratian’s Decretum (c. 1140)

In the expanse of medieval history, amidst the crisis of the church and state, stands a figure often overlooked: Gratian. A posthumous luminary of 12th century Europe, he was a magister of law, a weaver of harmony in the discordant fabric of the Christian church’s canonical regulations. His work synthesized the canons of councils, papal decretals, and biblical texts established across a millennium, and he shared his methodologies as the first to teach canon law as an academic subject. 

Gratian’s magnum opus, Concordia Discordantium Canonum (The Harmony of Discordant Canons), assembled circa 1140 and later referred to as the Decretum, was more than a compilation of legal doctrines; it was a symphony of jurisprudence, bringing order to the cacophony of contradictory laws that had accumulated over centuries. Gratian's work not only laid the foundation for the study and practice of canon law but also served as a beacon of intellectual rigor and order in an era that sought to unearth and systematize knowledge of the past. 

The Decretum, often hailed as the first university textbook, was not merely a relic of the past but a document that continues to shape modern society. A model for all Western law, its biblical approach to the legal field continues to impact the way many live their lives. Many principles of contemporary Catholic ecclesiastical law can be traced back to Gratian's seminal work, underscoring its enduring relevance.
However, the journey of the Decretum does not end with its initial composition. The discovery of the text’s first recension—an earlier edition that is approximately half of the size of its more widely known counterpart—has opened new avenues of inquiry, inviting scholars to delve deeper into its structural evolution. In this vein, our research project employs computational analysis, leveraging techniques such as lemmatization to discern the nuances between different stages of the text's development between its first and second recensions.

Lemmatization, a cornerstone of computational linguistics and natural language processing, offers an approach through which we can unravel the intricacies of Gratian's book. This technique involves breaking a word down to its root meaning, or lemma. For instance, the verb regitur (ruled) can be reduced to its infinitive regere (to rule). By mapping each Latin word to its root form, we aim to uncover the subtle shifts in language and doctrine that distinguish the Decretum's various recensions. Through this synergy of historical inquiry and technological innovation, we endeavor to illuminate a clearer understanding of Gratian's legacy—a story that continues to resonate in the hearts and minds of scholars and believers alike.

# 14 April 2024

## link to slideshow (for creative collabs presentation)
https://docs.google.com/presentation/d/1icXSh_cevUxDThI0pZc3ZkVV5VFejmJz5FeX51RRAgU/edit#slide=id.g26823933375_0_0

## link to speaker notes (for creative collabs presentation)
https://docs.google.com/document/d/1cbic1TGM4Ecxnd-WCtYMX9-r4iDk6P53wCUxITb6Q4c/edit

# 9 May 2024

## link to google drive folder with notes on readings, meetings,and creative collabs presentation
https://drive.google.com/drive/folders/1L1qdXKyiqOCB3-oRj2dDKcl1NsHPt0yL?usp=sharing
