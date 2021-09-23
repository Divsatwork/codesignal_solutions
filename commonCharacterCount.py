"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

def commonCharacterCount(s1, s2):
    x = (set(s1).intersection(set(s2)))
    c = 0
    for i in x:
        
        s1_count = s1.count(i)
        s2_count = s2.count(i)
        if s1_count < s2_count: c+=s1_count
        else: c+=s2_count
    return c
