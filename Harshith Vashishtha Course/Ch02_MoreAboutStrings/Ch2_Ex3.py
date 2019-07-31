#take 2 inputs, 1 is for name, 2nd for required char
#count len of name
#count character insesitively(e.g; "A" or "a")

name, query_char = input("Enter name & a character separated by ','  ").split(',') #multy inputs
#use len([]), [].count([]),  [].lower() [].strip()
print(f"Length: {len(name.strip().lower())} \nRequired Character: {name.strip().lower().count(query_char.strip().lower())}")
# name.strip().lower().count(char_query.strip().lower())
