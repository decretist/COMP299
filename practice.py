
# Jake Bayon (jbayon@sandiego.edu)
# 26 February 2024

# REGULAR EXPRESSIONS

import re

def main():
    text = 'Humanum genus duobus regitur, naturali uidelicet iure et moribus. Ius naturae est, quod in lege et euangelio continetur, quo quisque iubetur alii facere, quod sibi uult fieri, et prohibetur alii inferre, quod sibi nolit fieri. Unde Christus in euangelio: "Omnia quecunque uultis ut faciant uobis homines, et uos eadem facite illis. Haec est enim lex et prophetae." Hinc Ysidorus in V. libro Ethimologiarum ait:'
    
    #print(text)

    result = re.match(".", text)
    #print(result[0])
    # results in "H"

    result = re.match(".*", text)
    #print(result[0])
    # results in entire sentence

    result = re.match(".?", text)
    #print(result)

    result = re.match(".*?", text)
    #print(result[0])

    # how to access/print a subsection
    result = re.match("Humanum genus.* nolit fieri\.", text)
    #print(result[0])

if __name__ == "__main__":
    main()



# notes on regular expressions

    # a "mini language" for dealing w/ strings

    # . represents "any character except newline (\n)"
    # .* represents "0 or more occurences of something"
    # .? [possibly represents "0 or 1 more occurences of something"] <- VERIFY