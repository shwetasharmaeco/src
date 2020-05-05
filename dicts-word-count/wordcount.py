import sys
dict_word_count = {}
with open(str(sys.argv[1])) as dict_file:
    for line in dict_file:
        for char in line:
            if char != " " and not char.isalnum():
                line = line.replace(char,"")
        
        poem_words = line.lower().rstrip().split() 
        
        for word in poem_words:
            dict_word_count[word] = dict_word_count.get (word, 0) + 1

for word, count in sorted(dict_word_count.items(), key = lambda x: (-x[1], x[0]) ):
    print(word, count) 






