# -*- coding: utf-8 -*-
import unittest


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
        return print("был вызван CALL:%s , %r" % (self.name, self.faculty))

    def __lt__(self, other):
        return self.name < other.name
    def __eq__(self, other):
        return self.name == other.name and self.faculty == other.faculty


def SortJournal(slist):
    slisttemp=slist
    for i in range(len(slisttemp) - 1):
        for j in range(len(slisttemp) - i - 1):
            if (slisttemp[j + 1] < slisttemp[j]):
                slisttemp[j], slisttemp[j + 1] = slisttemp[j + 1], slisttemp[j]
    return slisttemp


class SortMyListTest(unittest.TestCase):
    def test_normal(self):
        res = SortJournal([journal('Ахметшин Сергей', 'АСУ-19-1'),
                            journal('Шарифханов Артем', 'АСУ-19-1'),
                            journal('Трошева Кристина', 'АСУ-19-1'),
                            journal('Рожин Павел', 'АСУ-19-1')])
        self.assertEqual(res, [journal('Ахметшин Сергей', 'АСУ-19-1'),
                               journal('Рожин Павел', 'АСУ-19-1'),
                               journal('Трошева Кристина', 'АСУ-19-1'),
                               journal('Шарифханов Артем', 'АСУ-19-1')])

    def test_single(self):
        res = SortJournal([journal('Ахметшин Сергей', 'АСУ-19-1')])
        self.assertEqual(res, [journal('Ахметшин Сергей', 'АСУ-19-1')])


if __name__ == '__main__':
    unittest.main()

