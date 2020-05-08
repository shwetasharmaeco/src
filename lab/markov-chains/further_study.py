"""Generate Markov text from text files."""

from random import choice
import sys



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    print (sys.argv)
    with open (str(sys.argv[1])) as file:
        data = file.read().replace("\n", " ")


    return data


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string = text_string.split()

    # text_string.append(None)
    
    n = int (input("Choose n for n-gram : "))
    print (text_string)
    
    
    for i in range(len(text_string)-n):
        key = tuple()
        for j in range(0,n):
            key +=(text_string[i+j],)
        
        value = text_string[i+n]
        if key not in chains.keys():
            chains[key] = []
        chains[key].append(value)    

    
    print(chains)
    
    return chains
 

def make_text(chains):
    """Return text from chains."""
    random_pair = (choice(list(chains.keys())))
    print("I am random pair", random_pair)

    words = []

    for word in random_pair:
        words.append(word)
 

    words.append(choice(chains[random_pair]))

    key_ = tuple(words[-(len(random_pair)):])


    while key_ in chains:

        if chains[key_] is not None:
            words.append(choice(chains[key_]))
            key_ = tuple(words[-(len(random_pair)):])
        else:
            break

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
