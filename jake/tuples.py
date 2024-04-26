# Jake | April 2024





# open original words (of Gratian 2) file
with open("work/corpora/final/Gratian2.txt", "r") as original_words_file:

    # read line
    first_line_og = original_words_file.readline()

    # split line at every whitespace
    original_words = first_line_og.split()

# open lemmatized words (of Gratian 2) file
with open("work/corpora/final_lemmas/Gratian2.txt", "r") as lemmatized_words_file:

    # read line
    first_line_lemmatized = lemmatized_words_file.readline()

    # split line at every whitespace
    lemmatized_words = first_line_og.split()

# initialize list to store tuples in
list_of_tuples = []

# initialize counter (to track index)
index = 0

for lemma in lemmatized_words:

    # find original word
    og_word = "test"

    # create tuple to store index, original word, lemmatized word
    new_tuple = (index, og_word, lemma)

    # increment index
    index += 1
	
    # append tuple to list
    list_of_tuples.append(new_tuple)

print(list_of_tuples)





