""" Rules
    for words that begin with consonant sounds,the initial consonant
    or consonant cluster is moved to the end of the word, and 'ay' is added,
    as in the following examples:
    'happy'->'appyhay'
    'duck' ->'uckday'
    'glove'->'oveglay'
    For words that begin with vowel sounds or silent letter, you just add
    'way' to the end.Examples are:
    'egg'->'eggway'
    'inbox'->'inboxway'
    'eight'->'eightway'
"""
def pig_latin(str):
    vowels = ['a','e','i','o','u']
    if str[0:1] in vowels:
        return str+'way'
    elif str[0:2] == 'qu':
        return str[2:]+'quay'
    else:
        for s in str:
            if s in vowels:
                return str[str.find(s):]+str[:str.find(s)]+'ay'
  
#Here are some test code.
str1 = 'stupid'
print pig_latin(str1)
str2 = 'amstrong'
print pig_latin(str2)
str3 = 'screen'
print pig_latin(str3)
str4 = 'fly'
print pig_latin(str4)
#yes,when the word is 'fly' the code go wrong.'y' is a vowel,too ,in this situaiton.   
