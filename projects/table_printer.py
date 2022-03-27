'''Table Printer

Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose'''

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(table: list[list[str]]):
    col = len(table)
    row = len(table[0])
    max_width = [max([len(item) for item in arr]) for arr in table]

    for i in range(row):
        for j in range(col):
            print(table[j][i].rjust(max_width[j]), end=' ')
        print()


print_table(table_data)
