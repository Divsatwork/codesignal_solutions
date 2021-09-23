"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""

def allLongestStrings(inputArray):
    m = 0
    for i in inputArray:
        if len(i) > m:
            m = len(i)
    
    return list(filter(lambda x: len(x) == m, inputArray))
