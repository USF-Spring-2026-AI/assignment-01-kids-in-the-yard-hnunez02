"""
Person class
for building a person in tree
"""


class Person:
    # give person attributes, name, year born, etc.
    def __init__(self, year_born, first_name, last_name, year_died):
        self.year_born = year_born
        self.first_name = first_name
        self.last_name = last_name
        self.spouse = None
        self.children = []
        self.year_died = year_died

    # getters for all attributes
    def get_year_born(self):
        return self.year_born

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_year_died(self):
        return self.year_died

    # spouse will be object set as a separate person
    def set_spouse(self, spouse):
        self.spouse = spouse
    # child will be object added to current persons children

    def add_child(self, child):
        self.children.append(child)
