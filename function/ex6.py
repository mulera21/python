def break_words(stuff):
    """this function will break up words for us."""
    words = stuff.split(' ')
    return words
def sort_words(words):
    """sorts the word"""
    return sorted(words)
def print_first_word(words):
    """print the first word after popping it off """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """print the last word after popping it off"""
    word = words.pop(-1)
    print(words)

def sort_sentence(sentence):
    word = break_word(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
