#!/usr/bin/python3

""" ABC """

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This is the animal.
    """

    @abstractmethod
    def sound(self):
        """
        Sound of animal.
        """
        pass


class Dog(Animal):
    """
    This is the dog.
    """

    def sound(self):
        """
        Sound of dog.
        """
        return "Bark"


class Cat(Animal):
    """
    This is the cat.
    """

    def sound(self):
        """
        Sound of cat.
        """
        return "Meow"
