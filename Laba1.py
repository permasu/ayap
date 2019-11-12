# -*- coding: utf-8 -*-
class journal:
    def __init__(self,name,faculty):
        self.name=name
        self.faculty=faculty
a = [journal('Ахметшин Сергей', 'АСУ-19-1'), journal('Рожин Павел','АСУ-19-1')]
print('Список группы')
for x in a:
    print("Имя: "+ x.name +" Группа: "+ x.faculty)