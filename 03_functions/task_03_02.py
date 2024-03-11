from typing import Callable

friends = [
    {'name': 'Bob',
     'gender': 'male', 'sport': 'Basketball', 'email': 'email@e.com'},
    {'name': 'Emily',
     'gender': 'female', 'sport': 'Running', 'email': 'email1@e.com'},
    {'name': 'Dima',
     'gender': 'male', 'sport': 'Ski', 'email': 'email@e.com'},
    {'name': 'Xsuha',
     'gender': 'female', 'sport': 'Snowboard', 'email': 'ksu@e.com'},
]


def select(*field_names: str) -> Callable:
    """
    :param field_names:список полей, которые должны быть в результирующем списке
    :type field_names:
    :return: function for selection
    :rtype: Callable
    """

    def inner(di: dict):
        """
        :param di: dict from some list
        :type di: dict
        :return: dict with keys from fields_names list only
        :rtype: dict
        """
        new_d = {f: di.get(f) for f in field_names}
        return new_d

    return inner


def field_filter(field_name: str, field_values: list) -> Callable:
    """
    функция принимает имя по кот. необходимо фильтровать и итерируемый объект -
    значения которые должны быть в результирующем списке
    :param field_name: field name - key for some dictionary
    :type field_name: str
    :param field_values: list of possible string values for filtration
    aka select .. where field_name in (field_values)
    :type field_values: list of str
    :return: функцию для оценки условий
    :rtype: Callable
    """

    def inner(di: dict) -> bool:
        """
        :param di: dict, который нужно оценить на
            соответсвие условиям фильтрации из параметров внешней функции
        :type di: dict
        :return: true если условие фильтрации выполняется
        :rtype: bool
        """
        return di.get(field_name) in field_values

    return inner


def query(collection: list, f_column_filter: Callable,
          *f_row_filters: Callable) -> list:
    """
     функция которая действительно выбирает нужные поля и фильтрует их.
    :param collection: input list of dict
    :type collection: list
    :param f_column_filter: функция вертикальной фильтрации (выбор колонок)
    :type f_column_filter: Callable
    :param f_row_filters: функции горизонтальной фильтрации (выбор строк)
    :type f_row_filters: Callable
    :return: Отфильтрованный вертикально и горизантально list of dict
    :rtype: list
    """
    return [f_column_filter(item) for item in collection
            if all([f_row_filter(item) for f_row_filter in f_row_filters])
            ]


# tests
test1_output = query(friends,
                     select('name', 'gender', 'sport'),
                     field_filter(field_name='sport',
                                  field_values=['Ski', 'Running']),
                     field_filter(field_name='gender', field_values=['male'])
                     )
for d in test1_output:
    print(d)
