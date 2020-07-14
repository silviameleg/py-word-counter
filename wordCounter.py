x = False;
while x is False:
    hand = open('lincoln.txt')
    txt = hand.read()
    wordSearched = input('Type here your word: ')
    wordCount = txt.count(wordSearched)
    if wordSearched in txt:
        print('The word "' + wordSearched + '" is found in the text ' + str(wordCount) + ' times.')
        
        '''Additionally, you can add the bellow code so the user will only be asked to
        type in another word if the previous word wasn't found in the text:'''
        #x = True
        
    else:
        print('Oops, the word "' + wordSearched + '" is not found in the text. \nLet\' try another word!')
        
