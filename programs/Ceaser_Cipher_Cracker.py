###Ceaser Cipher Cracker

def decription(message):
    
    #most common 112 english words
    words = ['time', 'person', 'year', 'way', 'day', 'thing', 'man',
             'world', 'life','hand', 'part', 'child', 'eye', 'woman',
             'place', 'work', 'week', 'case','point', 'government',
             'company', 'number', 'group', 'problem', 'fact'
             'be', 'have', 'do', 'say', 'get', 'make', 'go', 'know',
             'take', 'see', 'come', 'think', 'look', 'want', 'give',
             'use','find', 'tell', 'ask', 'work', 'seem', 'feel', 'try',
             'leave', 'call', 'good', 'new', 'first', ' last', 'long', 'great',
             'little', 'own', 'other', 'old', 'right', 'big', 'high', 'different',
             'next', 'early', 'young', 'important', 'few', 'public', 'bad',
             'same', 'able','for', 'on', 'with', 'at', 'by', 'from', 'up',
             'about', 'into','over', 'after', 'the', 'and', 'a', 'that', 'I',
             'it', 'not', 'he', 'as', 'you', 'this', 'but', 'his',
             'they', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all',
             'would', 'there', 'their', 'small', 'large','to', 'of', 'in']

    #origianl ord. of alphabets         
    alphabets = ['a', 'b', 'c', 'd', 'e',
              'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']
    
              
    
    '''Step 1(a): Split message into characters'''

    message  = [individual for individual in message.lower()] #split char
    
    '''Step 1(b): Setting up variable for futuer use'''
    
    shifted_alphabets = [] #to catch letters in modified order 
    shift = -25 # -25 to +25
    tolerance_error = 0 # init.
    
    while (tolerance_error < 30 or tolerance_error == 0):
        msg = '' #empty everytime

        '''Step 2: adjesment of lst of order'''
        
        j = shift
        while j < len(alphabets): # this appends c-z where a & b remian left.
            shifted_alphabets.append(alphabets[j])
            j += 1

        i = 0 # init for to append remaining alphabets
        while i < shift:
            shifted_alphabets.append(alphabets[i])
            i += 1

        '''Step 3(a): placement of spaces'''
        
        spaces = [' ', '\r', '  ', '   ', '\t', '\n'] #used for spaces
        for character in message:
            if (character in spaces):
                msg += character#print spaces
                continue # <- statement terminate allsteps beneath under expression
            '''Step 3(b): PLacement of adjested characters'''
            
            i = 0 # init for all character
            while (character != shifted_alphabets[i]): # find character index in org. lst = alphabets
                i += 1 
            if (character == shifted_alphabets[i]): # using org index placed in modified lst = shifted_alphabets
                msg += alphabets[i]
                
        '''Step 4(a): Split str into each word'''
        
        msg = msg.split() #split str into words 
        counter = 0 #count no. of words present in both msg & words
        '''Step 4(b): Matching words in lst = words'''
        
        for each in msg:
            i = 0
            if (each in  words):
                counter += 1
                continue # <- terminate allsteps underneath of it
            if (each not in words):
                continue
            
        '''Step 5: Cal tolerance_erro which is <= 25'''
        
        tolerance_error = counter/len(msg)*100 # pass only tolerance_error >= 25%

        '''Step to accomplish'''
        if (tolerance_error < 30):
            if (shift <= 25): #if does'nt pass it increases by 1 & empty shifted_alphabets to use again 
                shift += 1 
                shifted_alphabets = []
    
    #this prints final message
    for i in msg: print(i, end= ' ')



message = input("Enter your str msg to encript: ")
shift = int(input("Letters jump by: "))         
decription(message)
