grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print('Оценки = ', grades)
print('Студенты = ', students)
GPA = list(map(lambda x: sum(x)/len(x), grades))
GPA_dict = dict(list(zip(students, GPA)))
print('Словарь оценок студентов: ', GPA_dict)
#
print("Улучшенный вариант с округлением среднего балла:")
#
GPA = list(map(lambda x: round(sum(x)/len(x)), grades))
GPA_dict = dict(list(zip(students, GPA)))
print('Словарь оценок студентов: ', GPA_dict)
