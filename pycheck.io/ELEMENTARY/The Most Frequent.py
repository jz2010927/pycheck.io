def most_frequent(data):
    
    most = data[0]
    frequent = data.count(data[0])
    
    for c in data:
        if c != most:
            if data.count(c) > frequent:
                most = c
                frequent = data.count(c)
                
    return most

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
