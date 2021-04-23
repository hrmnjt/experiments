def is_isogram(string):
    try:
        lowercase_string = string.lower()
        for char in lowercase_string:
            ascii_char = ord(char)
            if (ascii_char >= 97 and ascii_char <= 122):
                if (lowercase_string.count(char) == 1):
                    continue
                else:
                    return False
                    break
            else:
                continue
        return True
        
    except SyntaxError as err:
        raise Exception('Boo boo, you have a syntax error.\n Error: ', err)
