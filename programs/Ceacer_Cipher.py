### Ceaser Cipher Cracker

def encription(message, shift):

    ''' Step 1: Split each char into str & put it in lst'''
    #Split str & puttingg in lst
    message  = [individual for individual in message.lower()]

    ''' Step 2: Menupulate original lst by shifting through index '''
    #total list size of 26, indexing 0-25
    alphabets = ['a', 'b', 'c', 'd', 'e',
 	         'f', 'g', 'h', 'i', 'j',
	   	 'k', 'l', 'm', 'n', 'o',
	   	 'p', 'q', 'r', 's', 't',
	   	 'u', 'v', 'w', 'x', 'y', 'z']
    
    # append lst = alphabets from giving indexin e.g; from 2 means it appends
    # untill a & b left untouched
    i = shift
    shifted_alphabets = [] # TO catch alphabets in lst
    while i < len(alphabets): # this appends c-z where a & b remian left.
        shifted_alphabets.append(alphabets[i])
        i += 1

    #Appending remainig values e.g; for shift = 2-> this appends a & b
    i = 0
    while i < shift:
        shifted_alphabets.append(alphabets[i])
        i += 1
    print(shifted_alphabets)
    
    '''Step 3: find index position of char from org lst = alphabets
               & placed those index no.into modified lst =  shifed_lst
               e.g;
               shift = 2
               character = 'c', index in org lst = alphabets[2] <- [2] this 2 will be used
                 to place in modified lst = Shifted_alphabets'''
    # ALL spaces are here to treat in here
    spaces = [' ', '\r', '  ', '   ', '\t', '\n'] 
    for character in message:
        if (character in spaces):
            print(character, end = '')#print spaces
            continue # <- statement terminate allsteps beneath under expression
        
        i = 0 # init for all character
        while (character != alphabets[i]): # find character index in org. lst = alphabets
            i += 1 
        if (character == alphabets[i]): # using org index placed in modified lst = shifted_alphabets
            print(shifted_alphabets[i] , end = '')
    
message = input("Enter your str msg to encript: ")
shift = int(input("Letters jump by: "))         


encription(message, shift)
#decription(message)

















































