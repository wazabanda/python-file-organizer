import os, shutil
#file extensions and folders
extensions = {
    #Audio files
    '.aif': 'Audio',
    '.cda': 'Audio',
    '.mid': 'Audio',
    '.midi': 'Audio',
    '.mp3': 'Audio',
    '.mpa': 'Audio',
    '.ogg': 'Audio',
    '.wav': 'Audio',
    '.wpl': 'Audio',
    '.wma': 'Audio',
    #compressed extensions
    '.7z': 'compressed',
    '.arj': 'compressed',
    '.deb': 'compressed',
    '.pkg': 'compressed',
    '.rar': 'compressed',
    '.rpm': 'compressed',
    '.tar.gz': 'compressed',
    '.z': 'compressed',
    '.zip': 'compressed',
    #Disc Images
    '.bin': 'Disc Images',
    '.dmg': 'Disc Images',
    '.iso': 'Disc Images',
    '.toast': 'Disc Images',
    '.vcd': 'Disc Images',
    #Data Files
    '.csv': 'Data and Database files',
    '.dat': 'Data and Database files',
    '.db': 'Data and Database files',
    '.dbf': 'Data and Database files',
    '.log': 'Data and Database files',
    '.mdb': 'Data and Database files',
    '.sav': 'Data and Database files',
    '.sql': 'Data and Database files',
    '.tar': 'Data and Database files',
    '.xml': 'Data and Database files',
    #emails
    '.email': 'Emails',
    '.eml': 'Emails',
    '.emlx': 'Emails',
    '.msg': 'Emails',
    '.oft': 'Emails',
    '.ost': 'Emails',
    '.pst': 'Emails',
    '.vcf': 'Emails',
    #executables
    '.apk': 'Executable',
    '.bat': 'Executable',
    '.cgi': 'Executable',
    '.pl': 'Executable',
    '.com': 'Executable',
    '.jar': 'Executable',
    '.exe': 'Executable',
    '.gadget': 'Executable',
    '.msi': 'Executable',
    '.wsf': 'Executable',
    #fonts
    '.fnt': 'fonts',
    '.fon': 'fonts',
    '.otf': 'fonts',
    '.ttf': 'fonts',
    #images
    '.ai': 'images',
    '.bmp': 'images',
    '.gif': 'images',
    '.ico': 'images',
    '.jpg': 'images',
    '.jpeg': 'images',
    '.png': 'images',
    '.ps': 'images',
    '.psd': 'images',
    '.svg': 'images',
    '.tiff': 'images',
    '.tif': 'images',
    '.krita': 'images',
    #internet files
    '.asp': 'webFiles',
    '.aspx': 'webFiles',
    '.cer': 'webFiles',
    '.cfm': 'webFiles',
    '.css': 'webFiles',
    '.htm': 'webFiles',
    '.html': 'webFiles',
    '.js': 'webFiles',
    '.jsp': 'webFiles',
    '.part': 'webFiles',
    '.php': 'webFiles',
    '.rss': 'webFiles',
    '.xhtml': 'webFiles',
    #presentation files
    '.key': 'presentations',
    '.odp': 'presentations',
    '.pps': 'presentations',
    '.ppt': 'presentations',
    '.pptx': 'presentations',
    #programing files
    '.c': 'programming files',
    '.class': 'programming files',
    '.cpp': 'programming files',
    '.cs': 'programming files',
    '.h': 'programming files',
    '.java': 'programming files',
    '.py2': 'programming files',
    '.pl': 'programming files',
    '.sh': 'programming files',
    '.swift': 'programming files',
    '.vb': 'programming files',
    #spread Sheets
    '.obs': 'spreadSheets',
    '.xls': 'spreadSheets',
    '.xlsm': 'spreadSheets',
    '.xlsx': 'spreadSheets',
    #system files
    '.bak': 'systemFiles',
    '.cab': 'systemFiles',
    '.cfg': 'systemFiles',
    '.cpl': 'systemFiles',
    '.cur': 'systemFiles',
    '.dll': 'systemFiles',
    '.dmp': 'systemFiles',
    '.drv': 'systemFiles',
    '.icns': 'systemFiles',
    '.ico': 'systemFiles',
    '.ini': 'systemFiles',
    '.ink': 'systemFiles',
    '.msi': 'systemFiles',
    '.sys': 'systemFiles',
    '.tmp': 'systemFiles',
    #video files
    '.3g2': 'videos',
    '.3gp': 'videos',
    '.avi': 'videos',
    '.flv': 'videos',
    '.h264': 'videos',
    '.m4v': 'videos',
    '.mkv': 'videos',
    '.mov': 'videos',
    '.mp4': 'videos',
    '.mpg': 'videos',
    '.mpeg': 'videos',
    '.rm': 'videos',
    '.swf': 'videos',
    '.vob': 'videos',
    '.wmv': 'videos',
    #documents
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.odt': 'Documents',
    '.pdf': 'Documents',
    '.rtf': 'Documents',
    '.tex': 'Documents',
    '.txt': 'Documents',
    '.wpd': 'Documents'
}
#create floders for different extensions
def organizefolder(folderDir):
    for extension in extensions.values():
        if extension not in os.listdir(folderDir):
            os.makedirs(os.path.join(folderDir,extension))
    #move files
    moveFiles(folderDir)

def moveFiles(folderDir):
    for file in os.listdir(folderDir):
        if os.path.isfile(os.path.join(folderDir,file)):
            for extension in extensions.keys():
                if file.endswith(extension):
                    shutil.move(os.path.join(folderDir,file),os.path.join(folderDir,extensions[extension]))
                    break
    deleteEmpty(folderDir)
def deleteEmpty(folderDir):
    for folder in os.listdir(folderDir):
        try:
            if os.path.isdir(os.path.join(folderDir,folder)):
                os.rmdir(os.path.join(folderDir,folder))
        except OSError:
            continue
#the argument passed for this function should be that of the folder you want to organize leave empty if you are cleaning the current file
organizefolder(os.getcwd())
