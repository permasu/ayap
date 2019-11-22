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
print('Список группы')
for x in my_list:
    print(x.test())
    #print(repr(x))
testCall=journal("ИмяТестCall","ГруппаТестCall")
testCall()