#Aidan Lembcke
#SN: 340930908
def cypher(word):
    '''
    this encrypts the target string using Caesar encryption

    arguments
        target : string
        value : integer

    return
        string : encrypted version of target
    '''
    word = word.split(', ')
    shift = word[-1]
    word = word[0]
    shift = int(shift)%26 # This line turns the number string into an integer and also takes the remainder of a division by 26 to keep the provided value within the range of the alphabet. 
    word = word.lower()
    chs = ''
    for i in word:
        if ord(i)+shift < 97 and i.isalpha():
            dif = 123+shift
            chs = chs + chr(123+shift)
        elif ord(i)+shift > 122 and i.isalpha():
            dif = 96+shift
            chs = chs + chr(96+shift)
        elif i.isalpha():
            chs = chs + chr(ord(i)+shift)
    return chs
