from table.py import Table
import random

class Openspace:

    def __init__(self, tables: list, number_of_tables: int = 6):
        self.tables=tables
        self.number_of_tables=number_of_tables
  
    def organize(self, names: list):
        free_tables=[]
        for table in self.tables:
            if table.has_free_spot:
                free_tables.append(table)
        for name in names:
            table=random.choice(free_tables)
            table.assign_seat(name)
            
