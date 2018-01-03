def long_repeat(line):

    length = 1
    longest = 0
    
    for c in range(len(line)-1):
        
        if line[c] == line[c+1]:
            length += 1
        else:
            length = 1
        
        if length > longest:
            longest = length
    
    return longest

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('aa') == 2, "3rd"
    print('"Run" is good. How is "Check"?')
