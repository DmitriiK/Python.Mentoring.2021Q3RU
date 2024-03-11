from __future__ import annotations
# it requires this to be able to use name of class
# - inside definition of this class (in type hints)

from abc import ABC, abstractmethod
from typing import Type


class Currency(ABC):
    _curr_rates = {
        ('Euro', 'Dollar'): 1.25,
        ('Euro', 'Ruble'): 89,
        ('Dollar', 'Ruble'): 75,
    }

    # taking as an assumption that buy and sell rates are the same

    def __init__(self, how_much: float):
        self.value = how_much
        super().__init__()

    @staticmethod
    @abstractmethod
    def currency_name() -> str:
        """
        Currency name
        :return: dollar, euro, or ruble or whatever
        :rtype: string
        """
        pass

    @classmethod
    @abstractmethod
    def currency(cls, how_much: float):
        """
        kind of currency fabric
        :param how_much:
        :type how_much: numeric
        :return: some money
        :rtype: instance of concrete Currency class
        """
        pass

    @staticmethod
    @abstractmethod
    def currency_sign():
        """
        :return: $ or euro or ruble of whatever sign
        :rtype:
        """
        pass

    def __str__(self):
        return f'{round(self.value, 2)} {self.currency_sign} '

    def __eq__(self, other: Currency):
        other_in_mine = other.to(self.__class__).value
        return self.value == other_in_mine

    def __mul__(self, other: float):
        return self.__class__(self.value * other)

    def __imul__(self, other: float):
        self.value *= other
        return self

    def __truediv__(self, other):
        return self.__class__(self.value / other)

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(self.value + other)
        if isinstance(other, Currency):
            rate = self.__class__.course(other.__class__)
            return self.__class__(self.value + other.value / rate)

    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(self.value + other)
        if isinstance(other, Currency):
            rate = self.__class__.course(other.__class__)
            return self.__class__(self.value + other.value / rate)

    def __sub__(self, other):
        other *= -1
        return self + other

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.value += other
            return self
        if isinstance(other, Currency):
            rate = self.__class__.course(other.__class__)
            self.value = self.value + other.value * rate
            return self
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.value > other
        if isinstance(other, Currency):
            rate = self.__class__.course(other.__class__)
            return self.value > other.value / rate

    @classmethod
    def course(cls, currency_to_convert: Type[Currency]) -> float:
        """
        class method to make instance of one currency from another
        :param currency_to_convert: Currency we want to convert from
        :type currency_to_convert: Currency
        :return: Currency we want to convert to
        :rtype: Currency
        """
        curr_pair = (cls.currency_name(), currency_to_convert.currency_name())

        if cls == currency_to_convert:
            return 1
        if curr_pair in cls._curr_rates:
            rate = cls._curr_rates.__getitem__(curr_pair)
            return rate
        if (curr_pair[1], curr_pair[0]) in cls._curr_rates:
            rate = cls._curr_rates.__getitem__((curr_pair[1], curr_pair[0]))
            return 1 / rate
        error_message = f'currency rate for {curr_pair} not defined'
        raise error_message

    @classmethod
    def set_course(cls, currency_to_convert: Type[Currency],
                   new_course: float):
        """
        kind of setter for determine new course
        :param currency_to_convert:
        :type currency_to_convert:
        :param new_course:
        :type new_course:
        :return: None
        :rtype:
        """
        cls._curr_rates[(cls.currency_name(),
                         currency_to_convert.currency_name())] = new_course

    def to(self, currency_to_convert: Type[Currency]):
        return currency_to_convert.currency(self.value * self.course(
            currency_to_convert))


class Euro(Currency):
    @staticmethod
    def currency_name():
        return 'Euro'

    @property
    def currency_sign(self):
        return '€'

    @classmethod
    def currency(cls, how_much):
        return cls(how_much)


class Dollar(Currency):
    @staticmethod
    def currency_name():
        return 'Dollar'

    @property
    def currency_sign(self):
        return '$'

    @classmethod
    def currency(cls, how_much):
        return cls(how_much)


class Ruble(Currency):
    @staticmethod
    def currency_name():
        return 'Ruble'

    @property
    def currency_sign(self):
        return 'руб.'

    @classmethod
    def currency(cls, how_much):
        return cls(how_much)
