'''
class File - класс для обработки файлов

Дополнительные стандартные модули для обработки файлов
    shutil
    sys
    os.path
    os
    stat
    pathlib

Реализация методов класса - Максим Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# модуль для легкого копирования файлов и папок
# shutil.copyfileobj - копирование файлового объекта
# shutil.rmtree - удаление непустой папки/директории с носителя
import shutil
# модуль для работы с вводом и выводом в консоль
# sys.stdout - вывод информации в терминал (консоль)
# sys.platform - определение иммени платформы (операционной системы)
import sys
# импортируем молуль os.path
# dirname - определяем текущую директорию
# join - объеденяем директорию + файл (правильный путь файла)
from os.path import dirname, join
# импортируем молуль os
# os.stat(<file>).st_mode - получить состояние (права доступа) файла/папки в виде числа
# os.path.join(Path.home(), "Downloads") - получить путь/директорию к папке Downloads
import os
# импортируем молуль os
# remove - удаляет указанный файл
# listdir - получает все файлы и папки в текущей директории
# chmod - управление правами доступа у файлам и директориям
# mkdir - создание директории/папки
# rmdir - удаляет пустую папку/директорию
from os import remove, listdir, chmod, mkdir, rmdir
# импортируем молуль stat (работа с разрешениями прав доступа файлов и папок)
# stat.filemode - получить состояние (права доступа) файла/папки в виде строки (rwx)
# stat.S_IMODE - получить состояние (права доступа) файла/папки в виде числа (777)
# stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO - права доступа rwxrwxrwx (весь доступ разрешен)
# stat.S_ENFMT - права доступа -----S--- (весь доступ запрещен)
import stat
# импортируем молуль pathlib
# Path - задает путь к файлу
from pathlib import Path
# *****************************************************************************************
# класс для работы с файлом
class File:
    '''
    class File - класс для обработки файлов
    методы:
        file_create_dir(dir: str) -> bool
        file_delete(file: str) -> bool
        file_delete_empty_folder(file: str) -> bool
        file_delete_full_folder(file: str) -> bool
        file_name_init(folder: str, filename: str) -> str
        file_get_current_dir_files() -> list[str]
        file_get_dir_files(dir: str) -> list[str]
        file_get_current_access_dir_in_str() -> list[str]
        file_get_current_access_dir_in_int() -> list[int]
        file_get_path_to_downloads() -> str
        file_set_access_open_all(name: str) -> bool
        file_set_access_close_all(name: str) -> bool
        file_read(file: str) -> list[str] 
        file_read_utf8(file: str) -> list[str]  
        file_write(file: str, arr: list) -> None  
        file_write_append(file: str, arr: list) -> None 
        file_write_dict(file: str, dictor: dict) -> None  
        file_list_console(arr: list) -> None   
        file_print_console_utf8(file: str) -> None 
    '''
    # ---------------------------------------------------------------------------
    # создать указанную папку/директорию
    def file_create_dir(self, dir: str) -> bool:
        '''
        file_create_dir(dir: str) -> bool\n                      
                создает указанную папку/директорию\n             
                возвращаемое значение - bool (True - создано, False - ошибка)\n    
        параметры:\n                                                
                dir: str - имя папки/директории которое неоходимо создать\n                        
        '''
        try:
            # определить имя создаваемой папки/директории
            dir_name = self.file_name_init('', dir)
            # создать папку/директорию
            mkdir(dir_name)
            return True
        except (Exception) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # удаление файла с носителя
    def file_delete(self, file: str) -> bool:
        '''
        file_delete(file: str) -> bool\n                      
                удаление файла с носителя\n             
                возвращаемое значение - bool (True - удалено, False - ошибка)\n    
        параметры:\n                                                
                file: str - имя файла которое неоходимо удалить с носителя\n                        
        '''
        try:
            # определить имя удаляемого файла
            file_name = self.file_name_init('', file)
            # delete file
            remove(file_name)
            return True
        except (FileNotFoundError) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # удаление пустой папки/директории с носителя
    def file_delete_empty_folder(self, dir: str) -> bool:
        '''
        file_delete_empty_folder(file: str) -> bool\n                      
                удаление пустой папки/директории с носителя\n             
                возвращаемое значение - bool (True - удалено, False - ошибка)\n    
        параметры:\n                                                
                dir: str - имя пустой папки/директории которое\n   
                    неоходимо удалить с носителя\n                        
        '''
        try:
            # определить имя удаляемой папки/директории
            dir_name = self.file_name_init('', dir)
            # delete folder
            rmdir(dir_name)
            return True
        except (OSError) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # удаление непустой папки/директории с носителя
    # также удаляет пустую папку/директорию
    def file_delete_full_folder(self, dir: str) -> bool:
        '''
        file_delete_full_folder(file: str) -> bool\n                      
                удаление непустой папки/директории с носителя\n  
                    (также удаляет пустую папку/директорию)\n            
                возвращаемое значение - bool (True - удалено, False - ошибка)\n    
        параметры:\n                                                
                dir: str - имя непустой папки/директории которое\n   
                    неоходимо удалить с носителя\n                        
        '''
        try:
            # определить имя удаляемой папки/директории
            dir_name = self.file_name_init('', dir)
            # delete folder
            shutil.rmtree(dir_name)
            return True
        except (Exception) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # инициализация полного имени файла (директория + имя файла)
    def file_name_init(self, folder: str, filename: str) -> str:
        '''
        file_name_init(folder: str, filename: str) -> str\n   
                инициализация полного имени файла\n                   
                    (директория + имя файла)\n                        
                возвращаемое значение - str (строка)\n                
        параметры:\n                                                
                folder: str - создать директорию в текущей папке\n    
                filename: str - создать файл в директории folder\n    
        '''
        # определяем текущую директорию, гбе будет храниться файл
        CURRENT_DIR = dirname(__file__)
        # задаем имя папки (директории)
        FOLDER = folder
        # задаем имя файла для чтения/записи данных
        FILENAME = filename
        # объединяем текущую директорию и файл
        FILE_PATH = join(CURRENT_DIR, FOLDER + FILENAME)
        # определяем тип FILE_PATH
        # print('FILE_PATH :', type(FILE_PATH))
        # возвращаеи полное имя файла (директория + имя файла)
        return FILE_PATH
    # ---------------------------------------------------------------------------
    # получить все файлы и папки в текущей директории
    def file_get_current_dir_files(self) -> list[str]:
        '''
        file_get_current_dir_files() -> list[str]\n              
                получает все файлы и папки в текущей директории\n             
                возвращаемое значение - list[str] (список строк)\n    
        параметры:\n                                            
                нет параметров\n                        
        '''
        files_arr = listdir()
        return files_arr
    # ---------------------------------------------------------------------------
    # получить все файлы и папки в указанной директории
    def file_get_dir_files(self, dir: str) -> list[str]:
        '''
        file_get_dir_files(dir: str) -> list[str]\n               
                получает все файлы и папки в указанной директории\n           
                возвращаемое значение - list[str] (список строк)\n                
        параметры:\n                                                
                dir: str - имя директории которую необходимо показать\n                
        '''
        # определить имя директории
        dir_name = self.file_name_init('', dir)
        # получить все файлы и папки в указанной директории
        files_arr = listdir(dir_name)
        return files_arr
    # ---------------------------------------------------------------------------
    # получить все установленные права доступа файлов в текущей директории
    # в виде str (rwx)
    def file_get_current_access_dir_in_str(self) -> list[str]:
        '''
        file_get_current_access_dir_in_str() -> list[str]\n                       
                получает все установленные права доступа файлов\n 
                    в текущей директории в виде str (rwx)\n 
                возвращаемое значение - list[str] (список строк)\n    
        параметры:\n                                              
                нет параметров\n                        
        '''
        # массив установленных разрешений для файлов и папок
        access_arr = list()
        # заполняем массив установленныз разрешений для файлов и папок
        for file in self.file_get_current_dir_files():
            # Определим установленные разрешения в виде букв -rwx
            access_arr.append(stat.filemode(os.stat(file).st_mode))
        # return
        return access_arr
    # ---------------------------------------------------------------------------
    # получить все установленные права доступа файлов в текущей директории
    # в виде int (777)
    def file_get_current_access_dir_in_int(self) -> list[int]:
        '''
        file_get_current_access_dir_in_int() -> list[int]\n                       
                получает все установленные права доступа файлов\n 
                    в текущей директории в виде int (777)\n 
                возвращаемое значение - list[int] (список чисел)\n    
        параметры:\n                                              
                нет параметров\n                        
        '''
        # массив установленных разрешений для файлов и папок
        access_arr = list()
        # заполняем массив установленныз разрешений для файлов и папок
        for file in self.file_get_current_dir_files():
            # Определим установленные разрешения в виде чисел - int (777)
            access_arr.append(stat.S_IMODE(os.stat(file).st_mode))
        # return
        return access_arr
    # ---------------------------------------------------------------------------
    # получить путь/директорию к папке Downloads
    def file_get_path_to_downloads(self) -> str:
        '''
        file_get_path_to_downloads() -> str\n                       
                получает путь/директорию к папке Downloads\n 
                возвращаемое значение - str (строка)\n   
        параметры:\n                                              
                нет параметров\n                        
        '''
        # if android
        if hasattr(sys, 'getandroidapilevel'):
            # получить Download путь к каталогу в Android
            from android.storage import primary_external_storage_path
            dir = primary_external_storage_path()
            downloads_path = os.path.join(dir, './Download/')
            return downloads_path
        # if linux and freebsd and macosx
        elif (sys.platform.startswith("linux") or 
                sys.platform.startswith("linux2") or
                sys.platform.startswith("freebsd") or
                sys.platform == "darwin"):
            # downloads_path = str(Path.home()/"Downloads")
            # downloads_path = str(os.path.join(Path.home(), "Downloads"))
            downloads_path = str(os.path.join(Path.home(), "./Downloads/"))
            return downloads_path
        # if windows
        elif sys.platform in ("win", "win32", "win64", "cygwin"):
            # работа с реестром windows
            import winreg
            with winreg.OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
                downloads_path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
            return downloads_path
        # if unknown
        else:
            # создаем свое исключение
            class file_get_path_to_downloads_ERROR(BaseException):
                pass
            try:
                raise file_get_path_to_downloads_ERROR
            except (file_get_path_to_downloads_ERROR) as e:
                print(e, ' OS is unknown')
            # return 'unknown'
    # ---------------------------------------------------------------------------
    # разрешить весь доступ к указанному файлу/директории
    def file_set_access_open_all(self, name: str) -> bool:
        '''
        file_set_access_open_all(name: str) -> bool\n                      
                разрешает весь доступ к указанному файлу/директории\n             
                возвращаемое значение - bool (True - доступ разрешен, False - ошибка)\n    
        параметры:\n                                                
                name: str - имя папки/директории к которому нужно разрешить доступ\n                        
        '''
        try:
            # определить имя файла/директории
            dir_file_name = self.file_name_init('', name)
            # определяем текущие права файла
            # permissions = os.stat(dir_file_name).st_mode
            # Convert a file's mode to a string of the form '-rwxrwxrwx'
            # permissions = stat.filemode(permissions)
            # задаем новые права доступа к файлу (разрешаем доступ)
            new_permissions = stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO
            chmod(dir_file_name, new_permissions)
        except (PermissionError) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # запретить весь доступ к указанному файлу/директории
    def file_set_access_close_all(self, name: str) -> bool:
        '''
        file_set_access_close_all(name: str) -> bool\n                      
                запрещает весь доступ к указанному файлу/директории\n             
                возвращаемое значение - bool (True - доступ запрещен, False - ошибка)\n    
        параметры:\n                                                
                name: str - имя папки/директории к которому нужно запретить доступ\n                        
        '''
        try:
            # определить имя файла/директории
            dir_file_name = self.file_name_init('', name)
            print(dir_file_name) #####################################
            # определяем текущие права файла
            # permissions = os.stat(dir_file_name).st_mode
            # Convert a file's mode to a string of the form '-rwxrwxrwx'
            # permissions = stat.filemode(permissions)
            # задаем новые права доступа к файлу (запрещаем доступ)
            new_permissions = stat.S_ENFMT
            chmod(dir_file_name, new_permissions)
        except (PermissionError) as e:
            # show msg except
            # print(e)
            return False
    # ---------------------------------------------------------------------------
    # чтение содержимого файла построчно
    def file_read(self, file: str) -> list[str]:
        '''
        file_read(file: str) -> list[str]\n                         
                читает информацию из файла построчно\n                
                возвращаемое значение - list[str] (список строк)\n    
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    и прочитать\n                             
        '''
        # определить имя файла
        file_name = self.file_name_init('', file)
        # открыть файл и прочитать построчно
        with open(file_name, 'r') as f:
            return f.readlines()
    # ---------------------------------------------------------------------------
    # чтение содержимого файла содержащий текст в utf-8 кодировке
    def file_read_utf8(self, file: str) -> list[str]:
        '''
        file_read_utf8(file: str) -> list[str]\n                    
                читает информацию из файла в utf-8 кодировке\n        
                возвращаемое значение - list[str] (список строк)\n    
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    и прочитать\n                             
        '''
        # определить имя файла
        file_name = self.file_name_init('', file)
        # var
        str_byte = None
        # открыть файл и прочитать текст в utf-8 кодировке
        with open(file_name, 'r', encoding='utf-8') as f:
            # shutil.copyfileobj(f, str_byte.extend)
            str_byte = f.read().encode('utf-8')
        # print(repr(str(str_byte, 'utf-8')))
        return str(str_byte, 'utf-8').split('\n')
    # ---------------------------------------------------------------------------
    # запись содержимого списка (list) в файл
    def file_write(self, file: str, arr: list) -> None:
        '''
        file_write(file: str, arr: list) -> None\n                  
                запись содержимого списка (list) в файл\n             
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    для записи содержимого списка\n           
                arr: list - список для записи в файл\n                
        '''
        # определить имя файла
        file_name = self.file_name_init('', file)
        # в списке к концу строк добавляем \n (переход на новую строку)
        for i in range(len(arr)):
            arr[i] += '\n'
        # создаем файл и записываем содержимое списка
        with open(file_name, 'w') as f:
            f.writelines(arr)
    # ---------------------------------------------------------------------------
    # дозапись содержимого списка (list) в файл
    def file_write_append(self, file: str, arr: list) -> None:
        '''
        file_write_append(file: str, arr: list) -> None\n                  
                дозапись содержимого списка (list) в файл\n             
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    для дозаписи содержимого списка\n           
                arr: list - список для дозаписи в файл\n                
        '''
        # определить имя файла
        file_name = self.file_name_init('', file)
        # в списке к концу строк добавляем \n (переход на новую строку)
        for i in range(len(arr)):
            arr[i] += '\n'
        # открываем файл и дозаписываем содержимое списка
        with open(file_name, 'a') as f:
            f.writelines(arr)
    # ---------------------------------------------------------------------------
    # запись содержимого словаря (dict) в файл
    def file_write_dict(self, file: str, dictor: dict) -> None:
        '''
        file_write_dict(file: str, dictor: dict) -> None\n          
                запись содержимого словаря (dict) в файл\n            
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть\n     
                    для записи содержимого словаря\n          
                dictor: dict - словарь для записи в файл\n            
        '''
        # определить имя файла
        file_name = self.file_name_init('', file)
        # создать файл и записать содержимое словаря (хэш таблицы)
        with open(file_name, 'w') as f:
            for k,v in dictor.items():
                f.write(f'{k} {v}\n')
    # ---------------------------------------------------------------------------
    # вывод в консоль содержимого списка (list)
    def file_list_print_console(self, arr: list) -> None:
        '''
        file_list_console(arr: list) -> None\n                      
                вывод в консоль содержимого списка (list)\n           
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                arr: list - список для вывода в консоль\n          
        '''
        for line in arr:
            # print(line.strip())
            # print(repr(line))
            # print(line, end='')
            print(line)
    # ---------------------------------------------------------------------------
    # вывод в консоль содержимого файла содержащий текст в utf-8 кодировке 
    # (аналог type filename в cmd.exe)
    def file_print_console_utf8(self, file: str) -> None:
        '''
        file_print_console_utf8(file: str) -> None\n                
                вывод в консоль содержимого файла содержащий\n        
                    текст в utf-8 кодировке\n                         
                возвращаемое значение - None (None)\n                 
        параметры:\n                                                
                file: str - имя файла которое неоходимо открыть,\n    
                    прочитать и вывести в консоль\n           
        '''
        # определить имя файла
        file_name = self.file_name_init('', file)
        # открыть файл, скопировать содержимое в консоль (терминал)
        with open(file_name, 'r', encoding='utf-8') as f:
            shutil.copyfileobj(f, sys.stdout)
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тест
# если не модуль, то выполнить
if __name__ == '__main__':
    # функция для тестов
    def main():
        # ---------------------------------------------------------------------------
        # определяем текущую директорию, гбе будет храниться файл
        CURRENT_DIR = dirname(__file__)
        # задаем имя папки (директории)
        FOLDER = './temp/'
        # задаем имя файла для чтения данных
        FILENAME_READ = 'test_read.txt'
        # объединяем текущую директорию и файл для чтения
        FILE_PATH_READ = join(CURRENT_DIR, FOLDER + FILENAME_READ)
        # задаем имя файла для вывода результатов
        FILENAME_WRITE = 'test_write.txt'
        # объединяем текущую директорию и файл для записи
        FILE_PATH_WRITE = join(CURRENT_DIR, FOLDER + FILENAME_WRITE)
        # создаем объект
        f = File()
        # ---------------------------------------------------------------------------
        # чтение файла построчно
        print('----------чтение файла построчно----------')
        arr = f.file_read(FILE_PATH_READ)
        # вывод в консоль
        print(*arr, sep='')
        # ---------------------------------------------------------------------------
        # чтение содержимого файла содержащий текст в utf-8 кодировке
        print('----------чтение содержимого файла содержащий текст в utf-8 кодировке----------')
        arr = f.file_read_utf8(FILE_PATH_READ)
        # вывод в консоль
        print(*arr, sep='\n')
        # ---------------------------------------------------------------------------
        # запись содержимого списка (list) в файл
        print('----------запись содержимого списка (list) в файл----------')
        f.file_write(FILE_PATH_WRITE, arr)
        print('запись содержимого произведена')
        # ---------------------------------------------------------------------------
        # дозапись содержимого списка (list) в файл
        print('----------запись содержимого списка (list) в файл----------')
        f.file_write_append(FILE_PATH_WRITE, ['a', 'b', 'c'])
        print('дозапись содержимого произведена')
        # ---------------------------------------------------------------------------
        # запись содержимого словаря (dict) в файл
        print('----------запись содержимого словаря (dict) в файл----------')
        dictor = dict(zip((1, 2, 3, 4, 5),('a', 'b', 'c', 'd', 'e')))
        f.file_write_dict(FILE_PATH_WRITE, dictor)
        print('запись содержимого произведена')
        # ---------------------------------------------------------------------------
        # вывод в консоль содержимого списка (list)
        print('----------вывод в консоль содержимого списка (list)----------')
        arr = list(range(10, 21))
        f.file_list_print_console(arr)
        # ---------------------------------------------------------------------------
        # вывод в консоль содержимого файла содержащий текст в utf-8 кодировке 
        print('----------вывод в консоль содержимого файла содержащий текст в utf-8 кодировке----------')
        f.file_print_console_utf8(FILE_PATH_READ)
        # ---------------------------------------------------------------------------
        # инициализация полного имени файла (директория + имя файла)
        print('----------инициализация полного имени файла (директория + имя файла)----------')
        file_name = f.file_name_init('./temp/', 'test_read.txt')
        print(file_name)
        print(type(file_name))
        # ---------------------------------------------------------------------------
        # удаление файла с носителя
        file_name = f.file_name_init('./temp/', 'test_write.txt')
        print('----------удаление файла с носителя----------')
        if (f.file_delete(file_name)):
            print(f'Файл {file_name} удален')
        else:
            print('Ошибка удаления')
        # ---------------------------------------------------------------------------
        # получить все файлы и папки в текущей директории
        print('----------получить все файлы и папки в текущей директории----------')
        print(f.file_get_current_dir_files())
        # ---------------------------------------------------------------------------
        # получить все установленные права доступа файлов виде str (rwx)
        print('----------получить все установленные права доступа файлов виде str (rwx)----------')
        print(f.file_get_current_access_dir_in_str())
        # ---------------------------------------------------------------------------
        # получить все установленные права доступа файлов виде int (777)
        print('----------получить все установленные права доступа файлов виде int (777)----------')
        print(f.file_get_current_access_dir_in_int())
        # ---------------------------------------------------------------------------
        # создать указанную папку/директорию
        print('----------создать указанную папку/директорию----------')
        f.file_create_dir('./temp/new_dir_1/')
        dir = f.file_name_init('./temp/', './new_dir_2/')
        f.file_create_dir(dir)
        print(f.file_get_current_dir_files())
        # ---------------------------------------------------------------------------
        # разрешить весь доступ к указанному файлу/директории
        print('----------разрешить весь доступ к указанному файлу/директории----------')
        f.file_write('./temp/open.txt', ['test'])
        f.file_set_access_open_all('./temp/open.txt')
        # ---------------------------------------------------------------------------
        # запретить весь доступ к указанному файлу/директории
        print('----------запретить весь доступ к указанному файлу/директории----------')
        f.file_set_access_close_all('./temp/open.txt')
        # ---------------------------------------------------------------------------
        # получить все файлы и папки в указанной директории
        print('----------получить все файлы и папки в указанной директории----------')
        print(f.file_get_dir_files('./temp/'))
        # ---------------------------------------------------------------------------
        # удаление пустой папки/директории с носителя
        print('----------удаление пустой папки/директории с носителя----------')
        if (f.file_delete_empty_folder('./temp/new_dir_2/')):
            print('Пустая директория удалена')
        else:
            print('Ошибка удаления')
        # ---------------------------------------------------------------------------
        # удаление непустой папки/директории с носителя
        # также удаляет пустую папку/директорию
        print('----------удаление непустой папки/директории с носителя----------')
        if (f.file_delete_full_folder('./temp/new_dir_1/')):
            print('Непустая директория удалена')
        else:
            print('Ошибка удаления')
        # ---------------------------------------------------------------------------
        # получить путь/директорию к папке Downloads
        print('----------получить путь/директорию к папке Downloads----------')
        print(f.file_get_path_to_downloads())
        # ---------------------------------------------------------------------------
    # выполнить тест
    main()
# *****************************************************************************************