"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""
def solution(picture):
    result = ["*"*(len(picture[0])+2)]
    for i in picture:
        result.append("*"+str(i)+"*")
    result.append("*"*(len(picture[0])+2))
    return result
