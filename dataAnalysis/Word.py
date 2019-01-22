#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
出现次数最多的单词
'''
__author__ = 'tzl'



"""Quiz: Most Frequent Word"""


def most_frequent(s):
    """Return the most frequently occuring word in s."""

    # HINT: Use the built-in split() function to transform the string s into an
    #       array
    words = s.split(' ')

    # HINT: Sort the new array by using the built-in sorted() function or
    #       .sort() list method
    words.sort()


    # HINT: Iterate through the array and count each occurance of every word
    #       using the .count() list method

    count = 0
    for word in words:
        print(word)

    # HINT: Find the number of times the most common word appears using max()

    # HINT: Locate the index of the most frequently seen word

    # HINT: Return the most frequent word. Remember that if there is a tie,
    #       return the first (tied) word in alphabetical order.

    result = ''
    return result



def test_run():
    """Test most_frequent() with some inputs."""
    most_frequent("cat bat mat cat bat cat")
    # print(most_frequent("cat bat mat cat bat cat"))  # output: 'cat'
    # print(most_frequent("betty bought a bit of butter but the butter was bitter"))  # output: 'butter'

if __name__ == '__main__':
    test_run()
