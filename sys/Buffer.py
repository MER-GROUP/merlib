'''
class Buffer - класс для работы с буффером обмена информации

Дополнительные сторонние модули для обработки файлов
    clipboard

Реализация методов класса - Макс Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
import clipboard
# *****************************************************************************************
# Translate - автоматическая локализация программы на родной язык
class Translate:
    '''
    class Translate - класс для работы с буффером обмена информации\n
    методы:\n
        get_translate(self, lang: str, name: str) -> str\n
    '''
    # ---------------------------------------------------------------------------
    # Возвращает из буффера обмена информации последнюю скопированную информацию
    def copy_info_get(self) -> str:
        '''
        Eng:\n
        Returns the last copied information from the clipboard.\n
        Rus:\n
        Возвращает из буфера обмена информации последнюю скопированную информацию.\n
        '''
        try:
            return clipboard.copy()
        except (Exception):
            return 'KeyError'
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
# *****************************************************************************************