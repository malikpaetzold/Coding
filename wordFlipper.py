# Given a sentence, reverse each word in the sentence while keeping the order the same!

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
        our_string(string): String with words to flip
    Returns:
        string: String with words flipped
    """
    
    # TODO: Write your solution here
    
    words = our_string.split(" ")
    out = ""
    for word in words:
        reverse = ""
        for i in range(len(word)):
            reverse += word[len(word)-1-i]
        reverse += " "
        out += reverse
    return out[0:-1]

# Test Cases

print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")