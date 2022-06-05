'''
Определение названия ОС

Алгоритм определения названия операционной системы
    импортируем модуль sys (Модуль sys предоставляет программисту набор функций, 
    которые дают информацию о том, как интерпретатор Python взаимодействует 
    с операционной системой.)
    вызываем sys.platform - строка, дающая информацию об используемой операционной системе 
    (идентификатор платформы)
    для определения android используем hasattr(sys, 'getandroidapilevel'):

Реализация алгоритма - Максим Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# импорт модуля sys (Модуль sys предоставляет программисту набор функций, 
# которые дают информацию о том, как интерпретатор Python взаимодействует 
# с операционной системой.)
# sys.platform - строка, дающая информацию об используемой операционной системе 
# (идентификатор платформы)
import sys
from sys import platform as _platform
# также можно узнать через фреймворк kivi - название ОС 
# from kivy.utils import platform
# *****************************************************************************************
# класс - определение имени ОС
class OsName:
    '''
    class OsName - Определение названия ОС    
    методы:                                                  
        os_name_get() -> str                                 
    '''
    # ---------------------------------------------------------------------------
    # метод - определяем имя ОС
    def os_name_get(self) -> str:
        '''
        os_name_get() -> str\n                                 
                возвращает имя ОС\n                
                возвращаемое значение - str (текстовая строка)\n  
                возвращаемые str значения:\n 
                        android\n 
                        linux\n 
                        freebsd\n 
                        macosx\n 
                        windows\n 
                        unknown\n 
        '''
        if hasattr(sys, 'getandroidapilevel'):
            # android
            # print('android')
            return 'android'
        elif _platform.startswith("linux") or _platform.startswith("linux2"):
            # linux
            # print('linux')
            # print(_platform)
            return 'linux'
        elif _platform.startswith("freebsd"):
            # linux
            # print('linux')
            # print(_platform)
            return 'freebsd'
        elif _platform == "darwin":
            # MAC OS X
            # print('Mac OS')
            # print(_platform)
            return 'macosx'
        elif _platform in ("win", "win32", "win64", "cygwin"):
            # Windows
            # print('Windows')
            # print(_platform)
            return 'windows'
        else:
            # unknown
            # print('unknown')
            return 'unknown'
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тест
# если не модуль, то выполнить
if __name__ == '__main__':
    # получаем имя ОС
    os_name = OsName().os_name_get()
    # вывод в консоль имени ОС
    print('ОС:', os_name)
    # вывод дукументации класса
    print(OsName.__doc__)
    # вывод дукументации метода
    print(OsName().os_name_get.__doc__)
# *****************************************************************************************