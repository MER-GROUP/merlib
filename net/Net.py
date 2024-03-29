'''
class Net - класс для работы с интернетом

Дополнительные сторонние модули для обработки файлов
    requests

Реализация методов класса - Макс Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# module
# работа с HTTP
import requests
# *****************************************************************************************
# Net - класс для работы с интернетом
class Net:
    '''
    class Net - класс для работы с интернетом\n
    методы:\n
        is_internet(self) -> bool\n
    '''
    # ---------------------------------------------------------------------------
    # vars
    pass
    # ---------------------------------------------------------------------------
    # Проверяет есть ли подключение к интернету
    def is_internet(self) -> bool:
        '''
        Eng:\n
        Checks if there is an internet connection.\n
        Rus:\n
        Проверяет есть ли подключение к интернету.\n
        '''
        try:
            # делаем get запрос
            res = requests.get('http://just-the-time.appspot.com/')
            return True
        except (Exception) as e:
            # return str(e)
            return False
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    print('-------------------------------------')
    # method
    print('+++++is_internet+++++')
    if Net().is_internet():
        print('Internet is connect')
    else:
        print('Internet is NOT connect')
# *****************************************************************************************