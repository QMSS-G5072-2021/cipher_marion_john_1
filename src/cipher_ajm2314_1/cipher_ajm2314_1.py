def cipher(text, shift, encrypt=True):
    """
    Encrypts and decrypts phrases by moving each alphabetical character a given number of index units.

    Parameters
    ----------
    text: A string to be encrypted or decrypted. Can include alphabetical or other characters 
    shift: The number of index units to shift each alphabetical character. 
        An integer
    encrypt: If True, alphabetical characters will be shifted by the given value for the shift argument.
        If false, the alphabetical characters will be shifted by the negative of the given value for the shift argument.
    
    Returns
    ----------
    string
        The encrypted or decrypted string.

    Examples
    ----------
    >>> import cipher_ajm2314
    >>> cipher('Mr. Smith Goes to Washington',1)
        'Ns. Tnjui Hpft up Xbtijohupo'

    >>> cipher('Mr. Smith Goes to Washington',-3)
        'Jo. Pjfqe Dlbp ql TXpefkdqlk'

    >>> cipher('Mr. Smith Goes to Washington',3,encrypt=False)
        'Jo. Pjfqe Dlbp ql TXpefkdqlk'
    """
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
