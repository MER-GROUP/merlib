# импорт класса BogoSort
from BogoSort import BogoSort
# импорт модуля random
# shuffle() - перемешивает список случайным образом
from random import shuffle

# тест
# если не модуль, то выполнить
if __name__ == '__main__':
    # создаем список
    numbers = list(range(10))
    # перемешиваем начальный список
    shuffle(numbers)
    # выводим начальный список
    print(numbers)
    # сортируем список болотной сортировкой
    sorted_numbers = BogoSort().bogosort(numbers)
    # выводим отсортированный список
    print(sorted_numbers)