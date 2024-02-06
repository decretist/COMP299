## COMP499
Spring 2024 Independent Study with Jake Bayon

---

Default branch is `main`!

---
### Week 3 (12 February 2024)
### Week 2 (5 February 2024)
+ Dr Olson confirmed that course code is COMP499  
`COMP 499` INDEPENDENT STUDY  
Units: 1-3 Repeatability: Yes (Can be repeated for Credit)  
Individual study including library or laboratory research or program writing. A written report is required. Project proposal must be submitted and approved prior to enrollment. May be repeated for credit.
+ Dr Stern and Dr Olson recommended a poster at the Creative Collaborations Undergraduate Research Conference (CCURC) instead of a written report
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
+ Mike Kestemont: [Documentary: "Hildegard of Bingen: Authorship and Stylometry" \[HD\]](https://vimeo.com/70881172)  
(Be ready to turn down the volume at 3:12-3:32 and at 8:26-8:46)
### Week 1 (29 January 2024)
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
+ Paul Evans: [The Medieval University & the Question of Education: Gratian's *Decretum* & the Dawn of the University](https://www.youtube.com/watch?v=x2KbkcjMLDM)
+ What do you think of when you think of the Middle Ages?
+ Introductory activity: What do you know, or think you know, about the Middle Ages? Any source, e.g., other courses, fiction or non-fiction books, TV ("Game of Thrones"), movies ("Secret of Kells”), or video games is OK!
  - feudalism
  - castles
  - dragons (because Paul gave that as an example)
  - peasants
  - nobility
  - tension between science and religion
