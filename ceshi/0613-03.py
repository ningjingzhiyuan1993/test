#!/bin/python3
#-*- coding:utf-8 -*-

'a class test '

__author__ = 'sauron'

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printScore(self):
        print('%s score is %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.printScore()
lisa.printScore()
