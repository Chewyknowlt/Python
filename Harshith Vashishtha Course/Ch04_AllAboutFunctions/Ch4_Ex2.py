# Palindrome

def similar_palindrome(word):
    return  word.lower() == word[::-1].lower()

print(similar_palindrome("Madam")) # true
print(similar_palindrome("This")) # false