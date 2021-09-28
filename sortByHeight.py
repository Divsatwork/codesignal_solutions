"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""

def sortByHeight(a):
    
    people_index = []
    heights = []
    for i in range(len(a)):
        if a[i] != -1:
            people_index.append(i)
            heights.append(a[i])
            
    # Now that we have the indexes, we just need to sort the heights accordingly
    heights.sort()
    result = []
    print(people_index)
    print(heights)
    for i in range(len(a)):
        if i in people_index:
            a[i] = heights.pop(0)
    return a
            
    

