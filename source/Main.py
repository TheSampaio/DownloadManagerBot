# Version 1.4

import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from Config import *


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        pass

    @staticmethod
    def on_modified(event):
        if os.path.isdir(event.src_path):
            return

        if is_image_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('00 - Images')
            elif language == 'pt':
                path_to_folder = make_folder('00 - Imagens')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_video_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('01 - Videos')
            elif language == 'pt':
                path_to_folder = make_folder('01 - Vídeos')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_mp3_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('02 - Sounds')
            elif language == 'pt':
                path_to_folder = make_folder("02 - Áudios")
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_pdf_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('03 - PDFs')
            elif language == 'pt':
                path_to_folder = make_folder("03 - PDFs")
            move_to_new_corresponding_folder(event, path_to_folder)
            return 

        elif is_doc_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('04 - Words')
            elif language == 'pt':
                path_to_folder = make_folder('04 - Words')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_spreadsheet_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('05 - Spread Sheets')
            elif language == 'pt':
                path_to_folder = make_folder('05 - Tabelas')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_presentation_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('06 - Slides')
            elif language == 'pt':
                path_to_folder = make_folder('06 - Slides')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_text_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('07 - Texts')
            elif language == 'pt':
                path_to_folder = make_folder('07 - Textos')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_code_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('08 - Codes')
            elif language == 'pt':
                path_to_folder = make_folder('08 - Códigos')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_executable_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('09 - Executables')
            elif language == 'pt':
                path_to_folder = make_folder('09 - Executáveis')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_compacted_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('10 - Compresseds')
            elif language == 'pt':
                path_to_folder = make_folder('10 - Compactados')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        elif is_invoice_file(event) == True:
            if language == 'en':
                path_to_folder = make_folder('11 - Invoices')
            elif language == 'pt':
                path_to_folder = make_folder('11 - Notas Fiscais')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

        else:
            if language == 'en':
                path_to_folder = make_folder("12 - Others")
            elif language == 'pt':
                path_to_folder = make_folder('12 - Outros')
            move_to_new_corresponding_folder(event, path_to_folder)
            return

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        pass


file_change_handler = Handler()
observer = Observer()
os.chdir('{}\\Downloads'.format(user))
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False,)
observer.start()

try:
    while True:
        sleep(1)

except:
    observer.join()
