def is_pangram(sentence):
    try:
        lowercase_sentence = sentence.lower()
        
        alphabets = "abcdefghijklmnoprstuvwxyz"
        
        for char in alphabets:
            if char not in lowercase_sentence:
                return False
            else:
                continue
        
        return True
    
    except SyntaxError as err:
        raise Exception("Syntax error.\n Error: ", err)
