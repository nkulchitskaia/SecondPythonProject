class Person:
    def __init__(self, name, gender, age,):
        self.__name = name
        self.__age = age
        self.__gender = gender


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    def get_gender(self):
        return self.__gender


    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
    def set_gender(self, gender):
        self.__gender = gender


    def info(self):
        print(f'name = {self.__name}\n'
              f'age = {self.__age}\n'
              f'gender = {self.__gender}')



person = Person('Pasha', 'man', 29)
person1 = Person('Sasha', 'man', 27)
person2 = Person('Natasha', 'women', 77)
person3 = Person('Nikita', 'man', 66)


list = [person, person1, person2, person3]
oldest_person = person

for i in list:
    if i.get_age() > oldest_person.get_age():
        oldest_person = i
oldest_person.info()