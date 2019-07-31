import os, shutil

def main():
  folderPath = input('Enter folder path: ') # r'/home/hamza/Downloads/Compressed'

  def finder(path, extensions):
    '''returrn generator of files from path of specific folder '''
    return (i for i in os.listdir(path) 
    for extension in extensions if i.endswith(extension))
  
  def file_process():
    #fileType : fileFormats
    file_extensions = {
      'audio' : ('.mp3', '.m4a', '.wav', '.flac'),
      'video' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
      'document' : ('.doc', '.pdf', '.txt'),
      'image' : ('.jpeg', '.jpg', '.png')
    }

    #make folder & path if they are not exist in spwcfic folder
    for fileType, fileFormats in file_extensions.items():
      folderName = f'{fileType.title()}(s)'    #make folderName
      newFolderPath = os.path.join(folderPath, folderName) #new path will use under 
      if folderName not in os.listdir(folderPath): #check folderName is not in specific specific path
        os.mkdir(newFolderPath) #this make folder

    #Separating each fileType into respective folder
    #e.g; image file into iamge(s) folder   
    for item in finder(folderPath, fileFormats):
      oldPath = os.path.join(folderPath, item)
      newPath = os.path.join(newFolderPath, item)
      shutil.move(oldPath, newPath)

  #Calling f()
  file_process()

if __name__ == '__main__':
  main()