# Paractice Problem 3.10

def noVowel(x):
    for c in x:
        if c in 'aeiouAEIOU':
            return False
        return True
