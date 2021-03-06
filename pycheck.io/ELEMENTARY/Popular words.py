def popular_words(text, words):
    
    dict1 = {}
    text1 = text.lower()

    for w in words:
        dict1[w] = text1.count(w)
    return dict1


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))


    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
    When I was One,
    I had just begun.
    When I was Two,
    I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
