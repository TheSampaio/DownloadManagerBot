import shutil
import os
from time import sleep

user = os.environ['USERPROFILE']
activeTime = 8

def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_text_file(event):
    if extension_type(event) == 'txt':
        return True
    return False


def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_mp3_file(event):
    if extension_type(event) == 'mp3':
        return True
    return False


def is_image_file(event):
    if extension_type(event) in ('png', 'jpg', 'jpeg', 'bmp', 'gif', 'raw'):
        return True
    return False


def is_video_file(event):
    if extension_type(event) in ('mov', 'mp4', 'avi', 'flv'):
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx'):
        return True
    return False


def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx'):
        return True
    return False


def is_compacted_file(event):
    if extension_type(event) in ('rar', 'zip', '7z', 'iso'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in ('py', "jl", 'cs', 'js', 'php', 'html', 'sql', 'css', 'c', 'h', 'cpp', 'java', 'asp', 'aspx', 'axd', 'asx', 'asmx', 'ashx', 'cfm', 'yaws', 'swf', 'htm', 'xhtml', 'jhtml', "jsp", "jspx", "wss", "do", "cmd", "action", "pl", "phtml", "php3", "php4", "rb", "rhtml", "shtml", "rss", "svg", ):
        return True
    return False

def is_chit_file(event):
    if extension_type(event) in ('xml'):
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi'):
        return True
    return False


def make_folder(foldername):
    os.chdir('{}\\Downloads'.format(user))
    
    if os.path.exists(foldername) == True:
        print('\nA pasta destino já existe, pulando criação')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        print('\nMovendo arquivo em {} segundos...'.format(activeTime))
        sleep(activeTime / 2)

        print('Movendo o arquivo em {} segundos...'.format(activeTime / 2))
        sleep(activeTime / 2)

        shutil.move(event.src_path, path_to_new_folder)
        print('\nArquivo movido com sucesso')

    except:
        print('\nO arquivo já existe na pasta de destino')
        pass
