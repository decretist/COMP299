
# open Gratian1.txt (for reading)
with open("work/corpora/final_lemmas/Gratian1.txt", "r") as file_1:

    # read line
    first_line_gratian_1 = file_1.readline()

    # split line at every whitespace
    lemmatized_gratian_1 = first_line_gratian_1.split()

# open Gratian2.txt (for reading)
with open("work/corpora/final_lemmas/Gratian2.txt", "r") as file_2:

    # read line
    first_line_gratian_2 = file_2.readline()

    # split line at every whitespace
    lemmatized_gratian_2 = first_line_gratian_2.split()

# identify lemmas in Gratian2 but not in Gratian1
print([word for word in lemmatized_gratian_2 if word not in lemmatized_gratian_1])
