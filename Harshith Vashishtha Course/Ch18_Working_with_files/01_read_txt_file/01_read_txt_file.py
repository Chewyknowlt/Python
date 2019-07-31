file = r'B:\Python Course\Ch18_Working_with_files\01_read_txt_file.txt'
with open(file) as f: # Passing no arg with open(filePath, Mode) -> by default 'r' read
    print(f'Cursor: {f.tell()}')  #[].tell() ->current cursor position
    print(f.read())  # [].read() ->Read whole data
    print(f'Cursor: {f.seek(0)}') #[].tell([]) -> Moving cursor to position in  arg
    print(f.readline(), end = '')     #[].readline() ->read only 1 line, end = '' -> remove space
    f.close() #[].close() ->always close file after working

print()
with open(file, 'r') as f:   #instead of 'r' use 'w' to write
        lines  = f.readlines() [:2]  #[].readlines() -> make lst containes all lines with slixing
        for  num, line in enumerate(lines):
            print(f'{num+1}.  {line}', end = '')
        f.close()
        print(f.name) # [].name -> name of file
        print(f.closed)  # [].closed -> check file has closed (True/False) 
# 2 descrypters 
#  [].closed  -> check file has closed
# [].name -> name of file (True/False)