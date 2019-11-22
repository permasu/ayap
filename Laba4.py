# -*- coding: utf-8 -*-
class journal:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty
    def __repr__(self):
        return "%s, %r" % (self.name, self.faculty)
    def __str__(self):
        return "ФИО: %s, группа: %r" % (self.name, self.faculty)
    def test(self):
        return str(self)
    def __call__(self, *args):
        return  print("был вызван CALL:%s , %r" % (self.name,self.faculty))
    
my_list = [
    journal('Ахметшин Сергей', 'АСУ-19-1'),
    journal('Рожин Павел', 'АСУ-19-1')
]
print('Демонстрация lambda')
printjournal=lambda x: print("ФИО: %s, группа: %r" % (x.name, x.faculty))
for x in my_list:
    printjournal(x)
new_list= list(map(lambda x: x.name+" map",my_list))

print("Демонстрация map")
print(new_list)
print("Демонстрация reduce// Суммирование фамилий в списке")
from functools import reduce
sum_all_Fio=reduce(lambda x, y: x.name+" "+y.name, my_list)
print(sum_all_Fio)
print("Демонстрация filter//отфильтруем элементы с имеющимся вхождением строки Ахметшин Сергей в фио")
filt = list(filter(lambda x: x.name=='Ахметшин Сергей', my_list))
print(filt)