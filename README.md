# Teaching Gratian
![Gratian and his students](img/St-Omer.jpg)

Gratian teaching, from Saint-Omer Bibliothèque Municipale 453 manuscript of Gratian's *Decretum*
## COMP499
Spring 2024 Computer Science Independent Study with Jake Bayon

---
### Checklist
- [x] Jake: sign up for and attend [Creative Collaborations presentation workshop](https://www.sandiego.edu/events/detail.php?_focus=91693) (Thursday, 7 March 2024)

---
### 4 March 2024
Problem solved: you can install the nlp-pie and pie-extended packages in a Python 3.8 (or 3.7) virtual environment, but you have to install them together.
```
python3.8 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install nlp-pie pie-extended
pie-extended download lasla
pie-extended install-addons lasla
pie-extended tag lasla your_file.txt
```
---
Before Friday:
+ incorporate revised version of Creative Collaborations slide submission text into [Jake.md](Jake.md).
+ run [lemmatize.py](work/lemmatize.py). Make sure to use the Python 3.8 virtual environment with nlp-pie and pie-extended installed!
+ lemmatize.py writes four output files in the [`work/corpora/final_lemmas`](work/corpora/final_lemmas/) folder: Gratian0.txt, Gratian1.txt, Gratian2.txt, and dePen.txt. These are lemmatized versions of the text of the case statements or *themata* (Gratian0.txt), the first-recension *dicta* or sayings of Gratian (Gratian1.txt), the second-recension *dicta* (Gratian2.txt), and the *dicta* from *de Penitentia* (dePen.txt).
+ your deliverable is to generate a list of lemmas that are in Gratian2.txt and are not in Gratian1.txt using a Python list comprehension (see example in Jake.md under 12 February 2024).

<details>

<summary>Week 5</summary>

### 26 February 2024
</details>

<details>
<summary>Week 4</summary>

### 19 February 2024
</details>

<details>
<summary>Week 3</summary>

### 12 February 2024
+ demo for Jake
---
Before next Monday:
+ Clone PIE from GitHub (`https://github.com/emanjavacas/pie.git`) and try to get it to work in a Python 3.12 virtual environment
+ Start writing the narrative sections for your Creative Collaborations presentation by answering the following questions:
  - Who was Gratian?
  - What is the *Decretum* and why is it important?
  - What is lemmatization and what can it tell us about the *Decretum*?
+ Keep track of your progess in a Markdown-format file
  - https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
  - 
</details>

<details>
<summary>Week 2</summary>

### 5 February 2024
+ Dr (Rick) Olson confirmed that course code is COMP499  
`COMP 499` INDEPENDENT STUDY  
Units: 1-3 Repeatability: Yes (Can be repeated for Credit)  
Individual study including library or laboratory research or program writing. A written report is required. Project proposal must be submitted and approved prior to enrollment. May be repeated for credit.
+ Dr Stern and Dr Olson recommended a presentation at the [Creative Collaborations](https://www.sandiego.edu/ugresearch/students/creative-collaborations.php) Undergraduate Research Conference (CCURC) instead of a written report
+ Paul's proposal for the Seventeenth International Congress of Medieval Canon Law (ICMCL XVII) was accepted, so we will be working on lemmatization before regular expressions. See [this link](ICMCL.md) for the call for papers and proposal.
+ Introduction to lemmatization
  - "Humanum genus duobus regitur"
  - "humanus", "genus", "duo", "rego"
+ Install Python 3.8 and virtual environment  
`python3.8 -m venv pie`  
`cd pie`  
`source ./bin/activate`  
`pip install --upgrade pip`  
`pip install nlp-pie`  
`pip install pie-extended`  
`pie-extended download lasla`  
`pie-extended install-addons lasla`  
`pie-extended tag lasla your_file.txt`  
---
Before next Monday, watch:
+ Mike Kestemont, [Documentary: "Hildegard of Bingen: Authorship and Stylometry" \[HD\]](https://vimeo.com/70881172)  
(Be ready to turn down the volume at 3:12-3:32 and at 8:26-8:46)
</details>

<details>
<summary>Week 1</summary>

### 29 January 2024
+ Remember to bring HDMI adapter to every class meeting!
+ Install [Visual Studio Code](https://code.visualstudio.com/) or upgrade to the current version (1.86.0)
  - **Make sure that VSCode is *not* installed in the Downloads folder!**
  - In order for `Check for Updates...` to work, you have to open Terminal and enter either  
`xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app` or  
`xattr -dr com.apple.quarantine ~/Applications/Visual\ Studio\ Code.app`  
on the command line depending on whether you installed VSCode in the system or user Applications folder.  
If you installed VSCode in the system Applications folder, you *may* have to enter this command first:  
`sudo chown $USER ~/Library/Caches/com.microsoft.VSCode.ShipIt`  
+ GitHub setup
  + ~~Create GitHub account: `jakebayon12`~~
  + **Enable two-factor authentication!**
  + ~~Create repository for COMP299: `Gratian`~~   
  `git clone git@github.com:jakebayon12/Gratian.git` or  
  `git clone https://github.com/jakebayon12/Gratian.git`  
  + ~~Share repository with `decretist`~~ (Paul's GitHub username. In the Middle Ages, a *decretist* was someone who studied Gratian's *Decretum*.)
+ What do you think of when you think of the Middle Ages?
+ Introductory activity: What do you know, or think you know, about the Middle Ages? Any source, e.g., other courses, fiction or non-fiction books, TV ("Game of Thrones"), movies ("Secret of Kells”), or video games is OK!
  - feudalism
  - castles
  - dragons (because Paul gave that as an example)
  - peasants
  - nobility
  - tension between science and religion
---
Before next Monday, read
+ Anders Winroth, [Gratian and His Book](Readings/Winroth%20-%20Gratian%20and%20His%20Book.pdf) and watch
+ Paul Evans, [The Medieval University & the Question of Education: Gratian's *Decretum* & the Dawn of the University](https://www.youtube.com/watch?v=x2KbkcjMLDM)
</details>

<details>
<summary>Week 0</summary>

### 1 December 2023
#### Syllabus
+ Introduction:
  - The scholarly problem: multiple recensions of Gratian's Decretum
+ Materials:
  - OCP-format e-text of the 1879 Friedberg edition of Gratian's Decretum
  - Decretum Gratiani, First recension, edition in progress (Anders Winroth)
  - Anders Winroth, The Making of Gratian's Decretum, Appendix: The contents of the first recension of Gratian's Decretum
+ Tools:
  - VS Code and XML Tools extension
  - Git and GitHub
+ Python Techniques:
  - Lemmatizing natural language text (Medieval Latin)
  - Using regular expressions
  - Recursive-descent parsing
  - Generating TEI P5 XML
+ Deliverables:
  - Parse OCP e-text of Friedberg edition
  - Use regular expressions to transform vulgate readings (Friedberg edition) into first recension readings (Winroth appendix)
  - Output result as TEI P5 XML e-text of the first-recension
  - Lemmatize vulgate (Friedberg) and first-recension (Winroth) texts
  - Isolate lemmas that appear in the vulgate (Friedberg) but not in the first-recension text of Gratian's Decretum
---
Before the start of the semester, read
+ Peter Landau, [Gratian and the *Decretum Gratiani*](Readings/Landau%20-%20Gratian%20and%20the%20Decretum%20Gratiani.pdf)
</details>
