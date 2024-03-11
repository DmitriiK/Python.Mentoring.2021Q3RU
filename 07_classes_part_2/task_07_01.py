# example from https://docs.python.org/3/howto/descriptor.html#properties
class Prop:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None):
        self.fget = fget

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)

    def __set__(self, instance, owner):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, owner)

    def setter(self, fset):
        self.fset = fset
        return self
        # return type(self)(self.fget, fset, self.fdel, self.__doc__)


class Something:
    def __init__(self, x):
        self.x = x

    @Prop
    # В prop поступает ссылка на метод attr. prop возвращает нам
    # ссылку на экземпляр класса prop, в котором уже установлена ссылка
    # на метод.
    # И в пространстве имен класса Something переменной attr присваивается
    # ссылка на класс prop
    def attr(self):
        return self.x ** 2

    @attr.setter
    def attr_setter(self, update):
        self.x = update
        return self.x

    # attr_setter=attr.setter(attr_setter)
