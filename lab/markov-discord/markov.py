"""A Markov chain generator that can tweet random messages."""
import os
import discord
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open (file_path,"r") as file:
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
    

    for i in range(len(text_string)-1):
        word1 = text_string[i]
        word2 = text_string[i+1]
        chains[word1, word2] = []   
    
    for tup, lst in chains.items():
        for i in range(len(text_string)-2):
            if text_string[i]== tup[0] and text_string[i+1]== tup[1]:
                lst.append(text_string[i+2])
        if chains[tup] ==[]:
            chains[tup] = None

    print (chains)       
    return chains
 

def make_text(chains):
    """Return text from chains."""

    random_pair = (choice(list(chains.keys())))

    words = []

    words.append(random_pair[0])
    words.append(random_pair[1])

    words.append(choice(chains[random_pair]))

    key_ = tuple(words[-2:])


    while key_ in chains:

        if chains[key_] is not None:
            words.append(choice(chains[key_]))
            key_ = tuple(words[-2:])
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




client = discord.Client()


@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("s"):

        await message.channel.send(make_text(chains))


        

        # Get the filenames from the user through a command line prompt, ex:
        # python markov.py green-eggs.txt shakespeare.txt
        

client.run(os.environ['DISCORD_TOKEN'])

# client.run('replace this with your token from secrets.sh')
