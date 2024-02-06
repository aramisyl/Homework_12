class Employee:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        print(f'Сотрудник: {self.name}, должность: {self.position}, заработная плата: {self.salary}.')

class Manager(Employee):

    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.subordinates = []
    def get_info(self):
        print(f'Сотрудник: {self.name}, должность: {self.position}, заработная плата: {self.salary}, количество подчиненных: {len(self.subordinates)}')

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def remove_subordinate(self, subordinate):
        if subordinate in self.subordinates:
            self.subordinates.remove(subordinate)