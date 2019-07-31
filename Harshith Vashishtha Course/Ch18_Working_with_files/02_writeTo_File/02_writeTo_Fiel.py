# r -> read file as string
# a -> create unpresent file & append
# w -> create unpresent file & re-wrirte 
# r+ -> Not create unpresent file & over write by default from cudor position 0
#           although we overcome on it by moving cursor
#r  -> read present file

with open('write.txt', 'w') as f:   # w -> create unpresent file & re-wrirte 
    f.write("Hello there!")

with open('append.txt', 'a') as f:   # a -> create unpresent file & append
    f.write("Hello there!\n")

with open('read_plus.txt', 'r+') as f:   # r+ -> Not create unpresent file & over write 
    f.seek( len(f.read()) ) #read len of string and move cursor ahead
    f.write("Hello there!\n")  #tho; this work as append

with open('read.txt') as f:   # r -> read present file or open('read.txt', 'r')
    data = f.read()
    print(data)