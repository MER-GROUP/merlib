'''
class Buffer - класс для работы с буфером обмена информации

Дополнительные сторонние модули для обработки файлов
    clipboard
    threading
    time

Реализация методов класса - Макс Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# работы с буфером обмена информации
import clipboard
# поток таймер
from threading import Timer
# работа со временем 
# sleep - пауза во времени
from time import sleep
# *****************************************************************************************
# Buffer - автоматическая локализация программы на родной язык
class Buffer:
    '''
    class Buffer - класс для работы с буфером обмена информации\n
    методы:\n
        copy_info_get(self) -> str\n
        copy_info_set(self, info: str) -> None\n
    '''
    # ---------------------------------------------------------------------------
    # vars
    # блокировка буфера обмена выключена
    check_lock = False
    # для потока Timer
    timer = None
    # для теста метода Lock
    step = int()
    # ---------------------------------------------------------------------------
    # Возвращает из буфера обмена информации последнюю скопированную информацию
    def copy_info_get(self) -> str:
        '''
        Eng:\n
        Returns the last copied information from the clipboard.\n
        Rus:\n
        Возвращает из буфера обмена информации последнюю скопированную информацию.\n
        '''
        try:
            return clipboard.paste()
        except (Exception) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # Копирует информацию в буфер обмена
    def copy_info_set(self, info: str) -> None:
        '''
        Eng:\n
        Copies the information to the clipboard.\n
        :param info: information to be pasted to the clipboard.\n
        Rus:\n
        Копирует информацию в буфер обмена.\n
        :параметр info: информация которую нужно вставить в буфер обмена.\n
        '''
        try:
            clipboard.copy(info)
        except (Exception) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # Блокирует буфер обмена (запрет копирования)
    def lock(self) -> None:
        '''
        Eng:\n
        Blocks the clipboard (prohibits copying).\n
        Rus:\n
        Блокирует буфер обмена (запрет копирования).\n
        '''
        try:
            self.timer = Timer(0.5, self.__lock_private)
            self.timer.start()
        except (Exception) as e:
            return str(e)

    # алгоритм для метода lock
    def __lock_private(self) -> None:
        '''
        Eng:\n
        Algorithm for the lock method.\n
        Rus:\n
        Алгоритм для метода lock.\n
        '''
        try:
            # test #########################################
            print(f'__lock_private is work {self.step}') ###
            self.step += 1 #################################
            self.timer = Timer(0.5, self.__lock_private)
            self.timer.start()
        except (Exception) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # Снимает с блокировки буфер обмена
    def unlock(self) -> None:
        '''
        Eng:\n
        Removes the clipboard from the lock.\n
        Rus:\n
        Снимает с блокировки буфер обмена.\n
        '''
        try:
            self.timer.cancel()
        except (Exception) as e:
            return str(e)
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    print('-------------------------------------')
    print('+++++clipboard test+++++')
    # показывает последнюю информацию из буффера обмена
    print(f'{clipboard.paste()}')
    # вставляет информацию в буффера обмена
    clipboard.copy('RED ALERT')
    # показывает последнюю информацию из буффера обмена
    print(f'{clipboard.paste()}')
    print('-------------------------------------')
    print('+++++copy_info_get+++++')
    print(Buffer().copy_info_get())
    print('-------------------------------------')
    print('+++++copy_info_set+++++')
    Buffer().copy_info_set('Max Ramanenka')
    print(Buffer().copy_info_get())
    print('-------------------------------------')
    print('+++++lock+++++')
    print(Buffer().lock())
    print('-------------------------------------')
    print('+++++sleep+++++')
    sleep(5)
# *****************************************************************************************