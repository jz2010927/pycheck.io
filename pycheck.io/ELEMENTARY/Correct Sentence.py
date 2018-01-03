def correct_sentence(text: str) -> str:
    
    text1 = list(text)
    text1[0] = text1[0].upper()
    if text1[-1] != '.':
        text1.append('.')
    
    str = ''.join(text1)
    
    return str


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    print("Coding complete? Click 'Check' to earn cool rewards!")
