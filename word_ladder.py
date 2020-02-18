#!/bin/python3
import collections


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    f = open(dictionary_file, 'r')
    words = [w.strip('\n') for w in f]

    word_lst = []
    word_lst.append(start_word)
    word_q = collections.deque()
    word_q.appendleft(word_lst)
    while word_q: 
        temp_stack = word_q.pop()
        for word in words:
            if _adjacent(word, temp_stack[-1]):
                    if word == end_word:
                        temp_stack.append(word)
                        return(temp_stack)
                    stack_copy = temp_stack.copy()
                    stack_copy.append(word)
                    word_q.appendleft(stack_copy)
                    words.remove(word)
def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    
    >>> verify_word_ladder(['dog', 'bog', 'hog', 'log'])
    True
    '''
    if len(ladder) == 0:
        return False
    for i in range(len(ladder) - 1):
        if _adjacent(ladder[i], ladder[i+1]) == False:
            return False
    return True

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    >>> _adjacent('abome', 'above')
    True
    '''
    if len(word1) != len(word2):
        return False

    count = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False


