import shutil
from pathlib import Path


class OrganizeDirectory:
    """
    This class is used to organize the directory.
    """

    def __init__(self ):



        self.ext_directories = {
            '.img' : 'Images',
            '.jpg' : 'Images',
            '.pdf' : 'Documents',
            '.doc' : 'Documents',
            'docx' : 'Documents',
            'png' : 'Images',
            'txt' : 'Documents',
            '.mp3' : 'Music',
            'zip' : 'compressed',
                    }
    def __call__(self, directory ):
            directory = Path(directory)

            if not directory.exists():
                raise FileNotFoundError(f"{directory} does not exist.")

            files_extention = []

            for file_path in directory.iterdir():
                if file_path.is_dir():
                    continue
                    
                #ingore hidden files
                if file_path.name.startswith('.'):
                    continue
                    
                    
                #get all files
                files_extention.append(file_path.suffix)
                
                
                if file_path.suffix not in self.ext_directories:
                    DES_DIR =directory / 'othres'
                else:    
                    DES_DIR  = directory / self.ext_directories[file_path.suffix]
                

                DES_DIR.mkdir(exist_ok =True)
                print(f'{file_path.suffix:10}{DES_DIR}')
                shutil.move(str(file_path), str(DES_DIR))





if __name__ == '__main__':
    org_file = OrganizeDirectory()
    org_file('/home/Yourspecialname/Desktop/test')  #it's  an example
    print("Done!")


        