#Read emojis
emoji = r'B:\Python Course\Ch18_Working_with_files\06_Read_love_story\06_read_emoji.txt'
with open(emoji, 'r', encoding = 'utf-8') as f:
    f.encoding()
    data = f.read()
    print(data)