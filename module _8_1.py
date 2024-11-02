def add_everything_up( a,b ): #Функция принимает значение А и В
    try: # создаем блок try для проверки на ошибки
        print(a + b) # вывод значения ошибки
    except TypeError: # создаем блок except
        print(str(a) + str(b)) # возвращать строковое представление этих двух А и В
    #
add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)