transfer = r"B:\Python Course\Ch18_Working_with_files\Ch18_Ex1\Ch18_Ex1_transfer.txt"
reciever = r"B:\Python Course\Ch18_Working_with_files\Ch18_Ex1\Ch18_Ex1_reciever.txt"

with open(transfer, 'r') as rf:
    with open(reciever, 'w') as wf:
        for line in rf.readlines():
            name, salary = line.strip().split(',')
            parse = f"\n{name}\'s salary is {salary} "
            wf.write(parse)
        wf.close()
    rf.close() 
