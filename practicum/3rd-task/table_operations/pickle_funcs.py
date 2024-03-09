import pickle
from txt_funcs import Table


def load_table_pickle(filename: str) -> Table:
    with open(filename, 'rb') as f:
        return Table(pickle.load(f))


def save_table_pickle(table: Table, filename: str):
    assert isinstance(table, Table), "it`s not a table"
    with open(filename, 'wb') as f:
        pickle.dump(table.data, f)
