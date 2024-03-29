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
        print_screen_is_exit_wait_input(self) -> None
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
            # # test ##########################
            # print('print_screen_is_exit') ###
            # listener - создажем неблокирующий слушатель клавиатуры
            listener = ListenerPrintScreen(
                    on_press=self.__on_press_print_screen
                    )
            listener.start()
        except (Exception) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # При нажатии на кнопку print_screen происходит выход из программы
    def print_screen_is_exit_wait_input(self) -> None:
        '''
        Eng:\n
        When you click on the print_screen button, the program exits,\n
            but you need to wait for the button to be pressed.\n
        Rus:\n
        При нажатии на кнопку print_screen происходит выход из программы,\n
            но нужно ждать нажатия кнопки.\n
        '''
        try:
            # # test #####################################
            # print('print_screen_is_exit_wait_input') ###
            # блок `with` слушает события до выхода 
            # до остановки слушателя
            # with keyboard.Listener(
            with ListenerPrintScreen(
                    on_press=self.__on_press_print_screen
                    ) as listener:
                listener.join()
        except (Exception) as e:
            return str(e)
    # ---------------------------------------------------------------------------
    # для прослушивания клавиатуры
    def __on_press_print_screen(self, key) -> None:
        try:
            # если нажата кнопка print_screen
            if key == keyboard.Key.print_screen:
                # # test #######################
                # print('Exit programm ...') ###
                # остановить слушатель клавиатуры
                ListenerPrintScreen.stop
                # выход из программы
                __import__('os').abort()
                # __import__('sys').exit()
                # exit(0)
                # sys.exit
                # os.abort()
                # raise SystemExit
                # raise SystemExit(1)
                # raise Exception
            # # test ###########################################################
            # else:                                                          ###
            #     try:                                                       ###
            #         print(f'Нажата буквенно-цифровая клавиша: {key.char}') ###
            #     except AttributeError:                                     ###
            #         print(f'Нажата специальная клавиша: {key}')            ###
        except AttributeError as e:
            return str(e)
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# тесты
# если не модуль то выполнить программу
if __name__ == '__main__':
    print('-------------------------------------')
    print('+++++print_screen_is_exit_wait_input+++++')
    my_keyboard = Keyboard()
    # method
    # Keyboard().print_screen_is_exit_wait_input()
    # my_keyboard.print_screen_is_exit_wait_input()
    print('-------------------------------------')
    print('+++++print_screen_is_exit+++++')
    # method
    # my_keyboard.print_screen_is_exit_wait_input()
    my_keyboard.print_screen_is_exit()
    for i in range (1, 61):
        __import__('time').sleep(1)
        print(f'{i} секунда')
# *****************************************************************************************