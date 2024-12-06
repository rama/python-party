"""
Authors: Keerthi Reddy, Ramapriya Radhakrishnan
Chapter 2 of Impractical Python Projects: Finding Palingram Spells
"""

import sys


def is_palindrome(word: str) -> bool:
    """
    checks if the word is a palindrome
    args:
        word: word to check

    returns:
        bool - True if palindrome, False otherwise
    """
    return word[::-1] == word


def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(
            "{}\nError opening {}. Terminating program.".format(e, file),
            file=sys.stderr,
        )
        sys.exit(1)


dict_path = "dictionaries/2of4brif.txt"
WORD_LIST = load(dict_path)


def is_palingram(word1, word2):
    combined = word1 + word2
    return is_palindrome(combined)


def find_palingrams(word, word_list):
    # get dictionary
    # loop through all words
    # check if each word + our word is a palingram
    palingram_words = []
    for new_word in word_list:
        if is_palingram(word, new_word):
            palingram_words.append(new_word)
        if len(palingram_words) > 5:
            break

    for new_word in palingram_words:
        print(f"{word} {new_word}")


# nurses run
# stack cats
# puff up
# def main():
#     for word in WORD_LIST:
#         find_palingram(word, WORD_LIST)


def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(WORD_LIST)
    for word in words:
        word_length = len(word)
        rev_word = word[::-1]
        if word_length > 1:
            for i in range(word_length):
                if (word[i:] == rev_word[: word_length - i]) and (
                    rev_word[word_length - i :] in words
                ):
                    pali_list.append((word, rev_word[word_length - i :]))
                if (
                    word[:i] == rev_word[word_length - i :]
                    and rev_word[: word_length - i] in words
                ):
                    pali_list.append((rev_word[: word_length - i], word))
    return pali_list


print(find_palingrams())
