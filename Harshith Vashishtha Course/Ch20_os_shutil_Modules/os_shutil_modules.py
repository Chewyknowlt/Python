import os, shutil
# # DIRECTORY
# #os.getcwd()  -> current working dir 
# print(os.getcwd())

# #os.chdir(<PATH>)  -> change dir
# os.chdir(r'B:\Python Course\Ch20_OS_Module')
# # =============================

# # FOLDER
# #os.mkdir(<FolderNameOrPATH>)   -> make folder in current dirrectory if folder exist it throws error
# os.mkdir('test1')

## os.makedirs(<FFOLDER1/FOLDER2/... >) Make folder inside folder
# os.makedirs('this/those')

# # os.path.exists('<Folder>')   ->  check of existance of folder on basis of T/F
# print(os.path.exists('teast1'))

# #creating folder if it doesnt exist
# if not  os.path.exists('test1'):
#     os.mkdir('test1')

# #make folder to other directory
# #  os.mkdir(<PATH>/<FolderToCreate>)   -> make folder to dir 
# os.mkdir(r'B:\\Python Course\Ch20_OS_Module\this')
# # ================================================

# #FILE
# # open(<FILE>, 'a').close() -> Creating file if not exists else nor give  eror
# open('this.txt', 'a').close
##===============================================

# #LIST
# # os.listdir()   -> list of current files&folder
# print(os.listdir())

# # os.listdir(<PATH>)   ->List of specified dir
# print( os.listdir(r'B:\Python Course\Ch20_OS_Module') )

# # PATH
# #  os.path() -> take path & join() -> path + item
# path = r'B:\Python Course'   #Current path -> os.getcwd()
# for item in  os.listdir(path):
#   workingPath =   os.path.join(path, item)
#   print(workingPath)

## os.walk() -> deelply list of each file&folder or deep walkthrough
# path = (r'B:\Python Course\Ch20_OS_Module')
# for currentPath, folder, file in os.walk(path):
#     print(f'Current Path: {currentPath}')
#     print(f'Folder: {folder}')
#     print(f'File: {file}')
## ==========================================

##DELETE
## os.rmdir(<OnlyEmptyFolder>)
# os.rmdir('this')

## shutil.rmtree(<FolderThatContainFiles>) ->Permanent delete dir conating files
# shutil.rmtree('this')
## ===================================================

##COPY & RENAME
##  shutil.copytree(<copyPATH>,<pastePATH/<Rename/Name>> ) -> Copy&Rename Folder
# shutil.copytree(r'B:\Python Course\Ch20_OS_Module\this\those', r'B:\Python Course\Ch20_OS_Module/copyThis' )

## shutil.copy(<copyPath\FILE>, <pastePath/RenameFileOrFile>) -> copy file
# shutil.copy(r'B:\Python Course\Ch20_OS_Module\01_OS_1\this\file.txt', r'B:\Python Course\Ch20_OS_Module\01_OS_1/f.txt' )
## ===============================================================================

##MOVE & RENAME
## shutil.move(<movePath>, <pastePath/Rename>)   -> this move path  of file or folder
# shutil.move(r'B:\Python Course\Ch20_OS_Module\01_OS_1\this', r'B:\Python Course\Ch20_OS_Module/that')
##======================================================================