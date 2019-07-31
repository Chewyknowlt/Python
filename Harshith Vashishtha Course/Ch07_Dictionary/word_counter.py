# using dict. it over write repeating key and value

def dic_word_count(string):
    s = string.lower()
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count

print(dic_word_count("Hamza"))