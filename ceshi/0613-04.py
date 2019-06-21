#!/bin/python3
#-*- coding:utf-8 -*-

__author__ = 'sauron'

class Animal(object):
    def run(self):
        print('Animal is running')

    def run_two(animal):
        animal.run()
        animal.run()

class Cat(Animal):
    def run(self):
        print('cat is running')

animal = Animal()
cat = Cat()
cat.run()

a = Cat()
print(isinstance(a, Animal))
print(isinstance(a, Cat))
animal.run_two()
a.run_two()
