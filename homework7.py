my_dict = {'Иван': 1979, 'Максим': 2006, 'Константин': 1955,
           'Сергей': 2001, 'Анастасия': 2016}
print(my_dict)
print('Дата рождения Максима: ', my_dict['Максим'], 'год')
my_dict['Мария'] = 1973
print('Дата рождения Марии: ', my_dict['Мария'], 'год')
my_dict.update({'Глеб': 1963,
                'Татьяна': 1979})
del_accaunt = my_dict .pop('Максим')
print('Учётная запись Максима -', del_accaunt,
      'год рождения, удалена из справочника')
print('Modified dictionary: ', my_dict)
my_set = {1, 1, 2, 4, 4, 8, 8, (1, 2, 3), (1, 2, 3),
          (4, 5, 6), 3, 5, 2.45, 2.45, 4.88, 'next', 'next'}
print(my_set)
my_set .update({18, 18, 24})
my_set .discard((1, 2, 3))
print(my_set)
