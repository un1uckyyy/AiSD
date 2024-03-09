from typing import List, Hashable, Any


# класс
# внутреннее представление таблицы - экземпляр соответствующего класса
# при инициализации принимает список словарей с одинаковыми ключами
# (ключ - название столбца; значение - соответствующее значение для данной строки)
class Table:
    def __init__(self, data: List[dict[Hashable, Any]]):
        self.data = data
        assert (all(data[0].keys() == i.keys() for i in data)), "different names of coles"
        assert data, "not table"
        self.keys = list(data[0].keys())
        self.column_types = None

    # функция для выравнивания таблицы при выводе ее на печать в терминал
    # или записи в .txt файл
    def get_max_len_of_element_in_col(self) -> dict:
        max_len_of_element_in_col = dict([(col, len(str(col))) for col in self.keys])
        for el in self.data:
            for col in el.keys():
                max_len_of_element_in_col[col] = max(max_len_of_element_in_col[col], len(str(el[col])))

        return max_len_of_element_in_col

    def print_table(self):
        max_len_of_element_in_col = self.get_max_len_of_element_in_col()
        ans = '|'.join([str(col).center(max_len_of_element_in_col[col]) for col in self.keys]) + '\n'
        ans += '-' * (sum([i for i in max_len_of_element_in_col.values()]) + len(self.keys) - 1) + '\n'
        for el in self.data:
            ans += '|'.join([str(el[col]).center(max_len_of_element_in_col[col]) for col in el.keys()]) + '\n'
        return ans

    def __str__(self):
        return self.print_table()

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)


def save_table_txt(table: Table, filename: str):
    assert isinstance(table, Table), "it`s not a table"
    with open(filename, 'w') as f:
        f.write(table.print_table())
