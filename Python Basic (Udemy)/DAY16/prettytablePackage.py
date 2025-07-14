from patsy.state import center
from prettytable import PrettyTable

table = PrettyTable()

# print(table)

table.field_names = ['Name', 'Age', 'City']
table.add_row(['Alice', 24, 'New York'])
table.add_row(['Bob', 27, 'San Francisco'])
table.add_column("Distance", [50, 100])

table.align = "c" # "l" , "r"

print(table)