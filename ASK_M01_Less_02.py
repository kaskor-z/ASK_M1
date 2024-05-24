# Код выполнения задания по устаревшим условиям

# um1 = 5
# num2 = 3
# sum = num1 + num2
# print(sum)
# result = sum + num1 * num2
# print(result)
#
# Код выполнения задания по обновлённым условиям
#
namber_of_homework = 75
number_of_hours_spent = 36
training_course_name = 'Python'
hours_spent_per_session = number_of_hours_spent // namber_of_homework
add_minit_spent_per_session = round((number_of_hours_spent % namber_of_homework) /
                               namber_of_homework * 60)
print('Курс: "', training_course_name, '" - всего задач:', namber_of_homework,
      '; затрачено часов:', number_of_hours_spent,
      '; среднее время выполнения:', hours_spent_per_session, 'часов ',
      add_minit_spent_per_session, 'минут.')
