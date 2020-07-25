"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    answer = []
    for elem in list1:
        if elem not in answer:
            answer.append(elem)
    return answer

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    answer = []
    for elem in list1:
        if elem in list2:
            answer.append(elem)

            
    return answer

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    answer = []
    
    list1_copy = list(list1)
    list2_copy = list(list2)
    
    while len(list1_copy) > 0 and len(list2_copy) > 0:

        if list1_copy[0] > list2_copy[0]:
            answer.append(list2_copy.pop(0))
        else:
            answer.append(list1_copy.pop(0))
    
    if len(list1_copy):
        answer += list1_copy
    else:
        answer += list2_copy
    return answer
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1
    
    mid = len(list1)/2

    return merge(merge_sort(list1[:mid]), merge_sort(list1[mid:]))


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]
    
    
    first = word[0]
    rest = word[1:]
    
    rest_strings = gen_all_strings(rest)
    
    new_strings = []
    
    for string in rest_strings:
        for pos in range(len(string)+1):
            
            list_string = list(string) #convert string to list
            list_string.insert(pos, first)#insert the first letter in position
            new_strings.append("".join(list_string))#combine list to string
            
    return rest_strings + new_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    