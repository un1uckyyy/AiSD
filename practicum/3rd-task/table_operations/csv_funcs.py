import csv
from txt_funcs import Table


def load_table_csv(filename: str) -> Table:
    with open(filename, 'r') as f:
        return Table(list(csv.DictReader(f)))


def save_table_csv(table: Table, filename: str):
    assert isinstance(table, Table), "it`s not a table"
    with open(filename, 'w', newline='') as f:
        fieldnames = table.keys
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(table.data)
