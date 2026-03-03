""" Talking to a teenager simulator """
def response(hey_bob):
    """ Talking to Bob returns one of five possible answers """
    
    input_minus_whitespace = str.strip(hey_bob)

    if len(input_minus_whitespace) == 0:
        return "Fine. Be that way!"
    if input_minus_whitespace.endswith('?') and input_minus_whitespace.isupper():
        return "Calm down, I know what I'm doing!"
    if input_minus_whitespace.endswith('?'):
        return "Sure."
    if input_minus_whitespace.isupper():
        return "Whoa, chill out!"
    return "Whatever."

