from prettytable import PrettyTable as _PrettyTable

def addColumn(table, fieldname, *column):
    table.add_colum(fieldname, column)

def addRow(table, *row):
    table.add_row(row)

def clear(table):
    table.clear()

def clearRows(table):
    table.clear_rows()

def delRow(table, row_index):
    table.del_row(row_index)

def Table(*field_names):
    return _PrettyTable(field_names)
