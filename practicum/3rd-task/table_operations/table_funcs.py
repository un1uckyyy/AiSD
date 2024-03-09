from txt_funcs import Table


def get_rows_by_number(table: Table, *interval, copy_table=False) -> Table:
    assert isinstance(table, Table), "it`s not a table"
    assert 1 <= len(interval) <= 2, 'invalid interval, enter 1 or 2 arguments'
    assert all([isinstance(interval[i], int) for i in range(len(interval))])
    assert interval[0] <= interval[-1], 'invalid interval, 2nd index must be greater than 1st'
    assert interval[0] > 0, 'number must be > 0'
    if copy_table:
        return Table(table[interval[0] - 1:interval[-1]])
    else:
        table.data = table[interval[0] - 1:interval[-1]]
        return table


def get_rows_by_index(table: Table, *vals, copy_table=False) -> Table:
    assert isinstance(table, Table), "it`s not a table"
    data = []
    for i in table.data:
        if i[table.keys[0]] in vals:
            data.append(i)
    if copy_table:
        return Table(data)
    else:
        table.data = data
        return table


def get_column_types(table: Table, by_number=True) -> dict:
    if by_number:
        return dict([(table.keys.index(k), type(v)) for k, v in table[0].items()])
    else:
        return dict([(k, type(v)) for k, v in table[0].items()])


# по дефолту для self.column_types сохраняем {индекс столбца:тип}
def set_column_types(table: Table, types_dict: dict, by_number=True):
    if by_number:
        table.column_types = types_dict
    else:
        # если types_dict = {название столбца: тип}, то приводим к {индекс столбца: тип}
        table.column_types = dict([(table.keys.index(k), v) for k, v in types_dict.items()])


def get_values(table: Table, column=0) -> list:
    assert table.column_types is not None, 'you should set_column_types before'
    if isinstance(column, int):
        assert column < len(table.keys), 'index out of range'
        assert column >= 0, 'index must be >= 0'
        ans = []
        for i in table:
            ans.append(table.column_types[column](i[table.keys[column]]))
        return ans
    else:
        assert column in table.keys, f'there is no column {column}'
        ans = []
        column_index = table.keys.index(column)
        for i in table:
            ans.append(table.column_types[column_index](i[column]))
        return ans


def get_value(table: Table, column=0):
    assert table.column_types is not None, 'you should set_column_types before'
    assert len(table) == 1, 'cant get value, because table has only one row, use get_values()'

    if isinstance(column, int):
        assert column < len(table.keys), 'index out of range'
        assert column >= 0, 'index must be >= 0'

        return table.column_types[column](table[0][table.keys[column]])
    else:
        assert column in table.keys, f'there is no column {column}'
        column_index = table.keys.index(column)
        return table.column_types[column_index](table[0][column])


def set_values(table: Table, values: list, column=0):
    assert table.column_types is not None, 'you should set_column_types before'
    assert len(values) == len(table), 'len(values) must be equal len(table)'

    if isinstance(column, int):
        assert column < len(table.keys), 'index out of range'
        assert column >= 0, 'index must be >= 0'
        key = table.keys[column]
        for ind in range(len(table)):
            table[ind][key] = table.column_types[column](values[ind])
    else:
        assert column in table.keys, f'there is no column {column}'

        column_index = table.keys.index(column)
        for ind in range(len(table)):
            table[ind][column] = table.column_types[column_index](values[ind])


def set_value(table: Table, value, column=0):
    assert table.column_types is not None, 'you should set_column_types before'
    assert len(table) == 1, 'cant set value, because table has only one row, use set_values()'

    if isinstance(column, int):
        assert column < len(table.keys), 'index out of range'
        assert column >= 0, 'index must be >= 0'
        key = table.keys[column]
        table[0][key] = table.column_types[column](value)
    else:
        assert column in table.keys, f'there is no column {column}'
        column_index = table.keys.index(column)
        table[0][column] = table.column_types[column_index](value)

