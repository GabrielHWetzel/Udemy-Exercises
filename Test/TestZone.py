class User:

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        return self.name.upper()

    def age(self, current_year):
        return current_year - self.birth_year


john = User("John", 1999)
print(john.age(2023))
print(john.get_name())
