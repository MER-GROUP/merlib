'''
class Keyboard - класс для работы с клавиатурай устройства

Дополнительные сторонние модули для обработки файлов
    pynput

Реализация методов класса - Макс Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# module
# Управление клавиатурой
from pynput.keyboard import Key, Controller
# Мониторинг клавиатуры
from pynput import keyboard
# *****************************************************************************************
# создаем слушателя для клавиатуры (для кнопки print_screen)
class ListenerPrintScreen(keyboard.Listener):
    pass
# *****************************************************************************************
# Keyboard - класс для работы с клавиатурай устройства
class Keyboard:
    '''
    class Keyboard - класс для работы с клавиатурай устройства\n
    методы:\n
        print_screen_is_exit(self) -> None\n
    '''
    # ---------------------------------------------------------------------------
    # vars
    pass
    # ---------------------------------------------------------------------------
    # При нажатии на кнопку print_screen происходит выход из программы
    def print_screen_is_exit(self) -> None:
        '''
        Eng:\n
        When you click on the print_screen button, the program exits.\n
        Rus:\n
        При нажатии на кнопку print_screen происходит выход из программы.\n
        '''
        try:
            # блок `with` слушает события до выхода 
            # до остановки слушателя
            # with keyboard.Listener(
            with ListenerPrintScreen(
                    on_press=self.__on_press
                    ) as listener:
                listener.join()
        except (Exception) as e:
            return str(e)

    # для прослушивания клавиатуры
    def __on_press(key):
        try:
            # если нажата кнопка print_screen
            if key == keyboard.Key.print_screen:
                # test
                print('Exit programm ...')
                # остановить слушатель клавиатуры
                ListenerPrintScreen.stop()
                # выход из программы
                exit()
        except AttributeError as e:
            return str(e)
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    print('-------------------------------------')
    print('+++++method+++++')
    # method
    pass
# *****************************************************************************************