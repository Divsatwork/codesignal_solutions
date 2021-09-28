"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""

def reverseInParentheses(inputString):
    
    if inputString == "()":
        return ""
    if len(inputString) == 0:
        return ""
    
    import re
    def convert(match):
        print("In convert method")
        return ''.join(str(match.group())[-2:0:-1])
    
    while True:
        search_result = re.search(r'\([a-z]+\)', inputString)
        if search_result is not None:
            inputString = re.sub(r'\([a-z]+\)', convert, inputString)
        else:
            break
    
    return inputString
        

