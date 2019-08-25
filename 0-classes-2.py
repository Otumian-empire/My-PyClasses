# implementing my own class, continent class
class Continent:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def set_continent_name(self, name):
        self.name = name

    def set_continent_population(self, population):
        self.population = population

    def get_continent_name(self):
        return self.name

    def get_continent_population(self):
        return self.population

    def display_info(self):
        print(f"Name of continent: {self.get_continent_name}")
        print(f"Population of continent: {self.get_continent_population}")


class Africa(Continent):

    def print_complexity(self):
        print("Complexity Dark")


africa = Africa("", 0)

africa.set_continent_name("African")
africa.set_continent_population(1200000)

africa.display_info()
africa.print_complexity()