# string_1 = 'это новая строка'
# string_2 = 'это моя строка'
# print(string_2[0])
# print(string_2[-1])
# print(string_2[2:5])
# print(string_2[::-1])
# print(len(string_2))
# print(string_2,string_1)
#  
# В соответствии с изменением в задании новый код:
# 
example = 'это моя строка для примера'
print(example[0])
print(example[-1])
# haif_example = len(example)//2-1
# print('Индекс (haif_example) = ', haif_example)
print(example[(len(example)//2-1)::])
print(example[2:14])
print(example[::-1])
print(len(example))
print(example[::2])
