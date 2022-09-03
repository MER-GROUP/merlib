'''
class DateTime - класс для работы с датой и временем устройства

Дополнительные сторонние модули для обработки файлов
    requests
    datetime

Реализация методов класса - Макс Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# module
# работа с HTTP
import requests
# работа работа с датой и временем
from datetime import datetime
# *****************************************************************************************
# DateTime - класс для работы с датой и временем устройства
class DateTime:
    '''
    class DateTime - класс для работы с датой и временем устройства\n
    методы:\n
        date_current_get(self) -> datetime
        date_current_get_from_net(self) -> datetime\n
        date_current_show_from_net(self) -> str\n
    '''
    # ---------------------------------------------------------------------------
    # vars
    pass
    # ---------------------------------------------------------------------------
    # Получить текущуюю дату взятую с устройства
    def date_current_get(self) -> datetime:
        '''
        Eng:\n
        Get the current date taken from the device.\n
        Rus:\n
        Получить текущуюю дату взятую с устройства.\n
        '''
        try:
            return datetime.now()
        except (Exception) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # Получить текущуюю дату взятую из интернета
    def date_current_get_from_net(self) -> datetime:
        '''
        Eng:\n
        Get the current date taken from the internet.\n
        Rus:\n
        Получить текущую дату взятую из интернета.\n
        '''
        try:
            # делаем get запрос
            res = requests.get('http://just-the-time.appspot.com/')
            # получить код (текст) страницы
            data = res.text
            # парсинг для даты
            data = data.split()
            date_arr = map(int, data[0].split('-'))
            return datetime(*date_arr)
        except (Exception) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # Показать текущуюю дату взятую из интернета
    def date_current_show_from_net(self) -> str:
        '''
        Eng:\n
        Show the current date taken from the internet.\n
        Rus:\n
        Показать текущую дату взятую из интернета.\n
        '''
        try:
            cur_date = self.date_current_get_from_net()
            year = cur_date.year
            month = cur_date.month
            day = cur_date.day
            return str(day) + '.' + str(month) + '.' + str(year)
        except (Exception) as e:
            return str(e)
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    print('-------------------------------------')
    # method
    print('+++++date_current_get_from_net+++++')
    print(DateTime().date_current_get_from_net())
    print('+++++date_current_show_from_net+++++')
    print(DateTime().date_current_show_from_net())
    print('+++++date_current_get+++++')
    print(DateTime().date_current_get())
    pass
# *****************************************************************************************