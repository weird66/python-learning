class Person:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.address = adress

    def introduce(self):
        print(f"{self.name}, {self.address}, {self.age} years old.")

class PersonManager:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def list_people(self):
        for person in self.people:
            person.introduce()
    def find_person(self, name):
        for person in self.people:
            if person.name == name:
                return person
        return None


def main():
    manager = PersonManager()
    while True:
        name = input('Please input your name: ')
        age = input('Please input your age: ')
        address = input('Please input your address: ')
        person = Person(name, age, address)        
        manager.add_person(person)
        manager.list_people()

        moveNext = input('Add more? y/n')
        if moveNext == 'n':
            break

    name = input('Please input the name you want to find: ')
    person = manager.find_person(name)
    if person:
        years = input('Please input the years you want to add: ')
        person.age = int(person.age) + int(years)
        person.introduce()
    else:
        print('Not found')



if __name__ == "__main__":
    main()
