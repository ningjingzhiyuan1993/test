#!/bin/python3
#-*- coding:utf-8 -*-

'a class test '

__author__ = 'sauron'

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def printScore(self):
        print('%s score is %s' % (self.__name, self.__score))

    def get_grace(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        elif self.__score >= 70:
            return 'C'
        else:
            return 'D'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.printScore()
lisa.printScore()
print(bart.get_grace(), lisa.get_grace())
