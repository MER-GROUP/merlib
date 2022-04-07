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
        os_name_get() -> str                                 
                возвращает имя ОС               
                возвращаемое значение - str (текстовая строка) 
                возвращаемые str значения:
                        android
                        linux
                        mac
                        win
                        other
        '''
        if hasattr(sys, 'getandroidapilevel'):
            # android
            # print('android')
            return 'android'
        elif _platform == "linux" or _platform == "linux2":
            # linux
            # print('linux')
            # print(_platform)
            return 'linux'
        elif _platform == "darwin":
            # MAC OS X
            # print('Mac OS')
            # print(_platform)
            return 'mac'
        elif _platform == "win32":
            # Windows
            # print('Windows 32')
            # print(_platform)
            return 'win'
        elif _platform == "win64":
            # Windows 64-bit
            # print('Windows 32')
            # print(_platform)
            return 'win'
        else:
            # other
            # print('other')
            return 'other'
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