immutable_var = (4, 8.2, 'Strin_12', False, [ 7, 8, 9], True)
print(immutable_var)
    # для удобства, чтобы не прерывать исполнеие
       # из-за возникшей ошибки, я перенёс изменение элемент
       # картежа в конце кода
# создаю список состоящий из тех-же значений,
   # что и в составе кортеже
mutable_list = [4, 8.2, 'Strin_12', False, [ 7, 8, 9], True]
print(mutable_list)
mutable_list [1] = 17.98
print(mutable_list)
   # преобразую список в Картеж
immutable_var_1 = tuple(mutable_list)
print(immutable_var_1)
print(immutable_var_1 [1])
   # пытаюсь изменить 2-ой элемент картежа
immutable_var_1 [1] = 8.2
   # возникла ошибка, потому что кортеж не поддерживает
   # обращение по элементам. Кортеж является не изменяемым объектом.