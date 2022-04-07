'''
Болотная сортировка (Bogosort) — неэффективный алгоритм сортировки, 
используемый только в образовательных целях и противопоставляемый другим, 
более реалистичным алгоритмам.

Принцип работы алгоритма прост, как плесень. 
Перетряхиваем список случайным образом до тех пор пока 
он внезапно не отсортируется. Процесс может счастливо 
завершиться сразу, а может длиться до тепловой 
смерти Вселенной. Это уж как повезёт.

Колода в 32 карты будет сортироваться компьютером в среднем 2,7 * 10^19 лет.

Реализация алгоритма - Максим Романенко (Red Alert) - 2022г.
'''
# *****************************************************************************************
# импорт модуля random
# shuffle() - перемешивает список случайным образом
from random import shuffle
# *****************************************************************************************
cdef class BogoSort:
    '''
    class BogoSort - болотная сортировка                     
    методы:            
        __is_sort(numbers) -> bool
        bogosort(numbers) -> list
    информация:                                                      
        Установка модуля:                                        
            смотри файл BogoSortSetup.py                 
        Пример использования:                                    
            смотри файл BogoSortTest.py
    '''
    # ---------------------------------------------------------------------------
    # метод - проверяет отсортирован ли список
    cpdef __is_sort(self, numbers):
        '''
        __is_sort(numbers) -> bool  
                приватный метод
                проверяет отсортирован ли список                      
                возвращаемое значение - bool (true/false)               
        параметры:                                               
                numbers: list - список (массив) с числами
        '''
        # счетчик итерации
        cdef int i
        # список (массив) с числами
        cdef list nums = numbers

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
    # ---------------------------------------------------------------------------
    # реализация алгоритма болотной сортировки
    # Перетряхиваем список случайным образом до тех пор пока 
    # он внезапно не отсортируется. Процесс может счастливо 
    # завершиться сразу, а может длиться до тепловой 
    # смерти Вселенной. Это уж как повезёт.
    cpdef bogosort(self, numbers):
        '''
        bogosort(numbers) -> list  
                алгоритм болотной сортировки                    
                возвращаемое значение - list (отсортированный список)               
        параметры:                                        
                numbers: list - список (массив) с числами
        '''
        # список (массив) с числами
        cdef list nums = numbers

        while not self.__is_sort(nums):
            shuffle(nums)
        return nums
    # ---------------------------------------------------------------------------
# *****************************************************************************************