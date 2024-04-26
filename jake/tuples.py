
# Jake | April 2024



# part 1 | identify unique lemmas found in Gratian 2

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



# part 2 | create list of tuples

# open original words (of Gratian 1) file
with open("work/corpora/final/Gratian1.txt", "r") as g1_original_words_file:

    # put words on a single line
    g1_single_line = "".join(g1_original_words_file.readlines())

    # split line at every whitespace
    g1_split_line = g1_single_line.split()

# open original words (of Gratian 2) file
with open("work/corpora/final/Gratian2.txt", "r") as g2_original_words_file:

    # put words on a single line
    g2_single_line = "".join(g2_original_words_file.readlines())

    # split line at every whitespace
    g2_split_line = g2_single_line.split()

    # remove words found in Gratian 1
    unique_split_line = [word for word in g2_split_line if word not in g1_split_line]



# initialize list to store tuples in
list_of_tuples = []

# initialize counter (to track index)
index = 0

for lemma in list_of_lemmas:

    # find original word (by checking if first 3 characters match) <- is this inaccurate?
    for original_word in unique_split_line:

        if (lemma[:3]) == (original_word[:3]):
            og_word = original_word

    # create tuple to store index, original word, lemmatized word
    new_tuple = (index, og_word, lemma)

    # increment index
    index += 1

    # append tuple to list
    list_of_tuples.append(new_tuple)

# alphabetize?

# print
for tuple in list_of_tuples:

    print(tuple)
