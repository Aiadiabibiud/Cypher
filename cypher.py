#Aidan Lembcke
#SN: 340930908
def cypher(word, shift):
    '''
    This function takes an alphanumeric value and an integer value and shifts all of the alphabetical characters
    by the integer provided
    '''
    shift = int(shift)%26
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
