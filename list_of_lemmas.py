# Jake | March 2024

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
list_of_lemmas = [word for word in lemmatized_gratian_2 if word not in lemmatized_gratian_1]

print(len(list_of_lemmas))

# convert to set 
list_of_unique_lemmas = list(set(list_of_lemmas))

print(len(list_of_unique_lemmas))

# sort alphabetically
list_of_unique_lemmas.sort()

#print(list_of_unique_lemmas)

for lemma in list_of_unique_lemmas:

    print(lemma)
