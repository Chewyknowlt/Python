# data tranfer from trafer.txt to reciever.txt
transfer = r'B:\Python Course\Ch18_Working_with_files\03_dataTranfer_1file_to_2file\transfer.txt'
reciever = r'B:\Python Course\Ch18_Working_with_files\03_dataTranfer_1file_to_2file\reciever.txt'

with open(transfer, 'r') as rf:
    with open(reciever, 'w') as wf:
        wf.write( rf.read() )
