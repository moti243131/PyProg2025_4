# PyProg2025_4

Глушков Матвей группа P3120
Lab3: Бинарное дерево
Программа для построения бинарного дерева рекурсивным способом с несколькими вариантами представления структуры.

Вывод покажет дерево в четырёх форматах: dict, list, namedtuple, OrderedDict.

Запуск тестов
python -m pytest test_binary_tree.py -v
Использование в коде
from binary_tree import gen_bin_tree

# С параметрами по умолчанию (root=13, height=3)
tree = gen_bin_tree()

# С произвольными параметрами
tree = gen_bin_tree(height=4, root=100)

# Выбор формата представления
tree_dict = gen_bin_tree(structure="dict")         # базовый
tree_list = gen_bin_tree(structure="list")
tree_nt = gen_bin_tree(structure="namedtuple")
tree_od = gen_bin_tree(structure="ordered_dict")
Описание программы
Алгоритм
Функция gen_bin_tree строит бинарное дерево рекурсивно:

Базовый случай: при height <= 1 возвращается только корень без потомков.
Рекурсия: при height > 1:
левый потомок = root + 1
правый потомок = root - 1
для каждого потомка вызывается gen_bin_tree(height - 1, потомок).
Параметры
Параметр	По умолчанию	Описание
height	3	Высота дерева
root	13	Значение в корне (вариант задания)
structure	"dict"	Формат: dict, list, namedtuple, ordered_dict
Форматы представления
Dict (базовый):

{"root": 13, "left": {...}, "right": {...}}
List:

[root, left_subtree, right_subtree]
NamedTuple (collections):

Node(root=13, left=Node(...), right=Node(...))
OrderedDict (collections):

OrderedDict([("root", 13), ("left", ...), ("right", ...)])
Пример дерева (root=13, height=3)
        13
       /  \
     14    12
    / \   / \
  15  13 13  11
